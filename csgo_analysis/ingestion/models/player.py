from csgo_analysis.ingestion.models.db import DB
from csgo_analysis.ingestion.models.dbconn import DBConn
from csgo_analysis.ingestion.const import EventTypes
from enum import Enum


class Team(Enum):
    TEAM_TWO = 1  # CT first
    TEAM_THREE = 2  # T first


class Player(DBConn):

    # columns
    _ID = {DB._NAME: 'id', DB._TYPE: int}
    _GAME_ID = {DB._NAME: 'game_id', DB._TYPE: int}
    _TEAM_L_ID = {DB._NAME: 'team_l_id', DB._TYPE: int}
    _XUID = {DB._NAME: 'xuid', DB._TYPE: int}  # steam64 id
    _NAME = {DB._NAME: 'name', DB._TYPE: str}

    # table
    _TABLE_NAME = 'player'

    # supp data
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
                player = {
                    self._GAME_ID[DB._NAME]: self.game_id,
                    self._XUID[DB._NAME]: int(player_info[self._XUID[DB._NAME]]),
                    self._NAME[DB._NAME]: player_info[self._NAME[DB._NAME]],
                    self._USER_ID: int(player_info[self._USER_ID]),
                    self._TEAM_L_ID[DB._NAME]: None
                }

                self.players[self.get_full_id(player)] = player

            if self._SPAWN == event_name:
                spawn_info = event[self._SPAWN]
                if int(spawn_info[self._TEAM_NUM]) == 0 or \
                        spawn_info[self._FULL_ID] not in self.players:
                    continue

                team_id = self.TEAM_L.get(int(spawn_info[self._TEAM_NUM])).value
                self.players[spawn_info[self._FULL_ID]][self._TEAM_L_ID[DB._NAME]] = team_id

            if event_name in EventTypes.PLAYER_EVENTS:
                player = event[event_name][self._FULL_ID].strip()
                attacker = event[event_name].get(self._ATTACKER)
                assister = event[event_name].get(self._ASSISTER)

                if (player_xuid := self.get_player_xuid(player)):
                    event[event_name][self._FULL_ID] = player_xuid

                if attacker is not None:
                    attacker = attacker.strip()
                    if (attacker_xuid := self.get_player_xuid(attacker)):
                        event[event_name][self._ATTACKER] = attacker_xuid
                if assister is not None:
                    assister = assister.strip()
                    if (assister_xuid := self.get_player_xuid(assister)):
                        event[event_name][self._ASSISTER] = assister_xuid

        self.insert_prep()
        return self.data

    def get_full_id(self, player):
        ''' Return userid in the original format
            eg. "userid": "Chris P. Bacon (id:3)"
        '''
        return f'{player.get(self._NAME[DB._NAME])} (id:{player.get(self._USER_ID)})'

    def insert_prep(self):
        ''' Create list of unqiue player data and call insert to insert player data
            into db.
        '''
        fields = []
        xuids = []
        for player in self.players.values():
            player.pop(self._USER_ID)
            if player[self._XUID[DB._NAME]] not in xuids:
                xuids.append(player[self._XUID[DB._NAME]])
                fields.append(player)

        self.insert(self._TABLE_NAME, fields, True)

    def get_player_xuid(self, player):
        try:
            return self.players[player][self._XUID[DB._NAME]]
        except KeyError:
            return None
