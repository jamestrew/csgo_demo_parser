import json

from csgo_analysis.ingestion.const import EventTypes
from csgo_analysis.ingestion.models.db import DB, Field
from csgo_analysis.ingestion.db.dbconn import DBConn
from csgo_analysis.ingestion.models.team import Team


class Event(DBConn, DB):

    def __init__(self):
        super().__init__()
        self.data_set = []
        self.rs = {}

    def build_rs(self, event_data):
        pass

    def build_event(self, game_id, event_data, event_number, round_count):
        self.build_rs(event_data)
        self.rs[self._GAME_ID] = game_id
        self.rs[self._EVENT_NUMBER] = event_number
        self.rs[self._ROUND] = round_count

        rs = self.cast_data(self.rs)
        self.data_set.append(rs)
        return rs


class EventJson(DBConn):

    _ID = 'id'
    _GAME_ID = 'game_id'
    _DATA = 'data'

    _TABLE_NAME = 'event_json'

    def insert_prep(self, game_id, data):
        rs = {
            self._GAME_ID: game_id,
            self._DATA: json.dumps(data)
        }
        self.insert(self._TABLE_NAME, rs)


class PlayerBlind(Event, DB):

    # columns
    _ID = DB._ID
    _GAME_ID = DB._GAME_ID
    _PLAYER_ID = DB._PLAYER_ID
    _TEAM_L_ID = DB._TEAM_L_ID
    _ATTACKER_ID = DB._ATTACKER_ID
    _BLIND_DURATION = Field('blind_duration', float, 'blind_duration')
    _EVENT_NUMBER = DB._EVENT_NUMBER
    _ROUND = DB._ROUND

    _TABLE_NAME = EventTypes.PLAYER_BLIND

    def __init__(self):
        super().__init__()

    def build_rs(self, event_data):
        self.rs = {
            self._PLAYER_ID: event_data[self._PLAYER_ID.ref],
            self._TEAM_L_ID: Team.get_team_id(event_data[self._TEAM_L_ID.ref]),
            self._ATTACKER_ID: event_data[self._ATTACKER_ID.ref],
            self._BLIND_DURATION: event_data[self._BLIND_DURATION.ref]
        }


class PlayerDeath(Event, DB):

    # columns
    _ID = DB._ID
    _GAME_ID = DB._GAME_ID
    _PLAYER_ID = DB._PLAYER_ID
    _TEAM_L_ID = DB._TEAM_L_ID
    _PLAYER_ITEM_ID = Field('player_item_id', int, 'player_item_id')
    _ATTACKER_ID = DB._ATTACKER_ID
    _ASSISTER_ID = Field('assister_id', int, 'assister', True)
    _ITEM_ID = DB._ITEM_ID
    _ASSISTEDFLASH = Field('assistedflash', DB.custom_bool, 'assistedflash')
    _HEADSHOT = Field('headshot', DB.custom_bool, 'headshot')
    _DOMINATED = Field('dominated', DB.custom_bool, 'dominated')
    _REVENGE = Field('revenge', DB.custom_bool, 'revenge')
    _WIPE = Field('wipe', DB.custom_bool, 'wipe')
    _THRUSMOKE = Field('thrusmoke', DB.custom_bool, 'thrusmoke')
    _PENETRATED = Field('penetrated', DB.custom_bool, 'penetrated')
    _NOSCOPE = Field('noscope', DB.custom_bool, 'noscope')
    _ATTACKERBLIND = Field('attackerblind', DB.custom_bool, 'attackerblind')
    _DISTANCE = Field('distance', float, 'distance', True)
    _EVENT_NUMBER = DB._EVENT_NUMBER
    _ROUND = DB._ROUND

    _TABLE_NAME = EventTypes.PLAYER_DEATH

    def build_rs(self, event_data):
        self.rs = {
            self._PLAYER_ID: event_data[self._PLAYER_ID.ref],
            self._TEAM_L_ID: Team.get_team_id(event_data[self._TEAM_L_ID.ref]),
            self._PLAYER_ITEM_ID: event_data[self._PLAYER_ITEM_ID.ref],
            self._ATTACKER_ID: event_data[self._ATTACKER_ID.ref],
            self._ASSISTER_ID: event_data[self._ASSISTER_ID.ref],
            self._ITEM_ID: event_data[self._ITEM_ID.ref],
            self._ASSISTEDFLASH: event_data[self._ASSISTEDFLASH.ref],
            self._HEADSHOT: event_data[self._HEADSHOT.ref],
            self._DOMINATED: event_data[self._DOMINATED.ref],
            self._REVENGE: event_data[self._REVENGE.ref],
            self._WIPE: event_data[self._WIPE.ref],
            self._PENETRATED: event_data[self._PENETRATED.ref],
            self._NOSCOPE: event_data[self._NOSCOPE.ref],
            self._THRUSMOKE: event_data[self._THRUSMOKE.ref],
            self._ATTACKERBLIND: event_data[self._ATTACKERBLIND.ref],
            self._DISTANCE: event_data[self._DISTANCE.ref],
        }


