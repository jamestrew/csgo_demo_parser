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

    SELECT = 'SELECT'
    FROM = 'FROM'
    WHERE = 'WHERE'
    ORDER_BY = 'ORDER BY'
    ASC = 'ASC'
    DESC = 'DESC'

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
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def insert(self, tablename, fields, returning=False):
        if isinstance(fields, list):
            columns = [col.col_name for col in fields[0].keys()]
            val_holder = '%s'
            col_holder = '(' + ', '.join(columns) + ')'
            val = [list(row.values()) for row in fields]
            many = True
        else:
            field_keys = [col.col_name for col in fields.keys()]
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

    def select(self, tablename, **kwargs):
        """ Really basic select function for checking data """
        table_str = f'FROM {tablename}'
        if not kwargs:
            select_str = f'select * {table_str}'
            self.execute(self.select.__name__, {self._OPSTR: select_str})
        else:
            if kwargs.get(self.SELECT) is not None:
                select = "SELECT "
                select += ', '.join([field.col_name for field in kwargs[self.SELECT]])
            else:
                select = "SELECT *"
            select_str = select + f'\n{table_str}'

            if kwargs.get(self.WHERE) is not None:
                col = list(kwargs[self.WHERE].keys())[0]
                val = list(kwargs[self.WHERE].values())[0]
                where_str = f"WHERE {col} = '{val}'"
                select_str += f'\n{where_str}'

            if kwargs.get(self.ORDER_BY) is not None:
                order_items = kwargs[self.ORDER_BY].items()
                ord_lst = [f'{col.col_name} {order}' for col, order in order_items]
                ord_str = 'ORDER BY '
                ord_str += ', '.join(ord_lst)
                select_str += f'\n{ord_str}'

            self.execute(self.select.__name__, {self._OPSTR: select_str})

        return self.data

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

        if many:
            execute_values(self.cur, insert_str, val)
        else:
            self.cur.execute(insert_str, val)

        self.return_id = self.cur.fetchone()[0] if returning else None

        self.close()

    def execute_select(self, kwargs):
        select_str = kwargs.get(self._OPSTR)
        self.cur.execute(select_str)
        self.data = self.cur.fetchall()
        self.close()
