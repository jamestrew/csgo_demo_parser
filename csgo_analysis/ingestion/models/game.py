import time
import re
from csgo_analysis.ingestion.models.dbconn import DBConn
from csgo_analysis.ingestion.models.map import MapL
from csgo_analysis.ingestion.models.db import DB
from psycopg2._psycopg import TimestampFromTicks


class Game(DBConn):

    # columns
    _ID = {DB._NAME: 'id', DB._TYPE: int}
    _SHARE_CODE = {DB._NAME: 'share_code', DB._TYPE: str}
    _MATCH_TIME = {DB._NAME: 'match_time', DB._TYPE: TimestampFromTicks}
    _MATCH_DURATION = {DB._NAME: 'match_duration', DB._TYPE: int}
    _MAP_L_ID = {DB._NAME: 'map_l_id', DB._TYPE: int}
    _FINAL_SCORE_TWO = {DB._NAME: 'final_score_two', DB._TYPE: int}
    _FINAL_SCORE_THREE = {DB._NAME: 'final_score_three', DB._TYPE: int}

    # table
    _TABLE_NAME = 'game'

    # parse re patterns
    matchtime_p = r'matchtime: (\d+)'
    match_info_p = r'match_result: \d\n.+ (\d{1,2})\n.+ (\d{1,2})\n.+: (\d+)'

    def __init__(self):
        super().__init__()
        self.map_l = MapL()
        # team 2 CT start, team 3 T start?

    def convert_epoch_time(self, epoch_time):
        return time.strftime(self.timestamp_fmt, time.localtime(epoch_time))

    def ingest_data(self, dirty_data, scode, map_name):
        match_scores = re.search(self.match_info_p, dirty_data)
        epoch_time = int(re.search(self.matchtime_p, dirty_data).group(1))

        self.fields = {
            self._SHARE_CODE[DB._NAME]: self._SHARE_CODE[DB._TYPE](scode),
            self._MATCH_TIME[DB._NAME]: self._MATCH_TIME[DB._TYPE](epoch_time),
            self._MATCH_DURATION[DB._NAME]: self._MATCH_DURATION[DB._TYPE](match_scores.group(3)),
            self._MAP_L_ID[DB._NAME]: self._MAP_L_ID[DB._TYPE](self.map_l.get_map_l_id(map_name)),
            self._FINAL_SCORE_TWO[DB._NAME]: self._FINAL_SCORE_TWO[DB._TYPE](match_scores.group(1)),
            self._FINAL_SCORE_THREE[DB._NAME]: self._FINAL_SCORE_TWO[DB._TYPE](match_scores.group(2))
        }

        return self.insert(self._TABLE_NAME, self.fields, returning=True)[0]
