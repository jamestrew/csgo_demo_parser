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

    _ID = DB._ID
    _GAME_ID = DB._GAME_ID
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

    _ID = DB._ID
    _GAME_ID = DB._GAME_ID
    _PLAYER_ID = DB._PLAYER_ID
    _TEAM_L_ID = DB._TEAM_L_ID
    _ATTACKER_ID = DB._ATTACKER_ID
    _ITEM_ID = DB._ITEM_ID
    _HEALTH = Field('health', int, 'health')
    _ARMOR = Field('armor', int, 'armor')
    _DMG_HEALTH = Field('dmg_health', int, 'dmg_health')
    _DMG_ARMOR = Field('dmg_armor', int, 'dmg_armor')
    _HITGROUP = Field('hitgroup', int, 'hitgroup')
    _EVENT_NUMBER = DB._EVENT_NUMBER
    _ROUND = DB._ROUND

    _TABLE_NAME = EventTypes.PLAYER_HURT

    def build_rs(self, event_data):
        self.rs = {
            self._PLAYER_ID: event_data[self._PLAYER_ID.ref],
            self._TEAM_L_ID: Team.get_team_id(event_data[self._TEAM_L_ID.ref]),
            self._ATTACKER_ID: event_data[self._ATTACKER_ID.ref],
            self._ITEM_ID: event_data[self._ITEM_ID.ref],
            self._HEALTH: event_data[self._HEALTH.ref],
            self._ARMOR: event_data[self._ARMOR.ref],
            self._DMG_ARMOR: event_data[self._DMG_ARMOR.ref],
            self._DMG_HEALTH: event_data[self._DMG_HEALTH.ref],
            self._HITGROUP: event_data[self._HITGROUP.ref],
        }


class PlayerFallDamage(Event, DB):

    _ID = DB._ID
    _GAME_ID = DB._GAME_ID
    _PLAYER_ID = DB._PLAYER_ID
    _TEAM_L_ID = DB._TEAM_L_ID
    _DAMAGE = Field('damage', float, 'damage')
    _EVENT_NUMBER = DB._EVENT_NUMBER
    _ROUND = DB._ROUND

    _TABLE_NAME = EventTypes.PLAYER_FALLDAMAGE

    def build_rs(self, event_data):
        self.rs = {
            self._PLAYER_ID: event_data[self._PLAYER_ID.ref],
            self._TEAM_L_ID: Team.get_team_id(event_data[self._TEAM_L_ID.ref]),
            self._DAMAGE: event_data[self._DAMAGE.ref],
        }


class WeaponFire(Event, DB):

    _ID = DB._ID
    _GAME_ID = DB._GAME_ID
    _PLAYER_ID = DB._PLAYER_ID
    _TEAM_L_ID = DB._TEAM_L_ID
    _ITEM_ID = DB._ITEM_ID
    _SILENCED = Field('silenced', DB.custom_bool, 'silenced')
    _EVENT_NUMBER = DB._EVENT_NUMBER
    _ROUND = DB._ROUND

    _TABLE_NAME = EventTypes.WEAPON_FIRE

    def build_rs(self, event_data):
        self.rs = {
            self._PLAYER_ID: event_data[self._PLAYER_ID.ref],
            self._TEAM_L_ID: Team.get_team_id(event_data[self._TEAM_L_ID.ref]),
            self._ITEM_ID: event_data[self._ITEM_ID.ref],
            self._SILENCED: event_data[self._SILENCED.ref],
        }


class ItemEquip(Event):

    _ID = DB._ID
    _GAME_ID = DB._GAME_ID
    _PLAYER_ID = DB._PLAYER_ID
    _TEAM_L_ID = DB._TEAM_L_ID
    _ITEM_ID = DB._ITEM_ID
    _EVENT_NUMBER = DB._EVENT_NUMBER
    _ROUND = DB._ROUND

    _TABLE_NAME = EventTypes.ITEM_EQUIP

    def build_rs(self, event_data):
        self.rs = {
            self._PLAYER_ID: event_data[self._PLAYER_ID.ref],
            self._TEAM_L_ID: Team.get_team_id(event_data[self._TEAM_L_ID.ref]),
            self._ITEM_ID: event_data[self._ITEM_ID.ref],
        }

    def build_event(self, game_id, event_data, event_number, round_count):
        if event_data[self._TEAM_L_ID.ref] is None:
            return False
        return super().build_event(game_id, event_data, event_number, round_count)


class BombPlanted(Event):

    _ID = DB._ID
    _GAME_ID = DB._GAME_ID
    _PLAYER_ID = DB._PLAYER_ID
    _TEAM_L_ID = DB._TEAM_L_ID
    _SITE = 'site'
    _EVENT_NUMBER = DB._EVENT_NUMBER
    _ROUND = DB._ROUND

    _TABLE_NAME = EventTypes.BOMB_PLANTED


class BombDefused(Event):

    _ID = DB._ID
    _GAME_ID = DB._GAME_ID
    _PLAYER_ID = DB._PLAYER_ID
    _TEAM_L_ID = DB._TEAM_L_ID
    _SITE = 'site'
    _EVENT_NUMBER = DB._EVENT_NUMBER
    _ROUND = DB._ROUND

    _TABLE_NAME = EventTypes.BOMB_DEFUSED


class RoundStart(Event):

    _ID = DB._ID
    _GAME_ID = DB._GAME_ID
    _TIMELIMIT = 'timelimit'
    _EVENT_NUMBER = DB._EVENT_NUMBER
    _ROUND = DB._ROUND

    _TABLE_NAME = EventTypes.ROUND_START


class RoundEnd(Event):

    _ID = DB._ID
    _GAME_ID = DB._GAME_ID
    _TEAM_L_ID = DB._TEAM_L_ID
    _REASON = 'reason'
    _MESSAGE = 'message'
    _EVENT_NUMBER = DB._EVENT_NUMBER
    _ROUND = DB._ROUND

    _TABLE_NAME = EventTypes.ROUND_END

    def build_event(self, game_id, event_data, event_number, round_count):
        team_num = event_data[self._COMP[self._TEAM_L_ID]]
        team_id = self.TEAM_L[int(team_num)].value
        event_data[self._COMP[self._TEAM_L_ID]] = team_id
        return super().build_event(game_id, event_data, event_number, round_count)


class RoundMVP(Event):

    _ID = DB._ID
    _GAME_ID = DB._GAME_ID
    _PLAYER_ID = DB._PLAYER_ID
    _TEAM_L_ID = DB._TEAM_L_ID
    _REASON = 'reason'
    _EVENT_NUMBER = DB._EVENT_NUMBER
    _ROUND = DB._ROUND

    _TABLE_NAME = EventTypes.ROUND_MVP
