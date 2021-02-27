import time
import re
from csgo_analysis.ingestion.models.db import DB
from csgo_analysis.ingestion.models.map import MapL


class Game(DB):

    # columns
    _ID = 'id'
    _SHARE_CODE = 'share_code'
    _MATCH_TIME = 'match_time'
    _MATCH_DURATION = 'match_duration'
    _MAP_L_ID = 'map_l_id'
    _FINAL_SCORE_TWO = 'final_score_two'
    _FINAL_SCORE_THREE = 'final_score_three'

    # table
    _TABLE_NAME = 'game'

    # parse re patterns
    matchtime_p = r'matchtime: (\d+)'
    match_info_p = r'match_result: \d\n.+ (\d{1,2})\n.+ (\d{1,2})\n.+: (\d+)'

    def __init__(self):
        super().__init__()
        self.map_l = MapL()
        self.fields = {}
        # team 2 CT start, team 3 T start?

    def convert_epoch_time(self, epoch_time):
        return time.strftime(self.timestamp_fmt, time.localtime(epoch_time))

    def ingest_data(self, dirty_data, scode, map_name):
        match_scores = re.search(self.match_info_p, dirty_data)
        epoch_time = int(re.search(self.matchtime_p, dirty_data).group(1))

        self.fields = {
            self._MATCH_TIME: self.convert_epoch_time(epoch_time),
            self._SHARE_CODE: scode,
            self._MATCH_DURATION: int(match_scores.group(3)),
            self._FINAL_SCORE_TWO: int(match_scores.group(1)),
            self._FINAL_SCORE_THREE: int(match_scores.group(2)),
            self._MAP_L_ID: self.map_l.get_map_l_id(map_name)
        }

        self.insert(
            tablename=self._TABLE_NAME,
            val=list(self.fields.values()),
            col=list(self.fields.keys())
        )

        # TODO return game_id
