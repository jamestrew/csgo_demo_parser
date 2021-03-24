
import bz2
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
from csgo_analysis.ingestion.models import Game, Player, DBConn
from csgo_analysis.ingestion.converter import JsonConverter
from csgo_analysis.ingestion.item_controller import ItemController
from csgo_analysis.ingestion.event_controller import EventsController

format = '[%(asctime)s] %(levelname)s %(name)s: %(message)s'
# logging.basicConfig(format=format, level=logging.DEBUG)


class Parser:

    min_flags = '-gameevents -extrainfo -nofootsteps -nowarmup -stringtables'

    def __init__(self):
        self.game_data = {}

    def get_match_data(self, share_url):
        ''' Call Steam API to gather basic match info '''
        self.client_complete = False
        self.scode = share_url[-34:]

        if self._code_exists():
            print(f'{self.scode} already ingested')
            return

        print(f'Analyzing {self.scode}')

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
            self.client_complete = True

        username = os.environ.get('RUKA_USER')
        password = os.environ.get('RUKA_PW')
        client.cli_login(username=username, password=password)

        while not self.client_complete:
            time.sleep(30)
        self.download_demo()

    def download_demo(self):
        ''' Download demo file and extract'''
        dl_link_p = r'map: "(.+\.bz2)"'
        game_dl_link = re.search(dl_link_p, self.raw_match_data).group(1)
        print('Downloading demo')
        file_name = urlparse(game_dl_link).path.replace('/730/', '')

        req = requests.get(game_dl_link, stream=True)

        temp_dl_path = os.path.join(definition.ING_DIR, 'data', file_name)
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
        ''' Call demoinfogo to parse demo'''
        exe_path = definition.ING_DIR
        self.dem_file = os.path.join('data', self.dem_file)
        self.output_path = self.dem_file.replace('.dem', '.txt')
        cmd = f'demoinfogo {self.dem_file} > {self.output_path} {self.min_flags}'
        print('Running demoinfogo....', end=' ')
        subprocess.call(cmd.split(), cwd=exe_path, shell=True)
        print('demoinfogo complete')
        with open(self.output_path, encoding='ascii', errors='replace') as data_file:
            self.data_txt = data_file.read()
        self.load_game_data()

    def load_game_data(self):
        ''' Ingest game table data from match data and demo into DB'''
        game = Game()
        map_name = re.search(r'\d, maps\/(de_[a-z2]+)\.bsp', self.data_txt).group(1)
        self.game_id = game.ingest_data(self.raw_match_data, self.scode, map_name)
        self.load_all_data()

    def load_all_data(self):
        ''' Convert demo data into json and ingest into DB'''
        self.data = JsonConverter.convert(self.data_txt, self.output_path, True)
        del self.data_txt
        player = Player(self.game_id, self.data)
        self.data = player.create_players()
        item_con = ItemController(self.data, player.player_list)
        self.data = item_con.sub_item_id()
        del item_con
        # with open('test.json', 'w') as jf:
        #     json.dump(self.data, jf)
        events_con = EventsController(self.game_id, self.data, player.player_list)
        events_con.ingest_prep()
        events_con.ingest_data()
        print('Data ingestion complete')

    def _code_exists(self):
        db = DBConn()
        where = {Game._SHARE_CODE: self.scode}
        data = db.select(Game._TABLE_NAME, WHERE=where)
        return len(data) > 0
