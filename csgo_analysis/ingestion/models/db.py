

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
