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


class Items:

    _CZ75A = 'weapon_cz75a'
    _DEAGLE = 'weapon_deagle'
    _ELITE = 'weapon_elite'
    _FIVESEVEN = 'weapon_fiveseven'
    _GLOCK = 'weapon_glock'
    _HKP2000 = 'weapon_hkp2000'
    _P250 = 'weapon_p250'
    _REVOLVER = 'weapon_revolver'
    _TEC9 = 'weapon_tec9'
    _USP_SILENCER = 'weapon_usp_silencer'
    _MAG7 = 'weapon_mag7'
    _NOVA = 'weapon_nova'
    _SAWEDOFF = 'weapon_sawedoff'
    _XM1014 = 'weapon_xm1014'
    _M249 = 'weapon_m249'
    _NEGEV = 'weapon_negev'
    _MAC10 = 'weapon_mac10'
    _MP5SD = 'weapon_mp5sd'
    _MP7 = 'weapon_mp7'
    _MP9 = 'weapon_mp9'
    _P90 = 'weapon_p90'
    _BIZON = 'weapon_bizon'
    _UMP45 = 'weapon_ump45'
    _AK47 = 'weapon_ak47'
    _AUG = 'weapon_aug'
    _FAMAS = 'weapon_famas'
    _GALILAR = 'weapon_galilar'
    _M4A1_SILENCER = 'weapon_m4a1_silencer'
    _M4A1 = 'weapon_m4a1'
    _SG556 = 'weapon_sg556'
    _AWP = 'weapon_awp'
    _G3SG1 = 'weapon_g3sg1'
    _SCAR20 = 'weapon_scar20'
    _SSG08 = 'weapon_ssg08'
    _TASER = 'weapon_taser'
    _HEGRENADE = 'weapon_hegrenade'
    _FLASHBANG = 'weapon_flashbang'
    _SMOKEGRENADE = 'weapon_smokegrenade'
    _INCGRENADE = 'weapon_incgrenade'
    _MOLOTOV = 'weapon_molotov'
    _DECOY = 'weapon_decoy'
    _KNIFE = 'weapon_knife'
    _KNIFE_T = 'weapon_knife_t'
    _KNIFEGG = 'weapon_knifegg'
    _KNIFE_CSS = 'weapon_knife_css'
    _BAYONET = 'weapon_bayonet'
    _KNIFE_FLIP = 'weapon_knife_flip'
    _KNIFE_GUT = 'weapon_knife_gut'
    _KNIFE_KARAMBIT = 'weapon_knife_karambit'
    _KNIFE_M9_BAYONET = 'weapon_knife_m9_bayonet'
    _KNIFE_TACTICAL = 'weapon_knife_tactical'
    _KNIFE_BUTTERFLY = 'weapon_knife_butterfly'
    _KNIFE_FALCHION = 'weapon_knife_falchion'
    _KNIFE_PUSH = 'weapon_knife_push'
    _KNIFE_SURVIVAL = 'weapon_knife_survival'
    _KNIFE_URSUS = 'weapon_knife_ursus'
    _KNIFE_GYPSY_JACKKNIFE = 'weapon_knife_gypsy_jackknife'
    _KNIFE_STILETTO = 'weapon_knife_stiletto'
    _KNIFE_WIDOWMAKER = 'weapon_knife_widowmaker'
    _KNIFE_GHOST = 'weapon_knife_ghost'
    _KNIFE_CANIS = 'weapon_knife_canis'
    _KNIFE_CORD = 'weapon_knife_cord'
    _KNIFE_SKELETON = 'weapon_knife_skeleton'
    _KNIFE_OUTDOOR = 'weapon_knife_outdoor'
    _KEVLAR = 'item_kevlar'
    _ASSAULTSUIT = 'item_assaultsuit'
    _DEFUSER = 'item_defuser'
    _C4 = 'c4'

    # IDs
    _CZ75A_ID = 1
    _DEAGLE_ID = 2
    _ELITE_ID = 3
    _FIVESEVEN_ID = 4
    _GLOCK_ID = 5
    _HKP2000_ID = 6
    _P250_ID = 7
    _REVOLVER_ID = 8
    _TEC9_ID = 9
    _USP_SILENCER_ID = 10
    _MAG7_ID = 11
    _NOVA_ID = 12
    _SAWEDOFF_ID = 13
    _XM1014_ID = 14
    _M249_ID = 15
    _NEGEV_ID = 16
    _MAC10_ID = 17
    _MP5SD_ID = 18
    _MP7_ID = 19
    _MP9_ID = 20
    _P90_ID = 21
    _BIZON_ID = 22
    _UMP45_ID = 23
    _AK47_ID = 24
    _AUG_ID = 25
    _FAMAS_ID = 26
    _GALILAR_ID = 27
    _M4A1_SILENCER_ID = 28
    _M4A1_ID = 29
    _SG556_ID = 30
    _AWP_ID = 31
    _G3SG1_ID = 32
    _SCAR20_ID = 33
    _SSG08_ID = 34
    _TASER_ID = 35
    _HEGRENADE_ID = 36
    _FLASHBANG_ID = 37
    _SMOKEGRENADE_ID = 38
    _INCGRENADE_ID = 39
    _MOLOTOV_ID = 40
    _DECOY_ID = 41
    _KNIFE_ID = 42
    _KNIFE_T_ID = 42
    _KNIFEGG_ID = 42
    _KNIFE_CSS_ID = 42
    _BAYONET_ID = 42
    _KNIFE_FLIP_ID = 42
    _KNIFE_GUT_ID = 42
    _KNIFE_KARAMBIT_ID = 42
    _KNIFE_M9_BAYONET_ID = 42
    _KNIFE_TACTICAL_ID = 42
    _KNIFE_BUTTERFLY_ID = 42
    _KNIFE_FALCHION_ID = 42
    _KNIFE_PUSH_ID = 42
    _KNIFE_SURVIVAL_ID = 42
    _KNIFE_URSUS_ID = 42
    _KNIFE_GYPSY_JACKKNIFE_ID = 42
    _KNIFE_STILETTO_ID = 42
    _KNIFE_WIDOWMAKER_ID = 42
    _KNIFE_GHOST_ID = 42
    _KNIFE_CANIS_ID = 42
    _KNIFE_CORD_ID = 42
    _KNIFE_SKELETON_ID = 42
    _KNIFE_OUTDOOR_ID = 42
    _KEVLAR_ID = 65
    _ASSAULTSUIT_ID = 66
    _DEFUSER_ID = 67
    _C4_ID = 68

    _SUPPRESSED = ['m4a1', 'mp7', 'hpk2000']
    _ALT = ['p250']  # maybe revolver?

    @staticmethod
    def short_wep(item):
        return item.__name__
