import json
import re


class JsonConverter:

    player_p = r'player info'
    player_r = r'player_info'

    main_key_p = r'([a-z_]+)\n({\n)'
    main_key_r = r'{"\1": \2'

    inner_key_p = r' ([0-9a-zA-Z_]+):'
    inner_key_r = r'"\1":'

    inner_val_p = r': ?([#\-0-9a-zA-Z\. _\(\):]+)'
    inner_val_r = r': "\1", '

    friends_p = r'\s+"friendsName":\n'
    friends_r = r' "friendsName": "None", '

    end_bracket_p = r'}'
    end_bracket_r = r'}}, '

    middle_p = r'},\n(.+)\n{'
    middle_r = r'}, {'

    trailing_comma_p = r', }}, '
    trailing_comma_r = r'}}, '
    trailing_comma_p2 = r'", {"'
    trailing_comma_r2 = r'"}}, {"'

    numbers_p = r'\d+, .+\n'
    create_p = r'CreateStringTable:.+\n'
    update_p = r'UpdateStringTable:.+\n'
    bot_p = r'Player [a-zA-z ]+\(id:[0-9]+\).+\n'
    annoucements = r'[a-z_]+\n{\n}\n'
    junk_p = r'}\n(.+\n(?!{))+(.+\n(?={))*?'
    junk_r = r'\n\2'
    new_line_p = r'\n'
    blank = r''

    def convert(self, txt, file_path, save=False):
        txt = self.data
        txt = re.sub(self.annoucements, self.blank, txt)
        txt = re.sub(self.numbers_p, self.blank, txt)
        txt = re.sub(self.create_p, self.blank, txt)
        txt = re.sub(self.update_p, self.blank, txt)
        txt = re.sub(self.bot_p, self.blank, txt)
        txt = re.sub(self.junk_p, self.junk_r, txt)
        txt = re.sub(self.player_p, self.player_r, txt)
        txt = re.sub(self.inner_key_p, self.inner_key_r, txt)
        txt = re.sub(self.inner_val_p, self.inner_val_r, txt)
        txt = re.sub(self.end_bracket_p, self.end_bracket_r, txt)
        txt = re.sub(self.friends_p, self.friends_r, txt)
        txt = re.sub(self.main_key_p, self.main_key_r, txt)
        txt = re.sub(self.middle_p, self.middle_r, txt)
        txt = re.sub(self.new_line_p, self.blank, txt)
        txt = re.sub(self.trailing_comma_p, self.trailing_comma_r, txt)
        txt = re.sub(self.trailing_comma_p2, self.trailing_comma_r2, txt)

        txt = f'[{txt.strip()[:-1]}]'
        data = json.loads(txt)

        if save:
            save_path = file_path.replace('txt', 'json')
            with open(save_path, 'w') as jsonfile:
                json.dump(self.data, jsonfile)

        return data
