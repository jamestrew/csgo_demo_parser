from csgo_analysis.ingestion.models.db import DB
from csgo_analysis.ingestion.const import Events
from enum import Enum


class Team(Enum):
    TEAM_TWO = 2  # CT first
    TEAM_THREE = 3  # T first


class Player(DB):

    # columns
    _ID = 'id'
    _GAME_ID = 'game_id'
    _TEAM_L_ID = 'team_l_id'
    _XUID = 'xuid'  # steam64 id
    _NAME = 'name'

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
        for event in self.data:
            event_name = list(event.keys())[0]
            if self._INFO == event_name and event[self._INFO]['guid'] != 'BOT':
                player_info = event[self._INFO]
                player = {
                    self._GAME_ID: self.game_id,
                    self._XUID: int(player_info[self._XUID]),
                    self._NAME: player_info[self._NAME],
                    self._USER_ID: int(player_info[self._USER_ID]),
                    self._TEAM_L_ID: None
                }

                self.players[self.get_full_id(player)] = player

            if self._SPAWN == event_name:
                spawn_info = event[self._SPAWN]
                if int(spawn_info[self._TEAM_NUM]) == 0:
                    continue

                team_id = self.TEAM_L.get(int(spawn_info[self._TEAM_NUM])).value
                self.players[spawn_info[self._FULL_ID]][self._TEAM_L_ID] = team_id

            if event_name in Events.PLAYER_EVENTS:
                player = event[event_name][self._FULL_ID].strip()
                attacker = event[event_name].get(self._ATTACKER)
                assister = event[event_name].get(self._ASSISTER)
                event[event_name][self._FULL_ID] = self.players[player][self._XUID]

                if attacker is not None:
                    attacker = attacker.strip()
                    event[event_name][self._ATTACKER] = self.players[attacker][self._XUID]
                if assister is not None:
                    assister = assister.strip()
                    try:
                        event[event_name][self._ASSISTER] = self.players[assister][self._XUID]
                    except KeyError:
                        continue

    def get_full_id(self, player):
        ''' Return userid in the original format
            eg. "userid": "Chris P. Bacon (id:3)"
        '''
        return f'{player.get(self._NAME)} (id:{player.get(self._USER_ID)})'

    # TODO able to take [Player name (id : id)] and return
