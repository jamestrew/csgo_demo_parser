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
    RoundStart,
    EventJson
)


class EventsController:

    def __init__(self, game_id, data, player_list):
        self.game_id = game_id
        self.data = data
        self._player_blind = PlayerBlind()
        self._player_death = PlayerDeath()
        self._player_hurt = PlayerHurt()
        self._player_falldamage = PlayerFallDamage()
        self._weapon_fire = WeaponFire()
        self._item_equip = ItemEquip()
        self._bomb_planted = BombPlanted()
        self._bomb_defused = BombDefused()
        self._round_start = RoundStart()
        self._round_end = RoundEnd()
        self._round_mvp = RoundMVP()
        self._events = [
            self._player_blind,
            self._player_death,
            self._player_hurt,
            self._player_falldamage,
            self._weapon_fire,
            self._item_equip,
            self._bomb_planted,
            self._bomb_defused,
            self._round_end,
            self._round_start,
            self._round_mvp
        ]
        self.clean_data = []

        self.player_health = {player: 100 for player in player_list}

    def ingest_prep(self):
        round_cnt = 0
        event_cnt = 0
        for event in self.data:
            event_name = list(event.keys())[0]
            event_data = event[event_name]

            if event_name not in EventTypes.ALL_EVENTS:
                continue

            if 'userid' in event_data.keys() and event_data['userid'] is None:
                continue
            if event_name in EventTypes.ALL_EVENTS:
                event_cnt += 1
            if event_name == EventTypes.ROUND_START:
                round_cnt += 1

            data = event[event_name]
            event_class = getattr(self, '_' + event_name)

            # correct for overkill damage
            if event_name == EventTypes.PLAYER_HURT:
                player_id = data[PlayerHurt._COMP[PlayerHurt._PLAYER_ID]]
                health = int(data[PlayerHurt._COMP[PlayerHurt._HEALTH]])
                if health > 0:
                    self.player_health[player_id] = health
                else:  # overkill situation
                    prev_health = self.player_health[player_id]  # actual dmg done
                    data[PlayerHurt._COMP[PlayerHurt._DMG_HEALTH]] = prev_health
                    self.player_health[player_id] = 100

            data = event_class.build_event(self.game_id, data, event_cnt, round_cnt)
            if data:
                self.clean_data.append({event_class._TABLE_NAME: data})

    def ingest_data(self):
        for event in self._events:
            if len(event.data_set) > 0:
                event.insert(event._TABLE_NAME, event.data_set)

        EventJson().insert_prep(self.game_id, self.clean_data)
