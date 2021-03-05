import pytest


@pytest.fixture
def players_data():
    data = [
        {
            "player_info": {
                "adding": "true",
                "xuid": "76561197960512598",
                "name": "Chris P. Bacon",
                "userID": "3",
                "guid": "STEAM_1:0:123435",
                "friendsID": "246870",
                "friendsName": "None",
                "fakeplayer": "0",
                "ishltv": "0",
                "filesDownloaded": "0"
            }
        },
        {
            "player_info": {
                "adding": "true",
                "xuid": "76561197964398021",
                "name": "Mike",
                "userID": "4",
                "guid": "STEAM_1:1:2066146",
                "friendsID": "4132293",
                "friendsName": "None",
                "fakeplayer": "0",
                "ishltv": "0",
                "filesDownloaded": "0"
            }
        },
        {
            "player_info": {
                "adding": "true",
                "xuid": "76561198133822308",
                "name": "digga",
                "userID": "5",
                "guid": "STEAM_1:0:86778290",
                "friendsID": "173556580",
                "friendsName": "None",
                "fakeplayer": "0",
                "ishltv": "0",
                "filesDownloaded": "0"
            }
        },
        {"player_spawn": {"userid": "Chris P. Bacon (id:3)", "teamnum": "0 "}},
        {"player_spawn": {"userid": "Chris P. Bacon (id:3)", "teamnum": "2 "}},
        {"player_spawn": {"userid": "Chris P. Bacon (id:3)", "teamnum": "2 "}},
        {"player_spawn": {"userid": "Mike (id:4)", "teamnum": "0 "}},
        {"player_spawn": {"userid": "digga (id:5)", "teamnum": "0 "}},
        {"player_spawn": {"userid": "Mike (id:4)", "teamnum": "2 "}},
        {"player_spawn": {"userid": "digga (id:5)", "teamnum": "3 "}},
        {"player_spawn": {"userid": "Chris P. Bacon (id:3)", "teamnum": "2 "}},
        {
            "player_info": {
                "adding": "true",
                "xuid": "76561198133822308",
                "name": "digga",
                "userID": "12",
                "guid": "STEAM_1:0:86778290",
                "friendsID": "173556580",
                "friendsName": "None",
                "fakeplayer": "0",
                "ishltv": "0",
                "filesDownloaded": "0"
            }
        },
        {"player_spawn": {"userid": "digga (id:12)", "teamnum": "3 "}},
        {
            "weapon_fire": {
                "userid": "Chris P. Bacon (id:3)",
                "weapon": "weapon_ak47 ",
                "silenced": "0 "
            }
        },
        {
            "player_hurt": {
                "userid": "Chris P. Bacon (id:3)",
                "attacker": "digga (id:12)",
                "health": "0 ",
                "armor": "36 ",
                "weapon": "hkp2000 ",
                "dmg_health": "63 ",
                "dmg_armor": "31 ",
                "hitgroup": "1 "
            }
        },
        {
            "player_death": {
                "userid": "Chris P. Bacon (id:3)",
                "attacker": "digga (id:12)",
                "assister": "0 ",
                "assistedflash": "0 ",
                "weapon": "usp_silencer ",
                "weapon_itemid": "4348835034 ",
                "weapon_fauxitemid": "17293822569118171197 ",
                "weapon_originalowner_xuid": "76561197974666857 ",
                "headshot": "1 ",
                "dominated": "0 ",
                "revenge": "0 ",
                "wipe": "0 ",
                "penetrated": "0 ",
                "noreplay": "0 "
            }
        },
        {
            "player_death": {
                "userid": "Chris P. Bacon (id:3)",
                "attacker": "digga (id:12)",
                "assister": "Mike (id:4)",
                "assistedflash": "0 ",
                "weapon": "usp_silencer ",
                "weapon_itemid": "4348835034 ",
                "weapon_fauxitemid": "17293822569118171197 ",
                "weapon_originalowner_xuid": "76561197974666857 ",
                "headshot": "1 ",
                "dominated": "0 ",
                "revenge": "0 ",
                "wipe": "0 ",
                "penetrated": "0 ",
                "noreplay": "0 "
            }
        },
    ]

    return data


