import re
from datetime import datetime

from csgo_analysis.ingestion.db.dbconn import DBConn
from csgo_analysis.ingestion.models.db import DB, Field
from csgo_analysis.ingestion.models.map import Map


class Game(DBConn, DB):

    # column names
    _ID = DB._ID
    _SHARE_CODE = Field('share_code', str, None)
    _MATCH_TIME = Field('match_time', datetime.fromtimestamp, None)
    _MATCH_DURATION = Field('match_duration', int, None)
    _MAP_L_ID = Field('map_l_id', int, None)

    # table
    _TABLE_NAME = 'game'

    # parse re patterns
    matchtime_p = r'matchtime: (\d+)'
    match_info_p = r'match_result: \d\n.+ (\d{1,2})\n.+ (\d{1,2})\n.+: (\d+)'

    def __init__(self):
        super().__init__()
        self.recordset = {}

    def ingest_data(self, dirty_data, scode, map_name):
        match_scores = re.search(self.match_info_p, dirty_data)
        epoch_time = int(re.search(self.matchtime_p, dirty_data).group(1))

        rs = {
            self._SHARE_CODE: scode,
            self._MATCH_TIME: epoch_time,
            self._MATCH_DURATION: match_scores.group(3),
            self._MAP_L_ID: Map.get_map_id(map_name),
        }

        self.recordset = self.cast_data(rs)

        return self.insert(self._TABLE_NAME, self.recordset, returning=True)
