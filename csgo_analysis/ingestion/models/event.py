from csgo_analysis.ingestion.const import EventTypes
from csgo_analysis.ingestion.models.db import DB


class Event:

    _ID = 'id'
    _GAME_ID = 'game_id'
    _EVENT_NUMBER = 'event_number'
    _ROUND = 'round'

    _TYPES = {}
    _COMP = {}

    def __init__(self):
        self.data_set = []

    # TODO handle weapon-item translation
    # TODO handle item-weapon-item translation (pickup, equip, remove)
    # TODO handle team_l_id: winner in round_end

    def build_event(self, game_id, event_data, event_number, round_count):
        rs = {self._GAME_ID: game_id}
        for dest_col, orig_cal in self._COMP.items():
            rs[dest_col] = self._TYPES[dest_col](event_data[orig_cal])
        rs[self._EVENT_NUMBER] = event_number
        rs[self._ROUND] = round_count
        self.data_set.append(rs)
        return rs

    # tables yet to be completed
    # ! player_death
    # ! player_hurt
    # ! weapon_fire
    # ! item_pickup
    # ! item_equip
    # ! item_remove
    # bomb_planted
    # bomb_defused
    # round_start
    # ? round_end
    # round_mvp


class PlayerBlind(Event, DB):

    # columns
    _ID = 'id'
    _GAME_ID = 'game_id'
    _PLAYER_ID = 'player_id'
    _ATTACKER_ID = 'attacker_id'
    _BLIND_DURATION = 'blind_duration'
    _EVENT_NUMBER = 'event_number'
    _ROUND = 'round'

    _TYPES = {
        _ID: int,
        _GAME_ID: int,
        _PLAYER_ID: int,
        _ATTACKER_ID: int,
        _BLIND_DURATION: float,
        _EVENT_NUMBER: int,
        _ROUND: int
    }

    _COMP = {
        _ATTACKER_ID: 'attacker',
        _PLAYER_ID: 'userid',
        _BLIND_DURATION: 'blind_duration'
    }

    _TABLE_NAME = EventTypes.PLAYER_BLIND

    def __init__(self):
        super().__init__()


class PlayerDeath(Event, DB):

    # columns
    _ID = 'id'
    _GAME_ID = 'game_id'
    _PLAYER_ID = 'player_id'
    _ATTACKER_ID = 'attacker_id'
    _ASSISTER_ID = 'assister_id'
    _ITEM_ID = 'item_id'
    _ASSISTEDFLASH = 'assistedflash'
    _HEADSHOT = 'headshot'
    _DOMINATED = 'dominated'
    _REVENGE = 'revenge'
    _WIPE = 'wipe'
    _PENETRATED = 'penetrated'
    _NOSCOPE = 'noscope'
    _ATTACKERBLIND = 'attackerblind'
    _DISTANCE = 'distance'
    _EVENT_NUMBER = 'event_number'
    _ROUND = 'round'

    _TYPES = {
        _ID: int,
        _GAME_ID: int,
        _PLAYER_ID: int,
        _ATTACKER_ID: int,
        _ASSISTER_ID: int,
        _ITEM_ID: int,
        _ASSISTEDFLASH: DB.custom_bool,
        _HEADSHOT: DB.custom_bool,
        _DOMINATED: DB.custom_bool,
        _REVENGE: DB.custom_bool,
        _WIPE: DB.custom_bool,
        _PENETRATED: DB.custom_bool,
        _NOSCOPE: DB.custom_bool,
        _ATTACKERBLIND: DB.custom_bool,
        _DISTANCE: float,
        _EVENT_NUMBER: int,
        _ROUND: int
    }

    _COMP = {
        _PLAYER_ID: 'userid',
        _ATTACKER_ID: 'attacker',
        _ASSISTER_ID: 'assister',
        _ASSISTEDFLASH: 'assistedflash',
        _ITEM_ID: 'weapon',
        _HEADSHOT: 'headshot',
        _DOMINATED: 'dominated',
        _REVENGE: 'revenge',
        _WIPE: 'wipe',
        _PENETRATED: 'penetrated',
        _NOSCOPE: 'noscope',
        _ATTACKERBLIND: 'attackerblind',
        _DISTANCE: 'distance'
    }

    _TABLE_NAME = EventTypes.PLAYER_DEATH


