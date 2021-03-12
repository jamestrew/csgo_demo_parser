import re


class DB:
    _NAME = 'name'
    _TYPE = 'type'
    _NULLABLE = 'nullable'

    _TYPES = {}

    def __init__(self):
        self.fields = {}

    def cast_data(self, recordset):
        ''' Return dataset with data type-casted correctly. '''
        for col, val in recordset.items():
            data_type = self._TYPES[col]
            recordset[col] = data_type(val)
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
        return re.search(r'_([a-z_0-9]+)', name).group(1)
