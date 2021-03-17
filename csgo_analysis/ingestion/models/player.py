from csgo_analysis.ingestion.const import EventTypes
from csgo_analysis.ingestion.models.db import DB, Field
from csgo_analysis.ingestion.db.dbconn import DBConn
from csgo_analysis.ingestion.models.team import Team


class Player(DBConn, DB):

    # columns
    _ID = DB._ID
    _GAME_ID = DB._GAME_ID
    _TEAM_L_ID = DB._TEAM_L_ID  # _FIRST_TEAM_L_ID = 'first_team_l_id'
    _XUID = Field('xuid', int, None)  # int -> str
    _PLAYER_NAME = Field('player_name', str, None)

    _TYPES = {
        _ID: int,
        _GAME_ID: int,
        _TEAM_L_ID: int,
        _XUID: int,
        _PLAYER_NAME: str
    }

    # table
    _TABLE_NAME = 'player'

    # supp data
    _NAME = 'name'
    _USER_ID = 'userID'
    _TEAM_NUM = 'teamnum'
    _FULL_ID = 'userid'
    _ATTACKER = 'attacker'
    _ASSISTER = 'assister'
    _INFO = 'player_info'
    _SPAWN = 'player_spawn'

    def __init__(self, game_id, data):
        super().__init__()
        self.players = {}
        self.userid_id_dict = {}
        self.xuid_id_dict = {}
        self.game_id = game_id
        self.data = data

    def create_players(self):
        """Ingest player data into db, replace all userid values in json data with player xuid.

        Returns
        -------
        list
            game data object
        """

        for event in self.data:
            event_name = list(event.keys())[0]
            if EventTypes.PLAYER_INFO == event_name and \
                    event[EventTypes.PLAYER_INFO]['guid'] != 'BOT':
                player_info = event[EventTypes.PLAYER_INFO]
                data = {
                    self._GAME_ID: self.game_id,
                    self._XUID: player_info[self._XUID.col_name],
                    self._PLAYER_NAME: player_info[self._NAME],
                    self._TEAM_L_ID: Team.GOTV
                }

                userid = int(player_info[self._USER_ID])
                self.players[self._get_full_id(data, userid)] = self.cast_data(data)

            if EventTypes.PLAYER_SPAWN == event_name:
                spawn_info = event[EventTypes.PLAYER_SPAWN]
                if int(spawn_info[self._TEAM_NUM]) == 0 or \
                        spawn_info[self._FULL_ID] not in self.players:
                    continue

                team_id = int(spawn_info[self._TEAM_NUM])
                self.players[spawn_info[self._FULL_ID]][self._TEAM_L_ID] = team_id

            self._insert_prep()

            if event_name in EventTypes.PLAYER_EVENTS:
                event_data = event[event_name]
                player = event_data[self._FULL_ID].strip()
                attacker = event_data.get(self._ATTACKER)
                assister = event_data.get(self._ASSISTER)

                event_data[self._FULL_ID] = self.userid_id_dict.get(player)

                if attacker is not None:
                    attacker = attacker.strip()
                    event_data[self._ATTACKER] = self.userid_id_dict.get(attacker)
                if assister is not None:
                    assister = assister.strip()
                    event_data[self._ASSISTER] = self.userid_id_dict.get(assister)

        self._cleanup()
        return self.data

    def _get_full_id(self, data, userid):
        ''' Return userid in the original format
            eg. "userid": "Chris P. Bacon (id:3)"
        '''
        return f'{data.get(self._PLAYER_NAME)} (id:{userid})'

    def _insert_prep(self):
        ''' Insert each unqiue player into db and create userid - playerid pair. '''

        for player_userid in self.players.keys():
            row = self.players[player_userid]
            if row[self._TEAM_L_ID] != Team.GOTV and \
                    row[self._XUID] not in self.xuid_id_dict:
                id = self.insert(self._TABLE_NAME, row, True)
                self.xuid_id_dict[row[self._XUID]] = id
            self.userid_id_dict[player_userid] = self.xuid_id_dict.get(row[self._XUID])

    def _cleanup(self):
        clean_data = []
        for event in self.data:
            event_name = list(event.keys())[0]
            if event_name not in EventTypes.PLAYER_CLEANUP:
                clean_data.append(event)

        self.data = clean_data

    @property
    def player_list(self):
        return list(self.xuid_id_dict.values())
