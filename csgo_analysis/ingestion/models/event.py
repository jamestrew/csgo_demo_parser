from csgo_analysis.ingestion.const import EventTypes
from csgo_analysis.ingestion.models.db import DB


class Event:

    def build_event(self, game_id, event_data, event_numer, round_count):
        pass


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

    _TABLE_NAME = EventTypes.PLAYER_BLIND


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

    _TABLE_NAME = EventTypes.PLAYER_DEATH


class PlayerHurt(Event, DB):

    _ID = 'id'
    _GAME_ID = 'game_id'
    _PLAYER_ID = 'player_id'
    _ATTACKER_ID = 'attacker_id'
    _ASSISTER_ID = 'assister_id'
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
        _ASSISTER_ID: int,
        _ITEM_ID: int,
        _HEALTH: int,
        _ARMOR: int,
        _DMG_HEALTH: int,
        _DMG_ARMOR: int,
        _HIT_GROUP: int,
        _EVENT_NUMBER: int,
        _ROUND: int
    }


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


class ItemPickup(Event):

    _ID = 'id'
    _GAME_ID = 'game_id'
    _PLAYER_ID = 'player_id'
    _ITEM_ID = 'item_id'
    _SILENT = 'silent'
    _EVENT_NUMBER = 'event_number'
    _ROUND = 'round'

    _TYPES = {
        _ID: int,
        _GAME_ID: int,
        _PLAYER_ID: int,
        _ITEM_ID: int,
        _SILENT: DB.custom_bool,
        _EVENT_NUMBER: int,
        _ROUND: int
    }


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


class ItemRemove(Event):

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
