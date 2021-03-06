import pytest
from csgo_analysis.ingestion.const import EventTypes
from csgo_analysis.ingestion.models import (  # noqa
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


def test_build_event_player_blind():
    event_data = {
        "attacker": 76561198079455814,
        "userid": 76561198133822308,
        "blind_duration": "2.782995 ",
        "entityid": "363 "
    }

    rs = {
        'game_id': 1,
        'player_id': 76561198133822308,
        'attacker_id': 76561198079455814,
        'blind_duration': 2.782995,
        'event_number': 1,
        'round': 1
    }

    event = PlayerBlind()
    output = event.build_event(1, event_data, 1, 1)
    assert output == rs
    assert event.data_set == [rs]
    assert event._TABLE_NAME == EventTypes.PLAYER_BLIND


@pytest.mark.skip()
def test_build_event_player_death():
    pass


@pytest.mark.skip()
def test_build_event_player_hurt():
    pass


def test_build_event_player_falldamage():
    event_data = {
        "userid": 76561198974483816,
        "damage": "0.297619 "
    }

    rs = {
        'game_id': 1,
        'player_id': 76561198974483816,
        'damage': 0.297619,
        'event_number': 1,
        'round': 1
    }

    event = PlayerFallDamage()
    output = event.build_event(1, event_data, 1, 1)
    assert output == rs
    assert event.data_set == [rs]
    assert event._TABLE_NAME == EventTypes.PLAYER_FALLDAMAGE


@pytest.mark.skip()
def test_build_event_weapon_fire():
    pass


@pytest.mark.skip()
def test_build_event_item_pickup():
    pass


@pytest.mark.skip()
def test_build_event_item_equip():
    pass


@pytest.mark.skip()
def test_build_event_item_remove():
    pass


def test_build_event_bomb_planted():
    event_data = {
        "userid": 76561198079455814,
        "site": "301 "
    }

    rs = {
        'game_id': 1,
        'player_id': 76561198079455814,
        'site': 301,
        'event_number': 1,
        'round': 1
    }

    event = BombPlanted()
    output = event.build_event(1, event_data, 1, 1)
    assert output == rs
    assert event.data_set == [rs]
    assert event._TABLE_NAME == EventTypes.BOMB_PLANTED


def test_build_event_bomb_defused():
    event_data = {
        "userid": 76561198128398569,
        "site": "302 "
    }

    rs = {
        'game_id': 1,
        'player_id': 76561198128398569,
        'site': 302,
        'event_number': 1,
        'round': 1
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


@pytest.mark.skip()
def test_build_event_round_end():
    pass


def test_build_event_round_mvp():
    event_data = {
        "userid": 76561198802446098,
        "nomusic": "0 ",
        "reason": "1 ",
        "musickitmvps": "0 ",
        "value": "0 "
    }

    rs = {
        'game_id': 1,
        'player_id': 76561198802446098,
        'reason': 1,
        'event_number': 1,
        'round': 1
    }

    event = RoundMVP()
    output = event.build_event(1, event_data, 1, 1)
    assert output == rs
    assert event.data_set == [rs]
    assert event._TABLE_NAME == EventTypes.ROUND_MVP
