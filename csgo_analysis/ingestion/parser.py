
import bz2
import logging
import os
import re
import subprocess
import time
from urllib.parse import urlparse

import requests
from csgo import sharecode
from csgo.client import CSGOClient
from steam.client import SteamClient

import definition
from csgo_analysis.ingestion.models import Game

format = '[%(asctime)s] %(levelname)s %(name)s: %(message)s'
logging.basicConfig(format=format, level=logging.DEBUG)


class Parser:

    min_flags = '-gameevents -nofootsteps -nowarmup -stringtables'

    def __init__(self):
        self.game_data = {}

    def get_match_data(self, share_url):
        self.scode = share_url[-30:]
        try:
            match_params = sharecode.decode(self.scode)
        except ValueError:
            return False

        client = SteamClient()
        cs = CSGOClient(client)

        @client.on('logged_on')
        def start_csgo():
            cs.launch()

        @cs.on('ready')
        def return_clients():
            cs.request_full_match_info(**match_params)
            self.raw_match_data = str(cs.wait_event('full_match_info', 30))
            cs.exit()
            client.disconnect()
            self.download_demo()

        username = os.environ.get('RUKA_USER')
        password = os.environ.get('RUKA_PW')
        client.cli_login(username=username, password=password)
        client.run_forever()

    def download_demo(self):
        dl_link_p = r'map: "(.+\.bz2)"'
        game_dl_link = re.search(dl_link_p, self.raw_match_data).group(1)
        print('Downloading demo')
        file_name = urlparse(game_dl_link).path.replace('/730/', '')

        req = requests.get(game_dl_link, stream=True)

        temp_dl_path = os.path.join(definition.APP_DIR, 'ingestion', 'data', file_name)
        with open(temp_dl_path, 'wb') as bzip:
            bzip.write(req.content)

        zipfile = bz2.BZ2File(temp_dl_path)
        data = zipfile.read()
        self.dem_file = temp_dl_path.replace('.bz2', '')
        with open(self.dem_file, 'wb') as dem:
            dem.write(data)

        zipfile.close()
        os.remove(temp_dl_path)
        self.demo_parse()

    def demo_parse(self):
        exe_path = os.path.join(definition.APP_DIR, 'ingestion')
        output = os.path.join('data', self.dem_file.replace('.dem', '.txt'))
        self.dem_file = os.path.join('data', self.dem_file)
        cmd = f'demoinfogo {self.dem_file} > {output} {self.min_flags}'
        print(exe_path)
        sp_output = subprocess.run(cmd.split(), cwd=exe_path, shell=True)
        print(sp_output.returncode)

        print('Done')
        self.data_txt = open(output)

    def load_game_data(self):
        game = Game()
        map_name = re.search(r'\d, maps\/(de_[a-z2]+)\.bsp', self.data_txt).group(1)
        game.ingest_data(self.raw_match_data, self.scode, map_name)
        game.close()

    def test(self):
        print('good to go')
