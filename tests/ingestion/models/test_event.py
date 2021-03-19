from datetime import datetime
from unittest import TestCase
from unittest.mock import patch

import pytest

from csgo_analysis.ingestion.models.db import DB
from csgo_analysis.ingestion.const import EventTypes
from csgo_analysis.ingestion.models import (BombDefused, BombPlanted,  # noqa
                                            EventJson, ItemEquip, PlayerBlind,
                                            PlayerDeath, PlayerFallDamage,
                                            PlayerHurt, RoundEnd, RoundMVP,
                                            RoundStart, WeaponFire)


@pytest.fixture(scope='module')
def game_id(db_cur):
    insert_str = """INSERT INTO game (
        share_code,
        match_time,
        match_duration,
        map_l_id
    )
    VALUES (%s, %s, %s, %s) RETURNING id"""
    val = ['CSGO-xQKYC-4Nbc4-h43V2-Jc66v-EWtrT', datetime.fromtimestamp(1613364114), 2319, 1]

    db_cur.execute(insert_str, val)
    return db_cur.fetchone()[0]


@pytest.fixture(scope='module')
def player_id(db_cur, game_id):
    insert_str = """
        INSERT INTO player (game_id, first_team_l_id, xuid, player_name)
        VALUES (%s, %s, %s, %s)
        RETURNING id
    """
    val = [game_id, 2, '123345', 's1mple']
    db_cur.execute(insert_str, val)
    return db_cur.fetchone()[0]


@pytest.fixture(scope='module')
def attacker_id(db_cur, game_id):
    insert_str = """
        INSERT INTO player (game_id, first_team_l_id, xuid, player_name)
        VALUES (%s, %s, %s, %s)
        RETURNING id
    """
    val = [game_id, 3, '456788909', 'device']
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
        PlayerBlind._GAME_ID: 1,
        PlayerBlind._BLIND_DURATION: 2.782995,
        PlayerBlind._PLAYER_ID: 8,
        PlayerBlind._ATTACKER_ID: 4,
        PlayerBlind._TEAM_L_ID: 3,
        DB._EVENT_NUMBER: 1,
        DB._ROUND: 1
    }

    event = PlayerBlind()
    event.build_event(1, event_data, 1, 1)
    TestCase().assertDictEqual(event.rs, rs)
    assert event.data_set == [event.rs]
    assert event._TABLE_NAME == EventTypes.PLAYER_BLIND


@patch.object(PlayerBlind, 'connect')
@patch.object(PlayerBlind, 'close')
def test_player_blind_insert(connect_patch, close_path,
                             game_id, player_id, db_conn, db_cur, attacker_id):
    rs = [
        {
            DB._GAME_ID: game_id,
            PlayerBlind._BLIND_DURATION: 2.782995,
            DB._PLAYER_ID: player_id,
            DB._ATTACKER_ID: attacker_id,
            DB._TEAM_L_ID: 3,
            DB._EVENT_NUMBER: 1,
            DB._ROUND: 1
        },
        {
            DB._GAME_ID: game_id,
            PlayerBlind._BLIND_DURATION: 2.782995,
            DB._PLAYER_ID: player_id,
            DB._ATTACKER_ID: attacker_id,
            DB._TEAM_L_ID: 3,
            DB._EVENT_NUMBER: 2,
            DB._ROUND: 1
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
        DB._GAME_ID: 1,
        DB._ITEM_ID: 26,
        PlayerDeath._PLAYER_ITEM_ID: 17,
        PlayerDeath._DISTANCE: 12.206310,
        PlayerDeath._PENETRATED: False,
        PlayerDeath._ASSISTEDFLASH: False,
        PlayerDeath._WIPE: False,
        DB._ATTACKER_ID: 8,
        PlayerDeath._ASSISTER_ID: None,
        PlayerDeath._DOMINATED: False,
        PlayerDeath._ATTACKERBLIND: False,
        PlayerDeath._NOSCOPE: False,
        PlayerDeath._THRUSMOKE: False,
        PlayerDeath._HEADSHOT: True,
        PlayerDeath._REVENGE: False,
        DB._PLAYER_ID: 4,
        DB._TEAM_L_ID: 3,
        DB._EVENT_NUMBER: 1,
        DB._ROUND: 1
    }
    event = PlayerDeath()
    event.build_event(1, event_data, 1, 1)
    TestCase().assertDictEqual(event.rs, rs)
    assert event.data_set == [event.rs]
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
        DB._GAME_ID: 1,
        DB._ITEM_ID: None,
        PlayerDeath._PLAYER_ITEM_ID: 17,
        PlayerDeath._DISTANCE: 12.206310,
        PlayerDeath._PENETRATED: False,
        PlayerDeath._ASSISTEDFLASH: False,
        PlayerDeath._WIPE: False,
        DB._ATTACKER_ID: None,
        PlayerDeath._ASSISTER_ID: None,
        PlayerDeath._DOMINATED: False,
        PlayerDeath._ATTACKERBLIND: False,
        PlayerDeath._NOSCOPE: False,
        PlayerDeath._THRUSMOKE: False,
        PlayerDeath._HEADSHOT: True,
        PlayerDeath._REVENGE: False,
        DB._PLAYER_ID: 4,
        DB._TEAM_L_ID: 3,
        DB._EVENT_NUMBER: 1,
        DB._ROUND: 1
    }
    event = PlayerDeath()
    event.build_event(1, event_data, 1, 1)
    TestCase().assertDictEqual(event.rs, rs)
    assert event.data_set == [event.rs]
    assert event._TABLE_NAME == EventTypes.PLAYER_DEATH