class PlayerHurt(Event, DB):

    _ID = 'id'
    _GAME_ID = 'game_id'
    _PLAYER_ID = 'player_id'
    _TEAM = 'team'
    _ATTACKER_ID = 'attacker_id'
    _ITEM_ID = 'item_id'
    _HEALTH = 'health'
    _ARMOR = 'armor'
    _DMG_HEALTH = 'dmg_health'
    _DMG_ARMOR = 'dmg_armor'
    _HITGROUP = 'hitgroup'
    _EVENT_NUMBER = 'event_number'
    _ROUND = 'round'

    _TYPES = {
        _ID: int,
        _GAME_ID: int,
        _PLAYER_ID: int,
        _TEAM: str,
        _ATTACKER_ID: int,
        _ITEM_ID: int,
        _HEALTH: int,
        _ARMOR: int,
        _DMG_HEALTH: int,
        _DMG_ARMOR: int,
        _HITGROUP: int,
        _EVENT_NUMBER: int,
        _ROUND: int
    }

    _COMP = {
        _PLAYER_ID: 'userid',
        _TEAM: 'team',
        _ATTACKER_ID: 'attacker',
        _ITEM_ID: 'item_id',
        _HEALTH: 'health',
        _ARMOR: 'armor',
        _DMG_HEALTH: 'dmg_health',
        _DMG_ARMOR: 'dmg_armor',
        _HITGROUP: 'hitgroup'
    }

    _TABLE_NAME = EventTypes.PLAYER_HURT


class PlayerFallDamage(Event, DB):

    _ID = 'id'
    _GAME_ID = 'game_id'
    _PLAYER_ID = 'player_id'
    _TEAM = 'team'
    _DAMAGE = 'damage'
    _EVENT_NUMBER = 'event_number'
    _ROUND = 'round'

    _TYPES = {
        _ID: int,
        _GAME_ID: int,
        _PLAYER_ID: int,
        _TEAM: str,
        _DAMAGE: float,
        _EVENT_NUMBER: int,
        _ROUND: int
    }

    _COMP = {
        _PLAYER_ID: 'userid',
        _TEAM: 'team',
        _DAMAGE: 'damage'
    }

    _TABLE_NAME = EventTypes.PLAYER_FALLDAMAGE


class WeaponFire(Event, DB):

    _ID = 'id'
    _GAME_ID = 'game_id'
    _PLAYER_ID = 'player_id'
    _TEAM = 'team'
    _ITEM_ID = 'item_id'
    _SILENCED = 'silenced'
    _EVENT_NUMBER = 'event_number'
    _ROUND = 'round'

    _TYPES = {
        _ID: int,
        _GAME_ID: int,
        _PLAYER_ID: int,
        _TEAM: str,
        _ITEM_ID: int,
        _SILENCED: DB.custom_bool,
        _EVENT_NUMBER: int,
        _ROUND: int
    }

    _COMP = {
        _PLAYER_ID: 'userid',
        _TEAM: 'team',
        _ITEM_ID: 'item_id',
        _SILENCED: 'silenced'
    }

    _TABLE_NAME = EventTypes.WEAPON_FIRE


