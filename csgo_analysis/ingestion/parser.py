# take csgo demo share links and extract share code
# create steam and csgo client
# request_full_match_info

from steam.client import SteamClient
from csgo.client import CSGOClient
from csgo import sharecode


class Parser:

    OK = 1

    def __init__(self):
        self.client = SteamClient()
        self.cs = CSGOClient()

        resp = self.client.cli_login()
        self.client.run_forever()

        if resp == self.OK:
            resp = self.cs.launch()

            if resp == self.OK:
                pass

    def get_match_data(self, share_url):
        # CSGO + the next 30 chars
        scode = share_url[-30:]
        try:
            scode = sharecode.decode(scode)
        except ValueError:
            return False

        self.cs


p = Parser()
p.get_match_data('steam://rungame/730/76561202255233023/+csgo_download_match%20CSGO-WHujK-oFZSm-azzvG-Sac3A-uT2JE')
p.get_match_data('bad link')
