import definition
import os
import psycopg2
import json
from psycopg2.extras import execute_values


class DB:

    timestamp_fmt = '%Y-%m-%d %H:%M:%S'

    def __init__(self):
        cred_path = os.path.join(definition.ING_DIR, 'models', 'db.json')
        self.connection_params = json.loads(open(cred_path).read())

    def insert(self, tablename, col, val, many=False):
        if many:
            col_holder = '(' + ', '.join(col[0]) + ')'
            val_holder = '%s'
        else:
            col_holder = '(' + ', '.join(col) + ')'
            val_holder = '(' + ', '.join(['%s'] * len(val)) + ')'
        insert_str = f'INSERT INTO {tablename} {col_holder} VALUES {val_holder}'

        print(insert_str, val)
        self.execute(insert_str, val, many)

    def execute(self, exe_str, val, many):
        # TODO add UniqueViolation error handling
        self.conn = psycopg2.connect(**self.connection_params)
        self.cur = self.conn.cursor()

        if many:
            execute_values(self.cur, exe_str, val)
        else:
            self.cur.execute(exe_str, val)
        self.conn.commit()

        self.cur.close()
        self.conn.close()
