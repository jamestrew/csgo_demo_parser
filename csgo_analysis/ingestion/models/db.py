import definition
import os
import psycopg2
import json


class DB:

    timestamp_fmt = '%Y-%m-%d %H:%M:%S'

    def __init__(self):
        cred_path = os.path.join(definition.ING_DIR, 'models', 'db.json')
        self.connection_params = json.loads(open(cred_path).read())

    def insert(self, tablename, col, val):
        self.conn = psycopg2.connect(**self.connection_params)
        self.cur = self.conn.cursor()
        val_placeholder = '(' + ', '.join(['%s'] * len(val)) + ')'
        if col is None:
            insert_str = f'INSERT INTO {tablename} VALUES {val_placeholder}'
        else:
            col_placeholder = '(' + ', '.join(col) + ')'
            insert_str = f'INSERT INTO {tablename} {col_placeholder} VALUES {val_placeholder}'

        print(insert_str, val)
        self.cur.execute(insert_str, val)
        self.conn.commit()

        self.cur.close()
        self.conn.close()
        # TODO add UniqueViolation error handling

