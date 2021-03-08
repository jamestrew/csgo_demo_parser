from csgo_analysis.ingestion.models.db import DB
from csgo_analysis.ingestion.models.dbconn import DBConn
from csgo_analysis.ingestion.const import EventTypes
from enum import Enum


class Team(Enum):
    TEAM_TWO = 1
    TEAM_THREE = 2
    TEAM_UNKNOWN = 999


class Player(DBConn, DB):

    _ID = 'id'
    _GAME_ID = 'game_id'
    _TEAM_L_ID = 'team_l_id'
    _XUID = 'xuid'
    _PLAYER_NAME = 'player_name'

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

    TEAM_L = {
        2: Team.TEAM_TWO,
        3: Team.TEAM_THREE
    }

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
            if self._INFO == event_name and event[self._INFO]['guid'] != 'BOT':
                player_info = event[self._INFO]
                data = {
                    self._GAME_ID: self.game_id,
                    self._XUID: player_info[self._XUID],
                    self._PLAYER_NAME: player_info[self._NAME],
                    self._TEAM_L_ID: Team.TEAM_UNKNOWN.value
                }

                userid = int(player_info[self._USER_ID])
                self.players[self.get_full_id(data, userid)] = self.cast_data(data)

            if self._SPAWN == event_name:
                spawn_info = event[self._SPAWN]
                if int(spawn_info[self._TEAM_NUM]) == 0 or \
                        spawn_info[self._FULL_ID] not in self.players:
                    continue

                team_id = self.TEAM_L.get(int(spawn_info[self._TEAM_NUM])).value
                self.players[spawn_info[self._FULL_ID]][self._TEAM_L_ID] = team_id

            self.insert_prep()

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

        self.cleanup()
        return self.data

    def get_full_id(self, data, userid):
        ''' Return userid in the original format
            eg. "userid": "Chris P. Bacon (id:3)"
        '''
        return f'{data.get(self._PLAYER_NAME)} (id:{userid})'

    def insert_prep(self):
        ''' Insert each unqiue player into db and create userid - playerid pair. '''

        for player_userid in self.players.keys():
            row = self.players[player_userid]
            if row[self._TEAM_L_ID] != Team.TEAM_UNKNOWN and \
                    row[self._XUID] not in self.xuid_id_dict:
                id = self.insert(self._TABLE_NAME, row, True)
                self.xuid_id_dict[row[self._XUID]] = id
            self.userid_id_dict[player_userid] = self.xuid_id_dict[row[self._XUID]]

    def get_player_xuid(self, player):
        try:
            return self.players[player][self._XUID]
        except KeyError:
            return None

    def cleanup(self):
        clean_data = []
        for event in self.data:
            event_name = list(event.keys())[0]
            if event_name not in EventTypes.PLAYER_CLEANUP:
                clean_data.append(event)

        self.data = clean_data
