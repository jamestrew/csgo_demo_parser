import re
from collections import namedtuple

FieldBase = namedtuple('Field', ['col_name', 'data_type', 'ref', 'nullable'])


class Field(FieldBase):
    def __new__(cls, col_name, data_type, ref, nullable=False):
        return super().__new__(cls, col_name, data_type, ref, nullable)

    def __repr__(self):
        return self.col_name


class Table:

    def __init__(self, columns):
        for column in columns:
            setattr(self, column, None)


class DB:

    # common fields
    _ID = Field('id', int, None)
    _GAME_ID = Field('game_id', int, None)
    _PLAYER_ID = Field('player_id', int, 'userid')
    _ATTACKER_ID = Field('attacker_id', int, 'attacker_id', True)
    _TEAM_L_ID = Field('team_l_id', int, 'team')
    _ITEM_ID = Field('item_id', int, 'item_id', True)
    _EVENT_NUMBER = Field('event_number', int, None)
    _ROUND = Field('round', int, None)

    def __init__(self):
        self.fields = {}

    @staticmethod
    def cast_data(recordset):
        ''' Return dataset with data type-casted correctly. '''
        for col, val in recordset.items():
            data_type = col.data_type
            nullable = col.nullable

            if not nullable and val is not None:
                val = data_type(val)
                if data_type == str:
                    val = val.strip()
            recordset[col] = val
        return recordset

    @staticmethod
    def custom_bool(value):
        return bool(int(value))


class Lookup:

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name


class ItemLookup(Lookup):

    def __init__(self, id: int, name: str, short_name: str) -> None:
        super().__init__(id, name)
        self.short_name = short_name
        self.short_wep = self.get_short_wep(name)

    @staticmethod
    def get_short_wep(name):
        try:
            return re.search(r'_([a-z_0-9]+)', name).group(1)
        except AttributeError:
            return name