@pytest.fixture
def created_players():
    return {
        "Chris P. Bacon (id:3)": {
            "game_id": 1,
            "xuid": 76561197960512598,
            "name": "Chris P. Bacon",
            "userID": 3,
            "team_l_id": 1
        },
        "Mike (id:4)": {
            "game_id": 1,
            "xuid": 76561197964398021,
            "name": "Mike",
            "userID": 4,
            "team_l_id": 1
        },
        "digga (id:5)": {
            "game_id": 1,
            "xuid": 76561198133822308,
            "name": "digga",
            "userID": 5,
            "team_l_id": 2
        },
        "digga (id:12)": {
            "game_id": 1,
            "xuid": 76561198133822308,
            "name": "digga",
            "userID": 12,
            "team_l_id": 2
        }
    }


@pytest.fixture
def new_players_data():
    data = [
        {
            "player_info": {
                "adding": "true",
                "xuid": "76561197960512598",
                "name": "Chris P. Bacon",
                "userID": "3",
                "guid": "STEAM_1:0:123435",
                "friendsID": "246870",
                "friendsName": "None",
                "fakeplayer": "0",
                "ishltv": "0",
                "filesDownloaded": "0"
            }
        },
        {
            "player_info": {
                "adding": "true",
                "xuid": "76561197964398021",
                "name": "Mike",
                "userID": "4",
                "guid": "STEAM_1:1:2066146",
                "friendsID": "4132293",
                "friendsName": "None",
                "fakeplayer": "0",
                "ishltv": "0",
                "filesDownloaded": "0"
            }
        },
        {
            "player_info": {
                "adding": "true",
                "xuid": "76561198133822308",
                "name": "digga",
                "userID": "5",
                "guid": "STEAM_1:0:86778290",
                "friendsID": "173556580",
                "friendsName": "None",
                "fakeplayer": "0",
                "ishltv": "0",
                "filesDownloaded": "0"
            }
        },
        {"player_spawn": {"userid": "Chris P. Bacon (id:3)", "teamnum": "0 "}},
        {"player_spawn": {"userid": "Chris P. Bacon (id:3)", "teamnum": "2 "}},
        {"player_spawn": {"userid": "Chris P. Bacon (id:3)", "teamnum": "2 "}},
        {"player_spawn": {"userid": "Mike (id:4)", "teamnum": "0 "}},
        {"player_spawn": {"userid": "digga (id:5)", "teamnum": "0 "}},
        {"player_spawn": {"userid": "Mike (id:4)", "teamnum": "2 "}},
        {"player_spawn": {"userid": "digga (id:5)", "teamnum": "3 "}},
        {"player_spawn": {"userid": "Chris P. Bacon (id:3)", "teamnum": "2 "}},
        {
            "player_info": {
                "adding": "true",
                "xuid": "76561198133822308",
                "name": "digga",
                "userID": "12",
                "guid": "STEAM_1:0:86778290",
                "friendsID": "173556580",
                "friendsName": "None",
                "fakeplayer": "0",
                "ishltv": "0",
                "filesDownloaded": "0"
            }
        },
        {"player_spawn": {"userid": "digga (id:12)", "teamnum": "3 "}},
        {
            "weapon_fire": {
                "userid": 76561197960512598,
                "weapon": "weapon_ak47 ",
                "silenced": "0 "
            }
        },
        {
            "player_hurt": {
                "userid": 76561197960512598,
                "attacker": 76561198133822308,
                "health": "0 ",
                "armor": "36 ",
                "weapon": "hkp2000 ",
                "dmg_health": "63 ",
                "dmg_armor": "31 ",
                "hitgroup": "1 "
            }
        },
        {
            "player_death": {
                "userid": 76561197960512598,
                "attacker": 76561198133822308,
                "assister": "0 ",
                "assistedflash": "0 ",
                "weapon": "usp_silencer ",
                "weapon_itemid": "4348835034 ",
                "weapon_fauxitemid": "17293822569118171197 ",
                "weapon_originalowner_xuid": "76561197974666857 ",
                "headshot": "1 ",
                "dominated": "0 ",
                "revenge": "0 ",
                "wipe": "0 ",
                "penetrated": "0 ",
                "noreplay": "0 "
            }
        },
        {
            "player_death": {
                "userid": 76561197960512598,
                "attacker": 76561198133822308,
                "assister": 76561197964398021,
                "assistedflash": "0 ",
                "weapon": "usp_silencer ",
                "weapon_itemid": "4348835034 ",
                "weapon_fauxitemid": "17293822569118171197 ",
                "weapon_originalowner_xuid": "76561197974666857 ",
                "headshot": "1 ",
                "dominated": "0 ",
                "revenge": "0 ",
                "wipe": "0 ",
                "penetrated": "0 ",
                "noreplay": "0 "
            }
        },
    ]

    return data


