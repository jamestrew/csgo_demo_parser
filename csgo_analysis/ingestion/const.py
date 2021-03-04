from enum import Enum


class Map(Enum):
    DUST2 = 1
    MIRAGE = 2
    INFERNO = 3
    CACHE = 4
    OVERPASS = 5
    TRAIN = 6
    NUKE = 7
    CBBLE = 8
    VERTIGO = 9


class EventTypes:
    PLAYER_BLIND = 'player_blind'
    PLAYER_DEATH = 'player_death'
    PLAYER_HURT = 'player_hurt'
    PLAYER_FALLDAMAGE = 'player_falldamage'

    WEAPON_FIRE = 'weapon_fire'

    ITEM_PICKUP = 'item_pickup'
    ITEM_EQUIP = 'item_equip'
    ITEM_REMOVE = 'item_remove'

    BOMB_PLANTED = 'bomb_planted'
    BOMB_DEFUSED = 'bomb_defused'

    ROUND_START = 'round_start'
    ROUND_END = 'round_end'
    ROUND_MVP = 'round_mvp'

    _PLAYER_INFO = 'player_info'
    _PLAYER_SPAWN = 'player_spawn'

    PLAYER_EVENTS = [
        PLAYER_DEATH,
        PLAYER_BLIND,
        PLAYER_HURT,
        PLAYER_FALLDAMAGE,
        WEAPON_FIRE,
        ITEM_EQUIP,
        ITEM_REMOVE,
        ITEM_PICKUP,
        BOMB_PLANTED,
        BOMB_DEFUSED,
        ROUND_MVP
    ]

    ITEM_EVENTS = [
        PLAYER_DEATH,
        PLAYER_HURT,
        WEAPON_FIRE,
        ITEM_REMOVE,
        ITEM_EQUIP,
        ITEM_PICKUP
    ]

    ALL_EVENTS = [
        PLAYER_DEATH,
        PLAYER_BLIND,
        PLAYER_HURT,
        PLAYER_FALLDAMAGE,
        WEAPON_FIRE,
        ITEM_EQUIP,
        ITEM_REMOVE,
        ITEM_PICKUP,
        BOMB_PLANTED,
        BOMB_DEFUSED,
        ROUND_MVP,
        ROUND_START,
        ROUND_END
    ]

    ALL_NECESSARY_DATA = [
        PLAYER_DEATH,
        PLAYER_BLIND,
        PLAYER_HURT,
        PLAYER_FALLDAMAGE,
        WEAPON_FIRE,
        ITEM_EQUIP,
        ITEM_REMOVE,
        ITEM_PICKUP,
        BOMB_PLANTED,
        BOMB_DEFUSED,
        ROUND_MVP,
        ROUND_START,
        ROUND_END,
        _PLAYER_INFO,
        _PLAYER_SPAWN
    ]

    UNNECESSARY_DATA = [
        'bomb_begindefuse',
        'bomb_beginplant',
        'bomb_dropped',
        'bomb_exploded',
        'bomb_pickup',
        'cs_win_panel_round',
        'decoy_detonate',
        'decoy_started',
        'flashbang_detonate',
        'hegrenade_detonate',
        'hltv_chase',
        'hltv_message',
        'hltv_status',
        'inferno_expire',
        'inferno_startburn',
        'player_connect_full',
        'player_jump',
        'player_team',
        'smokegrenade_detonate',
        'smokegrenade_expired',
        'weapon_reload',
        'weapon_zoom',
    ]
