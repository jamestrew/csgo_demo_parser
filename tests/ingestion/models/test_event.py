from csgo_analysis.ingestion.const import EventTypes
from csgo_analysis.ingestion.models import (  # noqa
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


def test_build_event_player_blind():
    event_data = {
        "entityid": "363 ",
        "blind_duration": "2.782995 ",
        "userid": 8,
        "attacker": 4,
        "team": "CT "
    }

    rs = {
        "game_id": 1,
        "blind_duration": 2.782995,
        "player_id": 8,
        "attacker_id": 4,
        "team": "CT",
        "event_number": 1,
        "round": 1
    }

    event = PlayerBlind()
    output = event.build_event(1, event_data, 1, 1)
    assert output == rs
    assert event.data_set == [rs]
    assert event._TABLE_NAME == EventTypes.PLAYER_BLIND


def test_build_event_player_death():
    event_data = {
        "item_id": 26,
        "player_item_id": 17,
        "distance": "12.206310 ",
        "penetrated": "0 ",
        "assistedflash": "0 ",
        "wipe": "0 ",
        "attacker": 8,
        "weapon_fauxitemid": "17293822569119744010 ",
        "assister": None,
        "dominated": "0 ",
        "weapon_originalowner_xuid": "76561198133822308 ",
        "attackerblind": "0 ",
        "weapon_itemid": "963864360 ",
        "noscope": "0 ",
        "noreplay": "0 ",
        "thrusmoke": "0 ",
        "headshot": "1 ",
        "revenge": "0 ",
        "userid": 4,
        "team": "CT "
    }

    rs = {
        "game_id": 1,
        "item_id": 26,
        "player_item_id": 17,
        "distance": 12.206310,
        "penetrated": False,
        "assistedflash": False,
        "wipe": False,
        "attacker_id": 8,
        "assister_id": None,
        "dominated": False,
        "attackerblind": False,
        "noscope": False,
        "thrusmoke": False,
        "headshot": True,
        "revenge": False,
        "player_id": 4,
        "team": "CT",
        "event_number": 1,
        "round": 1
    }
    event = PlayerDeath()
    output = event.build_event(1, event_data, 1, 1)
    assert output == rs
    assert event.data_set == [rs]
    assert event._TABLE_NAME == EventTypes.PLAYER_DEATH


def test_build_event_player_hurt():
    event_data = {
        "item_id": 6,
        "dmg_health": "8 ",
        "armor": "95 ",
        "health": "21 ",
        "dmg_armor": "4 ",
        "hitgroup": "2 ",
        "userid": 5,
        "attacker": 6,
        "team": "CT "
    }
    rs = {
        "game_id": 1,
        "item_id": 6,
        "dmg_health": 8,
        "armor": 95,
        "health": 21,
        "dmg_armor": 4,
        "hitgroup": 2,
        "player_id": 5,
        "attacker_id": 6,
        "team": "CT",
        "event_number": 1,
        "round": 1
    }

    event = PlayerHurt()
    output = event.build_event(1, event_data, 1, 1)
    assert output == rs
    assert event.data_set == [rs]
    assert event._TABLE_NAME == EventTypes.PLAYER_HURT


def test_build_event_player_falldamage():
    event_data = {
        "userid": 6,
        "damage": "0.297619 ",
        "team": "CT "
    }

    rs = {
        "game_id": 1,
        "player_id": 6,
        "damage": 0.297619,
        "team": "CT",
        "event_number": 1,
        "round": 1
    }

    event = PlayerFallDamage()
    output = event.build_event(1, event_data, 1, 1)
    assert output == rs
    assert event.data_set == [rs]
    assert event._TABLE_NAME == EventTypes.PLAYER_FALLDAMAGE


def test_build_event_weapon_fire():
    data = {
        "item_id": 28,
        "silenced": "1 ",
        "userid": 8,
        "team": "CT "
    }
    rs = {
        "game_id": 1,
        "item_id": 28,
        "silenced": True,
        "player_id": 8,
        "team": "CT",
        "event_number": 1,
        "round": 1
    }
    event = WeaponFire()
    output = event.build_event(1, data, 1, 1)
    assert output == rs
    assert event.data_set == [rs]
    assert event._TABLE_NAME == EventTypes.WEAPON_FIRE


def test_build_event_item_equip():
    data = {
        "canzoom": "0 ",
        "userid": 2,
        "hastracers": "0 ",
        "issilenced": "0 ",
        "ispainted": "1 ",
        "weptype": "0 ",
        "defindex": "515 ",
        "hassilencer": "0 ",
        "item_id": 42,
        "team": "CT "
    }
    rs = {
        "game_id": 1,
        "player_id": 2,
        "item_id": 42,
        "team": "CT",
        "event_number": 1,
        "round": 1
    }
    event = ItemEquip()
    output = event.build_event(1, data, 1, 1)
    assert output == rs
    assert event.data_set == [rs]
    assert event._TABLE_NAME == EventTypes.ITEM_EQUIP


def test_build_event_bomb_planted():
    event_data = {
        "site": "301 ",
        "userid": 4,
        "team": "CT "
    }

    rs = {
        "game_id": 1,
        "site": 301,
        "player_id": 4,
        "team": "CT",
        "event_number": 1,
        "round": 1
    }

    event = BombPlanted()
    output = event.build_event(1, event_data, 1, 1)
    assert output == rs
    assert event.data_set == [rs]
    assert event._TABLE_NAME == EventTypes.BOMB_PLANTED


def test_build_event_bomb_defused():
    event_data = {
        "site": "302 ",
        "userid": 1,
        "team": "CT "
    }

    rs = {
        "game_id": 1,
        "site": 302,
        "player_id": 1,
        "team": "CT",
        "event_number": 1,
        "round": 1
    }

    event = BombDefused()
    output = event.build_event(1, event_data, 1, 1)
    assert output == rs
    assert event.data_set == [rs]
    assert event._TABLE_NAME == EventTypes.BOMB_DEFUSED


def test_build_event_round_start():
    event_data = {
        "objective": "BOMB TARGET ",
        "timelimit": "999 ",
        "fraglimit": "0 "
    }

    rs = {
        'game_id': 1,
        'timelimit': 999,
        'event_number': 1,
        'round': 1
    }

    event = RoundStart()
    output = event.build_event(1, event_data, 1, 1)
    assert output == rs
    assert event.data_set == [rs]
    assert event._TABLE_NAME == EventTypes.ROUND_START


def test_build_event_round_end():
    data = {
        "nomusic": "0 ",
        "player_count": "10 ",
        "reason": "9 ",
        "legacy": "0 ",
        "message": "#SFUI_Notice_Terrorists_Win ",
        "winner": "2 "
    }
    rs = {
        "game_id": 1,
        "reason": 9,
        "message": "#SFUI_Notice_Terrorists_Win",
        "team_l_id": 2,
        "event_number": 1,
        "round": 1
    }
    event = RoundEnd()
    output = event.build_event(1, data, 1, 1)
    assert output == rs
    assert event.data_set == [rs]
    assert event._TABLE_NAME == EventTypes.ROUND_END


def test_build_event_round_mvp():
    event_data = {
        "nomusic": "0 ",
        "value": "0 ",
        "musickitmvps": "0 ",
        "reason": "3 ",
        "userid": 1,
        "team": "CT "
    }

    rs = {
        "game_id": 1,
        "reason": 3,
        "player_id": 1,
        "team": "CT",
        "event_number": 1,
        "round": 1
    }

    event = RoundMVP()
    output = event.build_event(1, event_data, 1, 1)
    assert output == rs
    assert event.data_set == [rs]
    assert event._TABLE_NAME == EventTypes.ROUND_MVP
