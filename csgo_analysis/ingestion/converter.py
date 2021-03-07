import json
import re
from csgo_analysis.ingestion.const import EventTypes


class JsonConverter:

    PLAYER_P = r'player info'
    PLAYER_R = r'player_info'

    MAIN_KEY_P = r'([a-z_]+)\n({\n)'
    MAIN_KEY_R = r'{"\1": \2'

    INNER_KEY_P = r' ([0-9a-zA-Z_]+):'
    INNER_KEY_R = r'"\1":'

    DETAILS_KEY_P = r'  (position|facing):.+\n'
    TEAM_KEY_P = r' ( team: .+\n)'
    TEAM_KEY_R = r'\1'

    INNER_VAL_P = r': ?([#\-0-9a-zA-Z\. _\(\):]+)'
    INNER_VAL_R = r': "\1", '

    END_BRACKET_P = r'}'
    END_BRACKET_R = r'}}, '

    MIDDLE_P = r'},\n(.+)\n{'
    MIDDLE_R = r'}, {'

    TRAIL_COMMA_P = r', }}, '
    TRAIL_COMMA_R = r'}}, '
    TRAIL_COMMA_P2 = r'", {"'
    TRAIL_COMMA_R2 = r'"}}, {"'

    NEW_LINE_P = r'\n'
    BLANK = r''

    JUNK_P = r'}\n(.+\n(?!{))+(.+\n(?={))*?'
    JUNK_R = r'}\n'

    ANNOUNCEMENTS = r'[a-z_]+\n{\n}\n'

    NULL_P = r':  '
    NULL_R = r': "None"'
    TIGHT_NULL_P = r':\n'
    TIGHT_NULL_R = r':  \n'

    STOP_R = r'stophere\nplayer_info'
    FIRST_TABLE_P = r'^.+(stophere)$'

    EVENT_P = r'event\n{\n( [a-zA-Z0-9: \.\(\)_#\-]+\n)+}'

    @classmethod
    def convert(cls, txt, file_path, save=False):
        """Convert txt demo data into Python object (list of dict).

        Parameters
        ----------
        txt : str
            txt demo data
        file_path : str
            txt_demo data path
        save : bool, optional
            Option to save converted data as json, by default False

        Returns
        -------
        list
            game data object (list of dict)
        """

        txt = re.sub(cls.PLAYER_P, cls.PLAYER_R, txt)
        txt = re.sub(cls.PLAYER_R, cls.STOP_R, txt, 1)

        flags = re.DOTALL | re.MULTILINE
        first_table = re.match(cls.FIRST_TABLE_P, txt, flags)
        txt = txt.replace(first_table[0], '')

        txt = re.sub(cls.JUNK_P, cls.JUNK_R, txt)
        txt = re.sub(cls.ANNOUNCEMENTS, cls.BLANK, txt)
        txt = re.sub(cls.DETAILS_KEY_P, cls.BLANK, txt)
        txt = re.sub(cls.TEAM_KEY_P, cls.TEAM_KEY_R, txt)

        for event in EventTypes.UNNECESSARY_DATA:
            pattern = cls.EVENT_P.replace('event', event)
            txt = re.sub(pattern, cls.BLANK, txt)

        txt = re.sub(cls.TIGHT_NULL_P, cls.TIGHT_NULL_R, txt)
        txt = re.sub(cls.INNER_KEY_P, cls.INNER_KEY_R, txt)
        txt = re.sub(cls.INNER_VAL_P, cls.INNER_VAL_R, txt)
        txt = re.sub(cls.END_BRACKET_P, cls.END_BRACKET_R, txt)
        txt = re.sub(cls.MAIN_KEY_P, cls.MAIN_KEY_R, txt)
        txt = re.sub(cls.MIDDLE_P, cls.MIDDLE_R, txt)
        txt = re.sub(cls.NEW_LINE_P, cls.BLANK, txt)
        txt = re.sub(cls.TRAIL_COMMA_P, cls.TRAIL_COMMA_R, txt)
        txt = re.sub(cls.TRAIL_COMMA_P2, cls.TRAIL_COMMA_R2, txt)
        txt = f'[{txt.strip()[:-1]}]'  # convert to array

        data = json.loads(txt)

        if save:
            file_path = file_path.replace('.txt', '.json')
            with open(file_path, 'w') as jsonfile:
                json.dump(data, jsonfile)

        return data
