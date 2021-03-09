from unittest.mock import patch, call

import pytest

from csgo_analysis.ingestion.models import Player


@pytest.fixture
def player_info():
    player_info = {
        13: {
            'game_id': 1,
            'team_l_id': 1,
            'xuid': 76561197960512598,
            'player_name': 'Chris P. Bacon'
        },
        11: {
            'game_id': 1,
            'team_l_id': 1,
            'xuid': 76561198026942816,
            'player_name': 'paper girlfriend'
        }
    }
    return player_info


@pytest.fixture
def user_ids():
    return {
        76561197960512598: 1,
        76561197964398021: 2,
        76561198133822308: 3
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

    player_id = p.get_full_id(player, 11)
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
        "game_id": 1,
        "xuid": 76561197960512598,
        "player_name": "Chris P. Bacon",
        "team_l_id": 1
    }
    full_id = p.get_full_id(player, 3)
    assert full_id == "Chris P. Bacon (id:3)"


@patch.object(Player, 'insert')
def test_insert_prep(insert_patch, created_players, name_id, user_ids):
    insert_patch.side_effect = [1, 2, 3]
    p = Player(1, None)
    created_players['digga (id:12)']['team_l_id'] = 999  # unknown
    p.players = created_players

    p.insert_prep()
    fields = [
        {
            'game_id': 1,
            'xuid': 76561197960512598,
            'player_name': "Chris P. Bacon",
            'team_l_id': 1
        },
        {
            'game_id': 1,
            'xuid': 76561197964398021,
            'player_name': "Mike",
            'team_l_id': 1
        },
        {
            'game_id': 1,
            'xuid': 76561198133822308,
            'player_name': "digga",
            'team_l_id': 2
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
