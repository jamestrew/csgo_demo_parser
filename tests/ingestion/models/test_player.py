from unittest.mock import patch, call

import pytest
from psycopg2._psycopg import TimestampFromTicks
from csgo_analysis.ingestion.models import Player


@pytest.fixture
def player_info():
    player_info = {
        13: {
            Player._GAME_ID: 1,
            Player._TEAM_L_ID: 1,
            Player._XUID: '76561197960512598',
            Player._PLAYER_NAME: 'Chris P. Bacon'
        },
        11: {
            Player._GAME_ID: 1,
            Player._TEAM_L_ID: 1,
            Player._XUID: '76561198026942816',
            Player._PLAYER_NAME: 'paper girlfriend'
        }
    }
    return player_info


@pytest.fixture
def user_ids():
    return {
        '76561197960512598': 1,
        '76561197964398021': 2,
        '76561198133822308': 3
    }


@pytest.fixture
def name_id():
    return {
        "Chris P. Bacon (id:3)": 1,
        "Mike (id:4)": 2,
        "digga (id:5)": 3,
        "digga (id:12)": 3
    }


def test_get_userid(player_info):
    p = Player(game_id=1, data='')
    player = player_info.get(11)

    player_id = p._get_full_id(player, 11)
    assert player_id == 'paper girlfriend (id:11)'


@patch.object(Player, 'insert')
def test_create_players(
    insert_patch,
    players_data,
    new_players_data,
    created_players
):
    insert_patch.side_effect = [1, 2, 3]
    p = Player(game_id=1, data=players_data)
    p.create_players()

    assert p.players == created_players
    assert p.data == new_players_data
    assert insert_patch.call_count == 3


def test_get_full_id():
    p = Player(1, None)
    player = {
        Player._GAME_ID: 1,
        Player._XUID: 76561197960512598,
        Player._PLAYER_NAME: "Chris P. Bacon",
        Player._TEAM_L_ID: 1
    }
    full_id = p._get_full_id(player, 3)
    assert full_id == "Chris P. Bacon (id:3)"


@patch.object(Player, 'insert')
def test_insert_prep(insert_patch, created_players, name_id, user_ids):
    insert_patch.side_effect = [1, 2, 3]
    p = Player(1, None)
    created_players['digga (id:12)'][Player._TEAM_L_ID] = 0  # unknown
    p.players = created_players

    p._insert_prep()
    fields = [
        {
            Player._GAME_ID: 1,
            Player._XUID: '76561197960512598',
            Player._PLAYER_NAME: "Chris P. Bacon",
            Player._TEAM_L_ID: 2
        },
        {
            Player._GAME_ID: 1,
            Player._XUID: '76561197964398021',
            Player._PLAYER_NAME: "Mike",
            Player._TEAM_L_ID: 2
        },
        {
            Player._GAME_ID: 1,
            Player._XUID: '76561198133822308',
            Player._PLAYER_NAME: "digga",
            Player._TEAM_L_ID: 3
        },
    ]

    args = [
        call(p._TABLE_NAME, fields[0], True),
        call(p._TABLE_NAME, fields[1], True),
        call(p._TABLE_NAME, fields[2], True)
    ]
    insert_patch.assert_has_calls(args)
    assert p.userid_id_dict == name_id
    assert p.xuid_id_dict == user_ids


def test_player_list(user_ids):
    p = Player(None, None)
    p.xuid_id_dict = user_ids

    assert p.player_list == [1, 2, 3]


@pytest.mark.ingestion  # noqa
@patch.object(Player, 'connect')
@patch.object(Player, 'close')
def test_player_ingestion_insert(p_connect_p, p_close_p, db_cur, db_conn, players_data):
    insert_str = "INSERT INTO game (share_code, match_time, match_duration, map_l_id, final_score_two, final_score_three) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    val = ['CSGO-xQKYC-4Nbc4-h43V2-Jc66v-EWtrT', TimestampFromTicks(1613364114), 2319, 1, 10, 16]

    db_cur.execute(insert_str, val)
    return_id = db_cur.fetchone()

    p = Player(return_id[0], players_data)
    p.cur = db_cur
    p.conn = db_conn
    p.create_players()

    db_cur.execute("SELECT xuid FROM player WHERE game_id = (%s)", (return_id, ))
    players = [xuid[0] for xuid in db_cur.fetchall()]

    assert set(players) == set([76561197960512598, 76561197964398021, 76561198133822308])

# @pytest.mark.data_collection
# @patch.object(Player, 'insert')
# def test_pre_event_data_collection(insert_patch, data_json):
#     import json
#     import os
#     insert_patch.side_effect = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     p = Player(1, data_json)
#     output = p.create_players()

#     save_path = os.path.join('tests', 'ingestion', 'fixtures', 'inferno.json')
#     with open(save_path, 'w') as json_file:
#         json.dump(output, json_file)
