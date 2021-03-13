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
        self.clean_data = []

        self.player_health = {player: 100 for player in player_list}

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
            self.clean_data.append({event_class._TABLE_NAME: data})
