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
        self.match_time = ''
        self.final_score_two = ''  # CT start ?
        self.final_score_three = ''  # T start ?
        self.match_duration = ''
        self.share_code = ''
        self.map_l = MapL()
        self.map_l_id = ''

    def ingest_data(self, dirty_data, scode, map_name):
        match_scores = re.search(self.match_info_p, dirty_data)

        epoch_time = int(re.search(self.matchtime_p, dirty_data).group(1))
        self.match_time = time.strftime(self.timestamp_fmt, time.localtime(epoch_time))
        self.final_score_two = match_scores.group(1)
        self.final_score_three = match_scores.group(2)
        self.match_duration = match_scores.group(3)
        self.share_code = scode
        self.map_l_id = self.map_l.get_map_l_id(map_name).value

        self.insert(
            self._TABLE_NAME,
            [
                self.share_code,
                self.match_time,
                self.match_duration,
                self.map_l_id,
                self.final_score_two,
                self.final_score_three
            ],
            [
                self._SHARE_CODE,
                self._MATCH_TIME,
                self._MATCH_DURATION,
                self._MAP_L_ID,
                self._FINAL_SCORE_TWO,
                self._FINAL_SCORE_THREE
            ]
        )