@pytest.fixture
def event_dirty():
    return [
        {
            "round_start": {
                "timelimit": "999 ",
                "fraglimit": "0 ",
                "objective": "BOMB TARGET "
            }
        },
        {
            "item_pickup": {
                "userid": 1234567890,
                "item": "glock ",
                "silent": "0 ",
                "defindex": "4 "
            }
        },
        {
            "item_remove": {
                "userid": 1234567890,
                "item": "knife ",
                "defindex": "42 "
            }
        },
        {
            "item_remove": {
                "userid": 1234567890,
                "item": "hkp2000 ",
                "defindex": "32 "
            }
        },
        {
            "player_death": {
                "userid": 1234567890,
                "attacker": 1234567890,
                "assister": 1234567890,
                "assistedflash": "0 ",
                "weapon": "ak47 ",
                "weapon_itemid": "19904080205 ",
                "weapon_fauxitemid": "17293822569149038599 ",
                "weapon_originalowner_xuid": "76561198128398569 ",
                "headshot": "1 ",
                "dominated": "0 ",
                "revenge": "0 ",
                "wipe": "0 ",
                "penetrated": "0 ",
                "noreplay": "0 ",
                "noscope": "0 ",
                "thrusmoke": "0 ",
                "attackerblind": "0 ",
                "distance": "21.734600 "
            }
        },
        {
            "player_blind": {
                "userid": 1234567890,
                "attacker": 1234567890,
                "entityid": "363 ",
                "blind_duration": "3.031657 "
            }
        },
        {
            "player_hurt": {
                "userid": 1234567890,
                "attacker": 1234567890,
                "health": "0 ",
                "armor": "95 ",
                "weapon": "glock ",
                "dmg_health": "71 ",
                "dmg_armor": "0 ",
                "hitgroup": "1 "
            }
        }, {
            "player_falldamage": {
                "userid": 1234567890,
                "damage": "0.297619 "
            }
        },
        {
            "round_mvp": {
                "userid": 1234567890,
                "reason": "1 ",
                "value": "0 ",
                "musickitmvps": "0 ",
                "nomusic": "0 "
            }
        },
        {
            "round_end": {
                "winner": "2 ",
                "reason": "9 ",
                "message": "#SFUI_Notice_Terrorists_Win ",
                "legacy": "0 ",
                "player_count": "10 ",
                "nomusic": "0 "
            }
        },
        {
            "weapon_fire": {
                "userid": 1234567890,
                "weapon": "weapon_glock ",
                "silenced": "0 "
            }
        },
        {
            "item_equip": {
                "userid": 1234567890,
                "item": "knife ",
                "defindex": "522 ",
                "canzoom": "0 ",
                "hassilencer": "0 ",
                "issilenced": "0 ",
                "hastracers": "0 ",
                "weptype": "0 ",
                "ispainted": "1 "
            }
        },
        {
            "item_remove": {
                "userid": 1234567890,
                "item": "glock ",
                "defindex": "4 "
            }
        },
        {
            "item_pickup": {
                "userid": 1234567890,
                "item": "hkp2000 ",
                "silent": "0 ",
                "defindex": "32 "
            }
        },
        {
            "round_start": {
                "timelimit": "115 ",
                "fraglimit": "0 ",
                "objective": "BOMB TARGET "
            }
        },
        {"bomb_planted": {"userid": 1234567890, "site": "301 "}},
        {"bomb_defused": {"userid": 1234567890, "site": "301 "}},
    ]


