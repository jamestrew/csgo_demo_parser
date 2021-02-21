# take csgo demo share links and extract share code
# create steam and csgo client
# request_full_match_info
import os
import logging
from steam.client import SteamClient
from csgo.client import CSGOClient
from csgo import sharecode

format = '[%(asctime)s] %(levelname)s %(name)s: %(message)s'
logging.basicConfig(format=format, level=logging.DEBUG)


class Parser:

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
            return self.match_info_cleaner(raw_match_data)

        username = os.environ.get('RUKA_USER')
        password = os.environ.get('RUKA_PW')
        client.cli_login(username=username, password=password)
        client.run_forever()

    def match_info_cleaner(self, dirty_data):
        print(str(dirty_data))


if __name__ == '__main__':
    p = Parser()
    p.get_match_data('steam::url//fakeurl/CSGO-xQKYC-4Nbc4-h43V2-Jc66v-EWtrD')

