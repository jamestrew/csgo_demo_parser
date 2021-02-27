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


class Events:
    PLAYER_BLIND = 'player_bind'
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
