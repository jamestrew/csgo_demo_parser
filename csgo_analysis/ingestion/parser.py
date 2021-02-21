import re
import os
import logging
from steam.client import SteamClient
from csgo.client import CSGOClient
from csgo import sharecode

format = '[%(asctime)s] %(levelname)s %(name)s: %(message)s'
logging.basicConfig(format=format, level=logging.DEBUG)


class Parser:

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
        print(self.game_data)
        print(self.game_dl_link)


if __name__ == '__main__':
    p = Parser()

    with open('csgo_analysis/ingestion/data/raw_match_data.txt') as file:
        data = file.read()

    p.match_info_cleaner(data)
