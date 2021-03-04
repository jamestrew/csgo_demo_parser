import definition
import os
import psycopg2
import json
from psycopg2.extras import execute_values


class DBConn:

    _OPSTR = 'opstr'
    _VAL = 'val'
    _MANY = 'many'
    _RETURNING = 'returning'

    timestamp_fmt = '%Y-%m-%d %H:%M:%S'

    def __init__(self):
        cred_path = os.path.join(definition.ING_DIR, 'models', 'db.json')
        self.connection_params = json.loads(open(cred_path).read())
        self.return_id = None
        self.conn = None
        self.cur = None

    def connect(self):
        self.conn = psycopg2.connect(**self.connection_params)
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    def insert(self, tablename, fields, returning=False):
        if isinstance(fields, list):
            val_holder = '%s'
            col_holder = '(' + ', '.join(list(fields[0].keys())) + ')'
            val = [list(row.values()) for row in fields]
            many = True
        else:
            field_keys = list(fields.keys())
            val_holder = '(' + ', '.join(['%s'] * len(field_keys)) + ')'
            col_holder = '(' + ', '.join(field_keys) + ')'
            val = list(fields.values())
            many = False
        insert_str = f'INSERT INTO {tablename} {col_holder} VALUES {val_holder}'

        if returning:
            insert_str += ' RETURNING id'

        kwargs = {
            self._OPSTR: insert_str,
            self._VAL: val,
            self._MANY: many,
            self._RETURNING: returning
        }

        self.execute(self.insert.__name__, kwargs)
        return self.return_id

    def execute(self, func, kwargs):
        self.connect()
        func_call = getattr(DBConn, self.execute.__name__ + '_' + func)
        func_call(self, kwargs)

    def execute_insert(self, kwargs):
        # TODO add UniqueViolation error handling
        insert_str = kwargs.get(self._OPSTR)
        val = kwargs.get(self._VAL)
        many = kwargs.get(self._MANY)
        returning = kwargs.get(self._RETURNING)
        print(insert_str, val)
        print()

        if many:
            execute_values(self.cur, insert_str, val)
        else:
            self.cur.execute(insert_str, val)
        self.conn.commit()

        self.return_id = self.cur.fetchone() if returning else None

        self.close()
