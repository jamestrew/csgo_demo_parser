import time
import re
from csgo_analysis.ingestion.models.dbconn import DBConn
from csgo_analysis.ingestion.models.map import MapL
from csgo_analysis.ingestion.models.db import DB
from psycopg2._psycopg import TimestampFromTicks


class Game(DBConn, DB):

    # column names
    _ID = 'id'
    _SHARE_CODE = 'share_code'
    _MATCH_TIME = 'match_time'
    _MATCH_DURATION = 'match_duration'
    _MAP_L_ID = 'map_l_id'
    _FINAL_SCORE_TWO = 'final_score_two'
    _FINAL_SCORE_THREE = 'final_score_three'

    # column types
    _TYPES = {
        _ID: int,
        _SHARE_CODE: str,
        _MATCH_TIME: TimestampFromTicks,
        _MATCH_DURATION: int,
        _MAP_L_ID: int,
        _FINAL_SCORE_TWO: int,
        _FINAL_SCORE_THREE: int
    }

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

    def ingest_data(self, dirty_data, scode, map_name):
        match_scores = re.search(self.match_info_p, dirty_data)
        epoch_time = int(re.search(self.matchtime_p, dirty_data).group(1))

        self.input_column_data(self._SHARE_CODE, scode)
        self.input_column_data(self._MATCH_TIME, epoch_time)
        self.input_column_data(self._MATCH_DURATION, match_scores.group(3))
        self.input_column_data(self._MAP_L_ID, self.map_l.get_map_l_id(map_name))
        self.input_column_data(self._FINAL_SCORE_TWO, match_scores.group(1))
        self.input_column_data(self._FINAL_SCORE_THREE, match_scores.group(2))

        return self.insert(self._TABLE_NAME, self.fields, returning=True)[0]
