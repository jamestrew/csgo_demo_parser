from csgo_analysis.ingestion.const import EventTypes
from csgo_analysis.ingestion.models import (
    PlayerBlind,
    PlayerDeath,
    PlayerHurt,
    PlayerFallDamage,
    WeaponFire,
    ItemEquip,
    ItemPickup,
    ItemRemove,
    BombDefused,
    BombPlanted,
    RoundEnd,
    RoundMVP,
    RoundStart
)


class EventsController:

    def __init__(self, game_id, data):
        self.game_id = game_id
        self.data = data
        self.player_blind = PlayerBlind()
        self.player_death = PlayerDeath()
        self.player_hurt = PlayerHurt()
        self.player_falldamage = PlayerFallDamage()
        self.weapon_fire = WeaponFire()
        self.item_pickup = ItemPickup()
        self.item_equip = ItemEquip()
        self.item_remove = ItemRemove()
        self.bomb_planted = BombPlanted()
        self.bomb_defused = BombDefused()
        self.round_start = RoundStart()
        self.round_end = RoundEnd()
        self.round_mvp = RoundMVP()

    def ingest_data(self):
        round_count = 0
        event_count = 0
        for event in self.data:
            event_name = list(event.keys())[0]
            event_data = event[event_name]
            if 'userid' in event_data.keys() and \
                    isinstance(event_data['userid'], str):
                continue
            if event_name in EventTypes.ALL_EVENTS:
                event_count += 1
            if event_name == EventTypes.ROUND_START:
                round_count += 1

            # event_class = getattr(self, event_name)
            # event_class.build_event(self.game_id, event[event_name], event_count, round_count)

            self.item_equip.build_event(self.game_id, event_data, event_count, round_count)
