from csgo_analysis.ingestion.const import EventTypes


class EventsController:

    def __init__(self, game_id, data):
        self.game_id = game_id
        self.data = data
        self.player_blind = PlayerBlind(game_id)
        self.player_death = PlayerDeath(game_id)
        self.player_hurt = PlayerHurt(game_id)
        self.player_falldamage = PlayerFallDamage(game_id)
        self.weapon_fire = WeaponFire(game_id)
        self.item_pickup = ItemPickup(game_id)
        self.item_equip = ItemEquip(game_id)
        self.item_remove = ItemRemove(game_id)
        self.bomb_planted = BombPlanted(game_id)
        self.bomb_defused = BombDefused(game_id)
        self.round_start = RoundStart(game_id)
        self.round_end = RoundEnd(game_id)
        self.round_mvp = RoundMVP(game_id)


class Event:

    def __init__(self, game_id):
        self.game_id = game_id

    def get_event_number(self):
        pass


class PlayerBlind(Event):

    # columns
    _ID = 'id'
    _GAME_ID = 'game_id'
    _PLAYER_ID = 'player_id'
    _ATTACKER_ID = 'attacker_id'
    _BLIND_DURATION = 'blind_duration'
    _EVENT_NUMBER = 'event_number'
    _ROUND = 'round'

    _TABLE_NAME = EventTypes.PLAYER_BLIND

    def __init__(self, game_id):
        super().__init__(game_id)


class PlayerDeath(Event):

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

    _TABLE_NAME = EventTypes.PLAYER_DEATH

    def __init__(self):
        super().__init__()


class PlayerHurt(Event):
    def __init__(self):
        super().__init__()


class PlayerFallDamage(Event):
    def __init__(self):
        super().__init__()


class WeaponFire(Event):
    def __init__(self):
        super().__init__()


class ItemPickup(Event):
    def __init__(self):
        super().__init__()


class ItemEquip(Event):
    def __init__(self):
        super().__init__()


class ItemRemove(Event):
    def __init__(self):
        super().__init__()


class BombPlanted(Event):
    def __init__(self):
        super().__init__()


class BombDefused(Event):
    def __init__(self):
        super().__init__()


class RoundStart(Event):
    def __init__(self):
        super().__init__()


class RoundEnd(Event):
    def __init__(self):
        super().__init__()


class RoundMVP(Event):
    def __init__(self):
        super().__init__()
