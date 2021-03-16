from unittest.mock import patch
import pytest
from psycopg2._psycopg import TimestampFromTicks

from csgo_analysis.ingestion.const import EventTypes
from csgo_analysis.ingestion.models import (BombDefused, BombPlanted,  # noqa
                                            EventJson, ItemEquip, PlayerBlind,
                                            PlayerDeath, PlayerFallDamage,
                                            PlayerHurt, RoundEnd, RoundMVP,
                                            RoundStart, WeaponFire)


@pytest.fixture(scope='module')
def game_id(db_cur):
    insert_str = "INSERT INTO game (share_code, match_time, match_duration, map_l_id, final_score_two, final_score_three) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    val = ['CSGO-xQKYC-4Nbc4-h43V2-Jc66v-EWtrT', TimestampFromTicks(1613364114), 2319, 1, 10, 16]

    db_cur.execute(insert_str, val)
    return db_cur.fetchone()[0]


@pytest.fixture(scope='module')
def player_id(db_cur, game_id):
    insert_str = """
        INSERT INTO player (game_id, team_l_id, xuid, player_name)
        VALUES (%s, %s, %s, %s)
        RETURNING id
    """
    val = [game_id, 1, 123345, 's1mple']
    db_cur.execute(insert_str, val)
    return db_cur.fetchone()[0]


@pytest.fixture(scope='module')
def attacker_id(db_cur, game_id):
    insert_str = """
        INSERT INTO player (game_id, team_l_id, xuid, player_name)
        VALUES (%s, %s, %s, %s)
        RETURNING id
    """
    val = [game_id, 1, 456789, 'device']
    db_cur.execute(insert_str, val)
    return db_cur.fetchone()[0]


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


@patch.object(PlayerBlind, 'connect')
@patch.object(PlayerBlind, 'close')
def test_player_blind_insert(connect_patch, close_path,
                             game_id, player_id, db_conn, db_cur, attacker_id):
    rs = [
        {
            "game_id": game_id,
            "blind_duration": 2.782995,
            "player_id": player_id,
            "attacker_id": attacker_id,
            "team": "CT",
            "event_number": 1,
            "round": 1
        },
        {
            "game_id": game_id,
            "blind_duration": 2.782995,
            "player_id": player_id,
            "attacker_id": attacker_id,
            "team": "CT",
            "event_number": 2,
            "round": 1
        }
    ]

    pb = PlayerBlind()
    pb.conn = db_conn
    pb.cur = db_cur
    pb.data_set = rs
    pb.insert(pb._TABLE_NAME, rs)
    connect_patch.assert_called_once()
    close_path.assert_called_once()


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