class ItemEquip(Event):

    _ID = 'id'
    _GAME_ID = 'game_id'
    _PLAYER_ID = 'player_id'
    _TEAM = 'team'
    _ITEM_ID = 'item_id'
    _EVENT_NUMBER = 'event_number'
    _ROUND = 'round'

    _TYPES = {
        _ID: int,
        _GAME_ID: int,
        _PLAYER_ID: int,
        _TEAM: str,
        _ITEM_ID: int,
        _EVENT_NUMBER: int,
        _ROUND: int
    }

    _COMP = {
        _PLAYER_ID: 'userid',
        _TEAM: 'team',
        _ITEM_ID: 'item_id',
    }

    _TABLE_NAME = EventTypes.ITEM_EQUIP

    def build_event(self, game_id, event_data, event_number, round_count):
        if event_data.get(self._COMP[self._TEAM]) is None:
            return False
        return super().build_event(game_id, event_data, event_number, round_count)


class BombPlanted(Event):

    _ID = 'id'
    _GAME_ID = 'game_id'
    _PLAYER_ID = 'player_id'
    _TEAM = 'team'
    _SITE = 'site'
    _EVENT_NUMBER = 'event_number'
    _ROUND = 'round'

    _TYPES = {
        _ID: int,
        _GAME_ID: int,
        _PLAYER_ID: int,
        _TEAM: str,
        _SITE: int,
        _EVENT_NUMBER: int,
        _ROUND: int
    }

    _COMP = {
        _PLAYER_ID: 'userid',
        _TEAM: 'team',
        _SITE: 'site'
    }

    _TABLE_NAME = EventTypes.BOMB_PLANTED


class BombDefused(Event):

    _ID = 'id'
    _GAME_ID = 'game_id'
    _PLAYER_ID = 'player_id'
    _TEAM = 'team'
    _SITE = 'site'
    _EVENT_NUMBER = 'event_number'
    _ROUND = 'round'

    _TYPES = {
        _ID: int,
        _GAME_ID: int,
        _PLAYER_ID: int,
        _TEAM: str,
        _SITE: int,
        _EVENT_NUMBER: int,
        _ROUND: int
    }

    _COMP = {
        _PLAYER_ID: 'userid',
        _TEAM: 'team',
        _SITE: 'site'
    }

    _TABLE_NAME = EventTypes.BOMB_DEFUSED


class RoundStart(Event):

    _ID = 'id'
    _GAME_ID = 'game_id'
    _TIMELIMIT = 'timelimit'
    _EVENT_NUMBER = 'event_number'
    _ROUND = 'round'

    _TYPES = {
        _ID: int,
        _GAME_ID: int,
        _TIMELIMIT: int,
        _EVENT_NUMBER: int,
        _ROUND: int
    }

    _COMP = {
        _TIMELIMIT: 'timelimit'
    }

    _TABLE_NAME = EventTypes.ROUND_START


class RoundEnd(Event):

    _ID = 'id'
    _GAME_ID = 'game_id'
    _TEAM_L_ID = 'team_l_id'
    _REASON = 'reason'
    _MESSAGE = 'message'
    _EVENT_NUMBER = 'event_number'
    _ROUND = 'round'

    _TYPES = {
        _ID: int,
        _GAME_ID: int,
        _TEAM_L_ID: int,
        _REASON: int,
        _MESSAGE: str,
        _EVENT_NUMBER: int,
        _ROUND: int
    }

    _COMP = {
        _TEAM_L_ID: 'winner',
        _REASON: 'reason',
        _MESSAGE: 'message'
    }

    _TABLE_NAME = EventTypes.ROUND_END

    def build_event(self, game_id, event_data, event_number, round_count):
        team_num = event_data[self._COMP[self._TEAM_L_ID]]
        team_id = self.TEAM_L[int(team_num)].value
        event_data[self._COMP[self._TEAM_L_ID]] = team_id
        return super().build_event(game_id, event_data, event_number, round_count)


class RoundMVP(Event):

    _ID = 'id'
    _GAME_ID = 'game_id'
    _PLAYER_ID = 'player_id'
    _TEAM = 'team'
    _REASON = 'reason'
    _EVENT_NUMBER = 'event_number'
    _ROUND = 'round'

    _TYPES = {
        _ID: int,
        _GAME_ID: int,
        _PLAYER_ID: int,
        _TEAM: str,
        _REASON: int,
        _EVENT_NUMBER: int,
        _ROUND: int
    }

    _COMP = {
        _PLAYER_ID: 'userid',
        _TEAM: 'team',
        _REASON: 'reason',
    }

    _TABLE_NAME = EventTypes.ROUND_MVP
