from unittest.mock import patch
from csgo_analysis.ingestion.models import Player
import pytest


@pytest.fixture
def player_info():
    player_info = {
        13: {
            'game_id': 1,
            'team_l_id': 1,
            'xuid': 76561197960512598,
            'name': 'Chris P. Bacon',
            'userID': 13
        },
        11: {
            'game_id': 1,
            'team_l_id': 1,
            'xuid': 76561198026942816,
            'name': 'paper girlfriend',
            'userID': 11
        }
    }
    return player_info


def test_get_userid(player_info):
    p = Player(game_id=1, data='')
    player = player_info.get(11)

    player_id = p.get_full_id(player)
    assert player_id == 'paper girlfriend (id:11)'


@patch.object(Player, 'insert_prep')
def test_create_players(insert_patch, players_data, new_players_data):
    p = Player(game_id=1, data=players_data)
    p.create_players()

    created_players = {
        "Chris P. Bacon (id:3)": {
            "game_id": 1,
            "xuid": 76561197960512598,
            "name": "Chris P. Bacon",
            "userID": 3,
            "team_l_id": 2
        },
        "Mike (id:4)": {
            "game_id": 1,
            "xuid": 76561197964398021,
            "name": "Mike",
            "userID": 4,
            "team_l_id": 2
        },
        "digga (id:5)": {
            "game_id": 1,
            "xuid": 76561198133822308,
            "name": "digga",
            "userID": 5,
            "team_l_id": 3
        },
        "digga (id:12)": {
            "game_id": 1,
            "xuid": 76561198133822308,
            "name": "digga",
            "userID": 12,
            "team_l_id": 3
        }
    }

    assert p.players == created_players
    assert p.data == new_players_data
    insert_patch.assert_called_once()