def test_build_event_player_death2():
    event_data = {
        "item_id": None,
        "player_item_id": 17,
        "distance": "12.206310 ",
        "penetrated": "0 ",
        "assistedflash": "0 ",
        "wipe": "0 ",
        "attacker": None,
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
        "item_id": None,
        "player_item_id": 17,
        "distance": 12.206310,
        "penetrated": False,
        "assistedflash": False,
        "wipe": False,
        "attacker_id": None,
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


@patch.object(PlayerDeath, 'connect')
@patch.object(PlayerDeath, 'close')
def test_player_death_insert(connect_patch, close_path,
                             game_id, player_id, db_conn, db_cur, attacker_id):
    rs = [
        {
            "game_id": game_id,
            "item_id": 26,
            "player_item_id": 17,
            "distance": 12.206310,
            "penetrated": False,
            "assistedflash": False,
            "wipe": False,
            "attacker_id": attacker_id,
            "assister_id": None,
            "dominated": False,
            "attackerblind": False,
            "noscope": False,
            "thrusmoke": False,
            "headshot": True,
            "revenge": False,
            "player_id": player_id,
            "team": "CT",
            "event_number": 1,
            "round": 1
        },
        {
            "game_id": game_id,
            "item_id": 26,
            "player_item_id": 17,
            "distance": 12.206310,
            "penetrated": False,
            "assistedflash": False,
            "wipe": False,
            "attacker_id": attacker_id,
            "assister_id": None,
            "dominated": False,
            "attackerblind": False,
            "noscope": False,
            "thrusmoke": False,
            "headshot": True,
            "revenge": False,
            "player_id": player_id,
            "team": "CT",
            "event_number": 2,
            "round": 1
        },
        {
            "game_id": game_id,
            "item_id": None,
            "player_item_id": 17,
            "distance": None,
            "penetrated": False,
            "assistedflash": False,
            "wipe": False,
            "attacker_id": None,
            "assister_id": None,
            "dominated": False,
            "attackerblind": False,
            "noscope": False,
            "thrusmoke": False,
            "headshot": True,
            "revenge": False,
            "player_id": player_id,
            "team": "CT",
            "event_number": 3,
            "round": 1
        }
    ]

    event = PlayerDeath()
    event.conn = db_conn
    event.cur = db_cur
    event.data_set = rs
    event.insert(event._TABLE_NAME, rs)
    connect_patch.assert_called_once()
    close_path.assert_called_once()


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


@patch.object(PlayerHurt, 'connect')
@patch.object(PlayerHurt, 'close')
def test_player_hurt_insert(connect_patch, close_path,
                            game_id, player_id, db_conn, db_cur, attacker_id):
    rs = [
        {
            "game_id": game_id,
            "item_id": 6,
            "dmg_health": 8,
            "armor": 95,
            "health": 21,
            "dmg_armor": 4,
            "hitgroup": 2,
            "player_id": player_id,
            "attacker_id": attacker_id,
            "team": "CT",
            "event_number": 1,
            "round": 1
        },
        {
            "game_id": game_id,
            "item_id": 6,
            "dmg_health": 8,
            "armor": 95,
            "health": 21,
            "dmg_armor": 4,
            "hitgroup": 2,
            "player_id": player_id,
            "attacker_id": attacker_id,
            "team": "CT",
            "event_number": 2,
            "round": 1
        },
        {
            "game_id": game_id,
            "item_id": None,
            "dmg_health": 8,
            "armor": 95,
            "health": 21,
            "dmg_armor": 4,
            "hitgroup": 2,
            "player_id": player_id,
            "attacker_id": None,
            "team": "CT",
            "event_number": 3,
            "round": 1
        }
    ]

    event = PlayerHurt()
    event.conn = db_conn
    event.cur = db_cur
    event.data_set = rs
    event.insert(event._TABLE_NAME, rs)
    connect_patch.assert_called_once()
    close_path.assert_called_once()


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


@patch.object(PlayerFallDamage, 'connect')
@patch.object(PlayerFallDamage, 'close')
def test_player_falldamage_insert(connect_patch, close_path,
                                  game_id, player_id, db_conn, db_cur):
    rs = [
        {
            "game_id": game_id,
            "player_id": player_id,
            "damage": 0.297619,
            "team": "CT",
            "event_number": 1,
            "round": 1
        },
        {
            "game_id": game_id,
            "player_id": player_id,
            "damage": 0.297619,
            "team": "CT",
            "event_number": 2,
            "round": 1
        }
    ]

    event = PlayerFallDamage()
    event.conn = db_conn
    event.cur = db_cur
    event.data_set = rs
    event.insert(event._TABLE_NAME, rs)
    connect_patch.assert_called_once()
    close_path.assert_called_once()


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


@patch.object(WeaponFire, 'connect')
@patch.object(WeaponFire, 'close')
def test_weapon_fire_insert(connect_patch, close_path,
                            game_id, player_id, db_conn, db_cur):
    rs = [
        {
            "game_id": game_id,
            "item_id": 28,
            "silenced": True,
            "player_id": player_id,
            "team": "CT",
            "event_number": 1,
            "round": 1
        },
        {
            "game_id": game_id,
            "item_id": 28,
            "silenced": True,
            "player_id": player_id,
            "team": "CT",
            "event_number": 2,
            "round": 1
        }
    ]

    event = WeaponFire()
    event.conn = db_conn
    event.cur = db_cur
    event.data_set = rs
    event.insert(event._TABLE_NAME, rs)
    connect_patch.assert_called_once()
    close_path.assert_called_once()


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


@patch.object(ItemEquip, 'connect')
@patch.object(ItemEquip, 'close')
def test_item_equip_insert(connect_patch, close_path,
                           game_id, player_id, db_conn, db_cur):
    rs = [
        {
            "game_id": game_id,
            "player_id": player_id,
            "item_id": 42,
            "team": "CT",
            "event_number": 1,
            "round": 1
        },
        {
            "game_id": game_id,
            "player_id": player_id,
            "item_id": 42,
            "team": "CT",
            "event_number": 2,
            "round": 1
        }
    ]

    event = ItemEquip()
    event.conn = db_conn
    event.cur = db_cur
    event.data_set = rs
    event.insert(event._TABLE_NAME, rs)
    connect_patch.assert_called_once()
    close_path.assert_called_once()


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


@patch.object(BombPlanted, 'connect')
@patch.object(BombPlanted, 'close')
def test_bomb_planted_insert(connect_patch, close_path,
                             game_id, player_id, db_conn, db_cur):
    rs = [
        {
            "game_id": game_id,
            "site": 301,
            "player_id": player_id,
            "team": "CT",
            "event_number": 1,
            "round": 1
        }
    ]

    event = BombPlanted()
    event.conn = db_conn
    event.cur = db_cur
    event.data_set = rs
    event.insert(event._TABLE_NAME, rs)
    connect_patch.assert_called_once()
    close_path.assert_called_once()


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


@patch.object(BombDefused, 'connect')
@patch.object(BombDefused, 'close')
def test_bomb_defused_insert(connect_patch, close_path,
                             game_id, player_id, db_conn, db_cur):
    rs = [
        {
            "game_id": game_id,
            "site": 302,
            "player_id": player_id,
            "team": "CT",
            "event_number": 1,
            "round": 1
        }
    ]

    event = BombDefused()
    event.conn = db_conn
    event.cur = db_cur
    event.data_set = rs
    event.insert(event._TABLE_NAME, rs)
    connect_patch.assert_called_once()
    close_path.assert_called_once()


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


@patch.object(RoundStart, 'connect')
@patch.object(RoundStart, 'close')
def test_round_start_insert(connect_patch, close_path,
                            game_id, db_conn, db_cur):
    rs = [
        {
            'game_id': game_id,
            'timelimit': 999,
            'event_number': 1,
            'round': 1
        }
    ]

    event = RoundStart()
    event.conn = db_conn
    event.cur = db_cur
    event.data_set = rs
    event.insert(event._TABLE_NAME, rs)
    connect_patch.assert_called_once()
    close_path.assert_called_once()


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
        "team_l_id": 1,
        "event_number": 1,
        "round": 1
    }
    event = RoundEnd()
    output = event.build_event(1, data, 1, 1)
    assert output == rs
    assert event.data_set == [rs]
    assert event._TABLE_NAME == EventTypes.ROUND_END


