import gevent.monkey  # noqa
gevent.monkey.patch_all()  # noqa

import subprocess  # noqa
import time  # noqa
import bz2  # noqa
from urllib.parse import urlparse  # noqa
import definition  # noqa
from csgo import sharecode  # noqa
from csgo.client import CSGOClient  # noqa
from steam.client import SteamClient  # noqa
import logging  # noqa
import os  # noqa
import re  # noqa
import requests  # noqa


format = '[%(asctime)s] %(levelname)s %(name)s: %(message)s'
logging.basicConfig(format=format, level=logging.DEBUG)


class Parser:

    min_flags = '-gameevents -nofootsteps -nowarmup -stringtables'

    def __init__(self):
        self.game_data = {}

    def get_match_data(self, share_url):
        scode = share_url[-30:]
        try:
            match_params = sharecode.decode(scode)
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
            raw_match_data = cs.wait_event('full_match_info', 30)
            cs.exit()
            client.disconnect()
            self.match_info_cleaner(raw_match_data)

        username = os.environ.get('RUKA_USER')
        password = os.environ.get('RUKA_PW')
        client.cli_login(username=username, password=password)
        client.run_forever()

    def match_info_cleaner(self, dirty_data):
        matchtime_p = r'matchtime: (\d+)'
        match_info_p = r'match_result: \d\n.+(\d{1,2})\n.+(\d{1,2})\n.+: (\d+)'
        match_scores = re.search(match_info_p, dirty_data)

        self.game_data['match_time'] = re.search(matchtime_p, dirty_data).group(1)
        self.game_data['final_score_two'] = match_scores.group(1)
        self.game_data['final_score_three'] = match_scores.group(2)
        self.game_data['match_duration'] = match_scores.group(3)

        dl_link_p = r'map: "(.+\.bz2)"'
        self.game_dl_link = re.search(dl_link_p, dirty_data).group(1)
        self.download_demo()

    def download_demo(self):
        print('Downloading demo')
        file_name = urlparse(self.game_dl_link).path.replace('/730/', '')

        req = requests.get(self.game_dl_link, stream=True)

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
