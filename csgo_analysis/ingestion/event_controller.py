from csgo_analysis.ingestion.const import EventTypes
from csgo_analysis.ingestion.models import (
    PlayerBlind,
    PlayerDeath,
    PlayerHurt,
    PlayerFallDamage,
    WeaponFire,
    ItemEquip,
    BombDefused,
    BombPlanted,
    RoundEnd,
    RoundMVP,
    RoundStart
)


class EventsController:

    def __init__(self, game_id, data, player_xuids):
        self.game_id = game_id
        self.data = data
        self.player_blind = PlayerBlind()
        self.player_death = PlayerDeath()
        self.player_hurt = PlayerHurt()
        self.player_falldamage = PlayerFallDamage()
        self.weapon_fire = WeaponFire()
        self.item_equip = ItemEquip()
        self.bomb_planted = BombPlanted()
        self.bomb_defused = BombDefused()
        self.round_start = RoundStart()
        self.round_end = RoundEnd()
        self.round_mvp = RoundMVP()
        self.clean_data = []
        self.player_equip_state = {}

        for xuid in player_xuids:
            self.player_equip_state[xuid] = None

    def ingest_data(self):
        round_cnt = 0
        event_cnt = 0
        for event in self.data:
            event_name = list(event.keys())[0]
            event_data = event[event_name]
            if 'userid' in event_data.keys() and \
                    isinstance(event_data['userid'], str):
                continue
            if event_name in EventTypes.ALL_EVENTS:
                event_cnt += 1
            if event_name == EventTypes.ROUND_START:
                round_cnt += 1

            data = event[event_name]
            event_class = getattr(self, event_name)
            data = event_class.build_event(self.game_id, data, event_cnt, round_cnt)
            self.clean_data.append(data)