@patch.object(RoundEnd, 'connect')
@patch.object(RoundEnd, 'close')
def test_round_end_insert(connect_patch, close_path,
                          game_id, db_conn, db_cur):
    rs = [
        {
            "game_id": game_id,
            "reason": 9,
            "message": "#SFUI_Notice_Terrorists_Win",
            "team_l_id": 2,
            "event_number": 1,
            "round": 1
        }
    ]

    event = RoundEnd()
    event.conn = db_conn
    event.cur = db_cur
    event.data_set = rs
    event.insert(event._TABLE_NAME, rs)
    connect_patch.assert_called_once()
    close_path.assert_called_once()


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


@patch.object(RoundMVP, 'connect')
@patch.object(RoundMVP, 'close')
def test_round_mvp_insert(connect_patch, close_path,
                          game_id, player_id, db_conn, db_cur):
    rs = [
        {
            "game_id": game_id,
            "reason": 3,
            "player_id": player_id,
            "team": "CT",
            "event_number": 1,
            "round": 1
        }
    ]

    event = RoundMVP()
    event.conn = db_conn
    event.cur = db_cur
    event.data_set = rs
    event.insert(event._TABLE_NAME, rs)
    connect_patch.assert_called_once()
    close_path.assert_called_once()


@ patch.object(EventJson, 'connect')
@ patch.object(EventJson, 'close')
def test_json_insert_call(connect_p, close_p, game_id, db_cur, db_conn):
    data = [{'foo': 1, 'bar': None}, {1: 2, 3: 4}]
    ej = EventJson()
    ej.conn = db_conn
    ej.cur = db_cur
    ej.insert_prep(game_id, data)

    connect_p.assert_called_once()
    close_p.assert_called_once()
