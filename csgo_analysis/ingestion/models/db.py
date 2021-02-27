import psycopg2
import json


class DB:

    timestamp_fmt = '%Y-%m-%d %H:%M:%S'

    def __init__(self):
        connection_params = json.loads(open('csgo_analysis/ingestion/models/db.json').read())
        self.conn = psycopg2.connect(**connection_params)
        self.cur = self.conn.cursor()

    def insert(self, tablename, val, col=None):
        val_placeholder = '(' + ', '.join(['%s'] * len(val)) + ')'
        if col is None:
            insert_str = f'INSERT INTO {tablename} VALUES {val_placeholder}'
        else:
            col_placeholder = '(' + ', '.join(col) + ')'
            insert_str = f'INSERT INTO {tablename} {col_placeholder} VALUES {val_placeholder}'

        print(insert_str, val)
        self.cur.execute(insert_str, val)
        self.conn.commit()

        # TODO add UniqueViolation error handling

    def close(self):
        self.cur.close()
        self.conn.close()