@patch.object(PlayerDeath, 'connect')
@patch.object(PlayerDeath, 'close')
def test_player_death_insert(connect_patch, close_path,
                             game_id, player_id, db_conn, db_cur, attacker_id):
    rs = [
        {
            DB._GAME_ID: game_id,
            DB._ITEM_ID: 26,
            PlayerDeath._PLAYER_ITEM_ID: 17,
            PlayerDeath._DISTANCE: 12.206310,
            PlayerDeath._PENETRATED: False,
            PlayerDeath._ASSISTEDFLASH: False,
            PlayerDeath._WIPE: False,
            DB._ATTACKER_ID: attacker_id,
            PlayerDeath._ASSISTER_ID: None,
            PlayerDeath._DOMINATED: False,
            PlayerDeath._ATTACKERBLIND: False,
            PlayerDeath._NOSCOPE: False,
            PlayerDeath._THRUSMOKE: False,
            PlayerDeath._HEADSHOT: True,
            PlayerDeath._REVENGE: False,
            DB._PLAYER_ID: player_id,
            DB._TEAM_L_ID: 3,
            DB._EVENT_NUMBER: 1,
            DB._ROUND: 1
        },
        {
            DB._GAME_ID: game_id,
            DB._ITEM_ID: 26,
            PlayerDeath._PLAYER_ITEM_ID: 17,
            PlayerDeath._DISTANCE: 12.206310,
            PlayerDeath._PENETRATED: False,
            PlayerDeath._ASSISTEDFLASH: False,
            PlayerDeath._WIPE: False,
            DB._ATTACKER_ID: attacker_id,
            PlayerDeath._ASSISTER_ID: None,
            PlayerDeath._DOMINATED: False,
            PlayerDeath._ATTACKERBLIND: False,
            PlayerDeath._NOSCOPE: False,
            PlayerDeath._THRUSMOKE: False,
            PlayerDeath._HEADSHOT: True,
            PlayerDeath._REVENGE: False,
            DB._PLAYER_ID: player_id,
            DB._TEAM_L_ID: 3,
            DB._EVENT_NUMBER: 2,
            DB._ROUND: 1
        },
        {
            DB._GAME_ID: game_id,
            DB._ITEM_ID: None,
            PlayerDeath._PLAYER_ITEM_ID: 17,
            PlayerDeath._DISTANCE: None,
            PlayerDeath._PENETRATED: False,
            PlayerDeath._ASSISTEDFLASH: False,
            PlayerDeath._WIPE: False,
            DB._ATTACKER_ID: None,
            PlayerDeath._ASSISTER_ID: None,
            PlayerDeath._DOMINATED: False,
            PlayerDeath._ATTACKERBLIND: False,
            PlayerDeath._NOSCOPE: False,
            PlayerDeath._THRUSMOKE: False,
            PlayerDeath._HEADSHOT: True,
            PlayerDeath._REVENGE: False,
            DB._PLAYER_ID: player_id,
            DB._TEAM_L_ID: 3,
            DB._EVENT_NUMBER: 3,
            DB._ROUND: 1
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
        DB._GAME_ID: 1,
        DB._ITEM_ID: 6,
        PlayerHurt._DMG_HEALTH: 8,
        PlayerHurt._ARMOR: 95,
        PlayerHurt._HEALTH: 21,
        PlayerHurt._DMG_ARMOR: 4,
        PlayerHurt._HITGROUP: 2,
        DB._PLAYER_ID: 5,
        DB._ATTACKER_ID: 6,
        DB._TEAM_L_ID: 3,
        DB._EVENT_NUMBER: 1,
        DB._ROUND: 1
    }

    event = PlayerHurt()
    event.build_event(1, event_data, 1, 1)
    TestCase().assertDictEqual(event.rs, rs)
    assert event.data_set == [event.rs]
    assert event._TABLE_NAME == EventTypes.PLAYER_HURT


@patch.object(PlayerHurt, 'connect')
@patch.object(PlayerHurt, 'close')
def test_player_hurt_insert(connect_patch, close_path,
                            game_id, player_id, db_conn, db_cur, attacker_id):
    rs = [
        {
            DB._GAME_ID: game_id,
            DB._ITEM_ID: 6,
            PlayerHurt._DMG_HEALTH: 8,
            PlayerHurt._ARMOR: 95,
            PlayerHurt._HEALTH: 21,
            PlayerHurt._DMG_ARMOR: 4,
            PlayerHurt._HITGROUP: 2,
            DB._PLAYER_ID: player_id,
            DB._ATTACKER_ID: attacker_id,
            DB._TEAM_L_ID: 3,
            DB._EVENT_NUMBER: 1,
            DB._ROUND: 1
        },
        {
            DB._GAME_ID: game_id,
            DB._ITEM_ID: 6,
            PlayerHurt._DMG_HEALTH: 8,
            PlayerHurt._ARMOR: 95,
            PlayerHurt._HEALTH: 21,
            PlayerHurt._DMG_ARMOR: 4,
            PlayerHurt._HITGROUP: 2,
            DB._PLAYER_ID: player_id,
            DB._ATTACKER_ID: attacker_id,
            DB._TEAM_L_ID: 3,
            DB._EVENT_NUMBER: 2,
            DB._ROUND: 1
        },
        {
            DB._GAME_ID: game_id,
            DB._ITEM_ID: None,
            PlayerHurt._DMG_HEALTH: 8,
            PlayerHurt._ARMOR: 95,
            PlayerHurt._HEALTH: 21,
            PlayerHurt._DMG_ARMOR: 4,
            PlayerHurt._HITGROUP: 2,
            DB._PLAYER_ID: player_id,
            DB._ATTACKER_ID: None,
            DB._TEAM_L_ID: 3,
            DB._EVENT_NUMBER: 3,
            DB._ROUND: 1
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
        DB._GAME_ID: 1,
        DB._PLAYER_ID: 6,
        PlayerFallDamage._DAMAGE: 0.297619,
        DB._TEAM_L_ID: 3,
        DB._EVENT_NUMBER: 1,
        DB._ROUND: 1
    }

    event = PlayerFallDamage()
    event.build_event(1, event_data, 1, 1)
    TestCase().assertDictEqual(event.rs, rs)
    assert event.data_set == [event.rs]
    assert event._TABLE_NAME == EventTypes.PLAYER_FALLDAMAGE


@patch.object(PlayerFallDamage, 'connect')
@patch.object(PlayerFallDamage, 'close')
def test_player_falldamage_insert(connect_patch, close_path,
                                  game_id, player_id, db_conn, db_cur):
    rs = [
        {
            DB._GAME_ID: game_id,
            DB._PLAYER_ID: player_id,
            PlayerFallDamage._DAMAGE: 0.297619,
            DB._TEAM_L_ID: 3,
            DB._EVENT_NUMBER: 1,
            DB._ROUND: 1
        },
        {
            DB._GAME_ID: game_id,
            DB._PLAYER_ID: player_id,
            PlayerFallDamage._DAMAGE: 0.297619,
            DB._TEAM_L_ID: 3,
            DB._EVENT_NUMBER: 2,
            DB._ROUND: 1
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
        DB._GAME_ID: 1,
        DB._ITEM_ID: 28,
        WeaponFire._SILENCED: True,
        DB._PLAYER_ID: 8,
        DB._TEAM_L_ID: 3,
        DB._EVENT_NUMBER: 1,
        DB._ROUND: 1
    }
    event = WeaponFire()
    event.build_event(1, data, 1, 1)
    TestCase().assertDictEqual(event.rs, rs)
    assert event.data_set == [event.rs]
    assert event._TABLE_NAME == EventTypes.WEAPON_FIRE


@patch.object(WeaponFire, 'connect')
@patch.object(WeaponFire, 'close')
def test_weapon_fire_insert(connect_patch, close_path,
                            game_id, player_id, db_conn, db_cur):
    rs = [
        {
            DB._GAME_ID: game_id,
            DB._ITEM_ID: 28,
            WeaponFire._SILENCED: True,
            DB._PLAYER_ID: player_id,
            DB._TEAM_L_ID: 3,
            DB._EVENT_NUMBER: 1,
            DB._ROUND: 1
        },
        {
            DB._GAME_ID: game_id,
            DB._ITEM_ID: 28,
            WeaponFire._SILENCED: True,
            DB._PLAYER_ID: player_id,
            DB._TEAM_L_ID: 3,
            DB._EVENT_NUMBER: 2,
            DB._ROUND: 1
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
        DB._GAME_ID: 1,
        DB._PLAYER_ID: 2,
        DB._ITEM_ID: 42,
        DB._TEAM_L_ID: 3,
        DB._EVENT_NUMBER: 1,
        DB._ROUND: 1
    }
    event = ItemEquip()
    event.build_event(1, data, 1, 1)
    TestCase().assertDictEqual(event.rs, rs)
    assert event.data_set == [event.rs]
    assert event._TABLE_NAME == EventTypes.ITEM_EQUIP


@patch.object(ItemEquip, 'connect')
@patch.object(ItemEquip, 'close')
def test_item_equip_insert(connect_patch, close_path,
                           game_id, player_id, db_conn, db_cur):
    rs = [
        {
            DB._GAME_ID: game_id,
            DB._PLAYER_ID: player_id,
            DB._ITEM_ID: 42,
            DB._TEAM_L_ID: 3,
            DB._EVENT_NUMBER: 1,
            DB._ROUND: 1
        },
        {
            DB._GAME_ID: game_id,
            DB._PLAYER_ID: player_id,
            DB._ITEM_ID: 42,
            DB._TEAM_L_ID: 3,
            DB._EVENT_NUMBER: 2,
            DB._ROUND: 1
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
        DB._GAME_ID: 1,
        BombPlanted._SITE: 301,
        DB._PLAYER_ID: 4,
        DB._TEAM_L_ID: 3,
        DB._EVENT_NUMBER: 1,
        DB._ROUND: 1
    }

    event = BombPlanted()
    event.build_event(1, event_data, 1, 1)
    TestCase().assertDictEqual(event.rs, rs)
    assert event.data_set == [event.rs]
    assert event._TABLE_NAME == EventTypes.BOMB_PLANTED


@patch.object(BombPlanted, 'connect')
@patch.object(BombPlanted, 'close')
def test_bomb_planted_insert(connect_patch, close_path,
                             game_id, player_id, db_conn, db_cur):
    rs = [
        {
            DB._GAME_ID: game_id,
            BombPlanted._SITE: 301,
            DB._PLAYER_ID: player_id,
            DB._TEAM_L_ID: 3,
            DB._EVENT_NUMBER: 1,
            DB._ROUND: 1
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
        DB._GAME_ID: 1,
        BombPlanted._SITE: 302,
        DB._PLAYER_ID: 1,
        DB._TEAM_L_ID: 3,
        DB._EVENT_NUMBER: 1,
        DB._ROUND: 1
    }

    event = BombDefused()
    event.build_event(1, event_data, 1, 1)
    TestCase().assertDictEqual(event.rs, rs)
    assert event.data_set == [event.rs]
    assert event._TABLE_NAME == EventTypes.BOMB_DEFUSED


@patch.object(BombDefused, 'connect')
@patch.object(BombDefused, 'close')
def test_bomb_defused_insert(connect_patch, close_path,
                             game_id, player_id, db_conn, db_cur):
    rs = [
        {
            DB._GAME_ID: game_id,
            BombPlanted._SITE: 302,
            DB._PLAYER_ID: player_id,
            DB._TEAM_L_ID: 3,
            DB._EVENT_NUMBER: 1,
            DB._ROUND: 1
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
        DB._GAME_ID: 1,
        RoundStart._TIMELIMIT: 999,
        DB._EVENT_NUMBER: 1,
        DB._ROUND: 1
    }

    event = RoundStart()
    event.build_event(1, event_data, 1, 1)
    TestCase().assertDictEqual(event.rs, rs)
    assert event.data_set == [event.rs]
    assert event._TABLE_NAME == EventTypes.ROUND_START


@patch.object(RoundStart, 'connect')
@patch.object(RoundStart, 'close')
def test_round_start_insert(connect_patch, close_path,
                            game_id, db_conn, db_cur):
    rs = [
        {
            DB._GAME_ID: game_id,
            RoundStart._TIMELIMIT: 999,
            DB._EVENT_NUMBER: 1,
            DB._ROUND: 1
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
        DB._GAME_ID: 1,
        RoundEnd._REASON: 9,
        RoundEnd._MESSAGE: "#SFUI_Notice_Terrorists_Win",
        RoundEnd._TEAM_L_ID: 2,
        DB._EVENT_NUMBER: 1,
        DB._ROUND: 1
    }
    event = RoundEnd()
    event.build_event(1, data, 1, 1)
    TestCase().assertDictEqual(event.rs, rs)
    assert event.data_set == [event.rs]
    assert event._TABLE_NAME == EventTypes.ROUND_END


@patch.object(RoundEnd, 'connect')
@patch.object(RoundEnd, 'close')
def test_round_end_insert(connect_patch, close_path,
                          game_id, db_conn, db_cur):
    rs = [
        {
            DB._GAME_ID: game_id,
            RoundEnd._REASON: 9,
            RoundEnd._MESSAGE: "#SFUI_Notice_Terrorists_Win",
            RoundEnd._TEAM_L_ID: 2,
            DB._EVENT_NUMBER: 1,
            DB._ROUND: 1
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
        DB._GAME_ID: 1,
        RoundEnd._REASON: 3,
        DB._PLAYER_ID: 1,
        DB._TEAM_L_ID: 3,
        DB._EVENT_NUMBER: 1,
        DB._ROUND: 1
    }

    event = RoundMVP()
    event.build_event(1, event_data, 1, 1)
    TestCase().assertDictEqual(event.rs, rs)
    assert event.data_set == [event.rs]
    assert event._TABLE_NAME == EventTypes.ROUND_MVP


@patch.object(RoundMVP, 'connect')
@patch.object(RoundMVP, 'close')
def test_round_mvp_insert(connect_patch, close_path,
                          game_id, player_id, db_conn, db_cur):
    rs = [
        {
            DB._GAME_ID: game_id,
            RoundEnd._REASON: 3,
            DB._PLAYER_ID: player_id,
            DB._TEAM_L_ID: 3,
            DB._EVENT_NUMBER: 1,
            DB._ROUND: 1
        }
    ]

    event = RoundMVP()
    event.conn = db_conn
    event.cur = db_cur
    event.data_set = rs
    event.insert(event._TABLE_NAME, rs)
    connect_patch.assert_called_once()
    close_path.assert_called_once()


def test_to_literal(game_id, player_id):
    rs = {
        DB._GAME_ID: game_id,
        RoundEnd._REASON: 3,
        DB._PLAYER_ID: player_id,
        DB._TEAM_L_ID: 3,
        DB._EVENT_NUMBER: 1,
        DB._ROUND: 1
    }
    literal_rs = {
        'game_id': game_id,
        'reason': 3,
        'player_id': player_id,
        'team_l_id': 3,
        'event_number': 1,
        'round': 1
    }

    event = RoundMVP()
    event.rs = rs
    output = event.to_literal()
    TestCase().assertDictEqual(output, literal_rs)


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
