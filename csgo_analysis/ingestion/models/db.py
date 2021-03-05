

class DB:
    _NAME = 'name'
    _TYPE = 'type'
    _NULLABLE = 'nullable'

    _TYPES = {}

    def __init__(self):
        self.fields = {}

    def input_column_data(self, col_name, data):
        """Add correctly type-casted data into fields.

        Parameters
        ----------
        col_name : str
            Column name (eg. game_id, item_id, etc)
        data : any
            Data to be type-casted and appended to the fields dict.
        """
        data_type = self._TYPES[col_name]
        self.fields[col_name] = data_type(data)
