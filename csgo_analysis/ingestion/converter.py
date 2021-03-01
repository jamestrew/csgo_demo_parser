import json
import re
from csgo_analysis.ingestion.const import Events


class JsonConverter:

    player_p = r'player info'
    player_r = r'player_info'

    main_key_p = r'([a-z_]+)\n({\n)'
    main_key_r = r'{"\1": \2'

    inner_key_p = r' ([0-9a-zA-Z_]+):'
    inner_key_r = r'"\1":'

    inner_val_p = r': ?([#\-0-9a-zA-Z\. _\(\):]+)'
    inner_val_r = r': "\1", '

    end_bracket_p = r'}'
    end_bracket_r = r'}}, '

    middle_p = r'},\n(.+)\n{'
    middle_r = r'}, {'

    trailing_comma_p = r', }}, '
    trailing_comma_r = r'}}, '
    trailing_comma_p2 = r'", {"'
    trailing_comma_r2 = r'"}}, {"'

    new_line_p = r'\n'
    blank = r''

    junk_p = r'}\n(.+\n(?!{))+(.+\n(?={))*?'
    junk_r = r'}\n'

    announcements = r'[a-z_]+\n{\n}\n'

    null_p = r':  '
    null_r = r': "None"'
    tight_null_p = r':\n'
    tight_null_r = r':  \n'

    stop_r = r'stophere\nplayer_info'
    first_table_p = r'^.+(stophere)$'

    event_p = r'event\n{\n( [a-zA-Z0-9: \.\(\)_#\-]+\n)+}'

    def convert(self, txt, file_path, save=False):
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
        txt = re.sub(self.player_p, self.player_r, txt)
        txt = re.sub(self.player_r, self.stop_r, txt, 1)

        first_table = re.match(self.first_table_p, txt, re.DOTALL | re.MULTILINE)
        txt = txt.replace(first_table[0], '')

        txt = re.sub(self.junk_p, self.junk_r, txt)
        txt = re.sub(self.announcements, self.blank, txt)

        for event in Events.UNNECESSARY_DATA:
            pattern = self.event_p.replace('event', event)
            txt = re.sub(pattern, self.blank, txt)

        save_path = file_path.replace('.txt', '_events.txt')
        with open(save_path, 'w') as file:
            file.write(txt)

        txt = re.sub(self.tight_null_p, self.tight_null_r, txt)
        txt = re.sub(self.inner_key_p, self.inner_key_r, txt)
        txt = re.sub(self.inner_val_p, self.inner_val_r, txt)
        txt = re.sub(self.end_bracket_p, self.end_bracket_r, txt)
        txt = re.sub(self.main_key_p, self.main_key_r, txt)
        txt = re.sub(self.middle_p, self.middle_r, txt)
        txt = re.sub(self.new_line_p, self.blank, txt)
        txt = re.sub(self.trailing_comma_p, self.trailing_comma_r, txt)
        txt = re.sub(self.trailing_comma_p2, self.trailing_comma_r2, txt)
        txt = f'[{txt.strip()[:-1]}]'  # convert to array

        # debug
        save_path = file_path.replace('.txt', '_final.txt')
        with open(save_path, 'w') as file:
            file.write(txt)

        data = json.loads(txt)

        if save:
            file_path = file_path.replace('.txt', '.json')
            with open(file_path, 'w') as jsonfile:
                json.dump(data, jsonfile)

        return data
