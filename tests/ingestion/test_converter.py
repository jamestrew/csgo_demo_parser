from csgo_analysis.ingestion.converter import JsonConverter


def test_begin_new_match(data_txt_begin, data_json_begin):
    output = JsonConverter.convert(data_txt_begin, None, False)
    assert output == data_json_begin


def test_n_unicode_match(unicode_txt, unicode_json):
    output = JsonConverter.convert(unicode_txt, None, False)
    assert output == unicode_json


def test_colon_in_name(colon_in_name_txt):
    answer = [
        {
            "player_info": {
                "guid": "BOT",
                "xuid": "0",
                "userID": "17",
                "ishltv": "0",
                "filesDownloaded": "0",
                "friendsID": "4",
                "updating": "true",
                "friendsName": " ",
                "name": "Harvey",
                "fakeplayer": "1"
            }
        },
        {'player_spawn': {'userid': 'BVS: Shady-E-E\'s (id:11)', 'teamnum': '0'}},
        {
            "weapon_fire": {
                "weapon": "weapon_flashbang",
                "team": "T",
                "silenced": "0",
                "userid": "Maku18 (id:6)"
            }
        }
    ]
    output = JsonConverter.convert(colon_in_name_txt, None, False)
    assert output == answer