class PlayerHurt(Event, DB):

    _ID = 'id'
    _GAME_ID = 'game_id'
    _PLAYER_ID = 'player_id'
    _ATTACKER_ID = 'attacker_id'
    _ITEM_ID = 'item_id'
    _HEALTH = 'health'
    _ARMOR = 'armor'
    _DMG_HEALTH = 'dmg_health'
    _DMG_ARMOR = 'dmg_armor'
    _HIT_GROUP = 'hit_group'
    _EVENT_NUMBER = 'event_number'
    _ROUND = 'round'

    _TYPES = {
        _ID: int,
        _GAME_ID: int,
        _PLAYER_ID: int,
        _ATTACKER_ID: int,
        _ITEM_ID: int,
        _HEALTH: int,
        _ARMOR: int,
        _DMG_HEALTH: int,
        _DMG_ARMOR: int,
        _HIT_GROUP: int,
        _EVENT_NUMBER: int,
        _ROUND: int
    }

    _COMP = {
        _PLAYER_ID: 'userid',
        _ATTACKER_ID: 'attacker',
        _ITEM_ID: 'weapon',
        _HEALTH: 'health',
        _ARMOR: 'armor',
        _DMG_HEALTH: 'dmg_health',
        _DMG_ARMOR: 'dmg_armor',
        _HIT_GROUP: 'hitgroup'
    }

    _TABLE_NAME = EventTypes.PLAYER_HURT


class PlayerFallDamage(Event, DB):

    _ID = 'id'
    _GAME_ID = 'game_id'
    _PLAYER_ID = 'player_id'
    _DAMAGE = 'damage'
    _EVENT_NUMBER = 'event_number'
    _ROUND = 'round'

    _TYPES = {
        _ID: int,
        _GAME_ID: int,
        _PLAYER_ID: int,
        _DAMAGE: float,
        _EVENT_NUMBER: int,
        _ROUND: int
    }

    _COMP = {
        _PLAYER_ID: 'userid',
        _DAMAGE: 'damage'
    }

    _TABLE_NAME = EventTypes.PLAYER_FALLDAMAGE


class WeaponFire(Event, DB):

    _ID = 'id'
    _GAME_ID = 'game_id'
    _PLAYER_ID = 'player_id'
    _ITEM_ID = 'item_id'
    _SILENCED = 'silenced'
    _EVENT_NUMBER = 'event_number'
    _ROUND = 'round'

    _TYPES = {
        _ID: int,
        _GAME_ID: int,
        _PLAYER_ID: int,
        _ITEM_ID: int,
        _SILENCED: DB.custom_bool,
        _EVENT_NUMBER: int,
        _ROUND: int
    }

    _COMP = {
        _PLAYER_ID: 'userid',
        _ITEM_ID: 'weapon',
        _SILENCED: 'silenced'
    }

    _TABLE_NAME = EventTypes.WEAPON_FIRE


class ItemEquip(Event):

    _ID = 'id'
    _GAME_ID = 'game_id'
    _PLAYER_ID = 'player_id'
    _ITEM_ID = 'item_id'
    _EVENT_NUMBER = 'event_number'
    _ROUND = 'round'

    _TYPES = {
        _ID: int,
        _GAME_ID: int,
        _PLAYER_ID: int,
        _ITEM_ID: int,
        _EVENT_NUMBER: int,
        _ROUND: int
    }

    _COMP = {
        _PLAYER_ID: 'userid',
        _ITEM_ID: 'item',
    }

    _TABLE_NAME = EventTypes.ITEM_EQUIP


class BombPlanted(Event):

    _ID = 'id'
    _GAME_ID = 'game_id'
    _PLAYER_ID = 'player_id'
    _SITE = 'site'
    _EVENT_NUMBER = 'event_number'
    _ROUND = 'round'

    _TYPES = {
        _ID: int,
        _GAME_ID: int,
        _PLAYER_ID: int,
        _SITE: int,
        _EVENT_NUMBER: int,
        _ROUND: int
    }

    _COMP = {
        _PLAYER_ID: 'userid',
        _SITE: 'site'
    }

    _TABLE_NAME = EventTypes.BOMB_PLANTED


class BombDefused(Event):

    _ID = 'id'
    _GAME_ID = 'game_id'
    _PLAYER_ID = 'player_id'
    _SITE = 'site'
    _EVENT_NUMBER = 'event_number'
    _ROUND = 'round'

    _TYPES = {
        _ID: int,
        _GAME_ID: int,
        _PLAYER_ID: int,
        _SITE: int,
        _EVENT_NUMBER: int,
        _ROUND: int
    }

    _COMP = {
        _PLAYER_ID: 'userid',
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


class RoundMVP(Event):

    _ID = 'id'
    _GAME_ID = 'game_id'
    _PLAYER_ID = 'player_id'
    _REASON = 'reason'
    _EVENT_NUMBER = 'event_number'
    _ROUND = 'round'

    _TYPES = {
        _ID: int,
        _GAME_ID: int,
        _PLAYER_ID: int,
        _REASON: int,
        _EVENT_NUMBER: int,
        _ROUND: int
    }

    _COMP = {
        _PLAYER_ID: 'userid',
        _REASON: 'reason',
    }

    _TABLE_NAME = EventTypes.ROUND_MVP
