

class EventTypes:
    PLAYER_BLIND = 'player_blind'
    PLAYER_DEATH = 'player_death'
    PLAYER_HURT = 'player_hurt'
    PLAYER_FALLDAMAGE = 'player_falldamage'

    WEAPON_FIRE = 'weapon_fire'

    ITEM_EQUIP = 'item_equip'

    BOMB_PLANTED = 'bomb_planted'
    BOMB_DEFUSED = 'bomb_defused'

    ROUND_START = 'round_start'
    ROUND_END = 'round_end'
    ROUND_MVP = 'round_mvp'

    PLAYER_INFO = 'player_info'
    PLAYER_SPAWN = 'player_spawn'

    PLAYER_CLEANUP = [PLAYER_INFO, PLAYER_SPAWN]

    BEGIN_NEW_MATCH = 'begin_new_match'

    PLAYER_EVENTS = [
        PLAYER_DEATH,
        PLAYER_BLIND,
        PLAYER_HURT,
        PLAYER_FALLDAMAGE,
        WEAPON_FIRE,
        ITEM_EQUIP,
        BOMB_PLANTED,
        BOMB_DEFUSED,
        ROUND_MVP
    ]

    ITEM_EVENTS = [
        PLAYER_DEATH,
        PLAYER_HURT,
        WEAPON_FIRE,
        ITEM_EQUIP,
    ]

    ALL_EVENTS = [
        PLAYER_DEATH,
        PLAYER_BLIND,
        PLAYER_HURT,
        PLAYER_FALLDAMAGE,
        WEAPON_FIRE,
        ITEM_EQUIP,
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
        BOMB_PLANTED,
        BOMB_DEFUSED,
        ROUND_MVP,
        ROUND_START,
        ROUND_END,
        PLAYER_INFO,
        PLAYER_SPAWN
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
        'item_pickup',
        'item_remove'
    ]
