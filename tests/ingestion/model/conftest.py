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
