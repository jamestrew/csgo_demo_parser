# import json
# import os
# from unittest.mock import patch

# import pytest

# from csgo_analysis.ingestion.models import Player


# @pytest.fixture
# def player_info():
#     player_info = {
#         13: {
#             'game_id': 1,
#             'team_l_id': 1,
#             'xuid': 76561197960512598,
#             'player_name': 'Chris P. Bacon',
#             'userID': 13
#         },
#         11: {
#             'game_id': 1,
#             'team_l_id': 1,
#             'xuid': 76561198026942816,
#             'player_name': 'paper girlfriend',
#             'userID': 11
#         }
#     }
#     return player_info


# def test_get_userid(player_info):
#     p = Player(game_id=1, data='')
#     player = player_info.get(11)

#     player_id = p.get_full_id(player)
#     assert player_id == 'paper girlfriend (id:11)'


# @patch.object(Player, 'insert_prep')
# def test_create_players(
#     insert_patch,
#     players_data,
#     new_players_data,
#     created_players
# ):
#     p = Player(game_id=1, data=players_data)
#     p.create_players()

#     assert p.players == created_players
#     assert p.data == new_players_data
#     insert_patch.assert_called_once()


# def test_get_full_id():
#     p = Player(1, None)
#     player = {
#         "game_id": 1,
#         "xuid": 76561197960512598,
#         "player_name": "Chris P. Bacon",
#         "userID": 3,
#         "team_l_id": 1
#     }
#     full_id = p.get_full_id(player)
#     assert full_id == "Chris P. Bacon (id:3)"


# @patch.object(Player, 'insert')
# def test_insert_prep(insert_patch, created_players):
#     p = Player(1, None)
#     p.players = created_players

#     p.insert_prep()
#     fields = [
#         {'game_id': 1, 'xuid': 76561197960512598, 'player_name': "Chris P. Bacon", 'team_l_id': 1},
#         {'game_id': 1, 'xuid': 76561197964398021, 'player_name': "Mike", 'team_l_id': 1},
#         {'game_id': 1, 'xuid': 76561198133822308, 'player_name': "digga", 'team_l_id': 2},
#     ]
#     insert_patch.assert_called_with(p._TABLE_NAME, fields, True)


# @pytest.mark.parametrize(
#     'player_fullid, output', [
#         ("Chris P. Bacon (id:3)", 76561197960512598),
#         ("Invalid Player", None)
#     ]
# )
# def test_get_player_xuid(player_fullid, output, created_players):
#     p = Player(1, None)
#     p.players = created_players
#     player = p.get_player_xuid(player_fullid)
#     assert player == output


# @patch.object(Player, 'insert_prep')
# @pytest.mark.data_collection  # noqa
# def test_pre_event_data_collection(insert_patch, data_json):
#     p = Player(1, data_json)
#     output = p.create_players()
#     insert_patch.assert_called_once()

#     save_path = os.path.join('tests', 'ingestion', 'fixtures', 'pre_event.json')
#     with open(save_path, 'w') as json_file:
#         json.dump(output, json_file)
