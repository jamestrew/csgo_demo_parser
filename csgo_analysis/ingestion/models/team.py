

class Team:
    GOTV = 0
    T = 2
    CT = 3

    __TEAM_L = {
        'CT': CT,
        'T': T,
        'GOTV': GOTV
    }

    @classmethod
    def get_team_id(cls, team_name):
        return cls.__TEAM_L.get(team_name.strip())