@pytest.fixture
def event_clean():
    return [
        {
            "round_start": {
                "game_id": 1,
                "timelimit": 999,
                "event_number": 1,
                "round": 1
            }
        },
        {
            "item_pickup": {
                "game_id": 1,
                "player_id": 1234567890,
                "item_id": 6,
                "silent": False,
                "event_number": 2,
                "round": 1
            }
        },
        {
            "item_remove": {
                "game_id": 1,
                "player_id": 1234567890,
                "item_id": 1,
                "event_number": 3,
                "round": 1
            }
        },
        {
            "item_remove": {
                "game_id": 1,
                "player_id": 1234567890,
                "item_id": 7,
                "event_number": 4,
                "round": 1
            }
        },
        {
            "player_death": {
                "game_id": 1,
                "player_id": 1234567890,
                "attacker_id": 1234567890,
                "assister_id": 1234567890,
                "assistedflash": False,
                "item_id": 25,
                "headshot": True,
                "dominated": False,
                "revenge": False,
                "wipe": False,
                "penetrated": False,
                "noscope": False,
                "thrusmoke": False,
                "attackerblind": False,
                "distance": 21.734600,
                "event_number": 5,
                "round": 1
            }
        },
        {
            "player_blind": {
                "game_id": 1,
                "player_id": 1234567890,
                "attacker_id": 1234567890,
                "blind_duration": 3.031657,
                "event_number": 6,
                "round": 1
            }
        },
        {
            "player_hurt": {
                "game_id": 1,
                "player_id": 1234567890,
                "attacker_id": 1234567890,
                "health": 0,
                "armor": 95,
                "item_id": 6,
                "dmg_health": 71,
                "dmg_armor": 0,
                "hitgroup": 1,
                "event_number": 7,
                "round": 1
            }
        }, {
            "player_falldamage": {
                "game_id": 1,
                "player_id": 1234567890,
                "damage": 0.297619,
                "event_number": 8,
                "round": 1
            }
        },
        {
            "round_mvp": {
                "game_id": 1,
                "player_id": 1234567890,
                "event_number": 9,
                "round": 1
            }
        },
        {
            "round_end": {
                "game_id": 1,
                "team_l_id": 1,
                "reason": 9,
                "message": "#SFUI_Notice_Terrorists_Win",
                "event_number": 10,
                "round": 1
            }
        },
        {
            "weapon_fire": {
                "game_id": 1,
                "player_id": 1234567890,
                "item_id": 6,
                "silenced": False,
                "event_number": 11,
                "round": 1
            }
        },
        {
            "item_equip": {
                "game_id": 1,
                "player_id": 1234567890,
                "item_id": 1,
                "event_number": 12,
                "round": 1
            }
        },
        {
            "item_remove": {
                "game_id": 1,
                "player_id": 1234567890,
                "event_number": 13,
                "round": 1
            }
        },
        {
            "item_pickup": {
                "game_id": 1,
                "player_id": 1234567890,
                "item_id": 7,
                "silent": False,
                "event_number": 14,
                "round": 1
            }
        },
        {
            "round_start": {
                "game_id": 1,
                "timelimit": 115,
                "event_number": 15,
                "round": 2
            }
        },
        {"bomb_planted": {"game_id": 1, "player_id": 1234567890, "site": 301,
                          "event_number": 16,
                          "round": 2}},
        {"bomb_defused": {"game_id": 1, "player_id": 1234567890, "site": 301,
                          "event_number": 2,
                          "round": 16}},
    ]
