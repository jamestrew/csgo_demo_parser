from unittest.mock import patch
from csgo_analysis.ingestion.models.dbconn import DBConn
import pytest


@pytest.mark.parametrize(
    "tablename, fields, val, statement,  many", [
        (
            'map_l',
            {'id': 10, 'map_name': 'de_anubis'},
            [10, 'de_anubis'],
            "INSERT INTO map_l (id, map_name) VALUES (%s, %s)",
            False
        ),
        (
            'map_l',
            [{'id': 10, 'map_name': 'de_anubis'}, {'id': 11, 'map_name': 'cs_office'}],
            [[10, 'de_anubis'], [11, 'cs_office']],
            "INSERT INTO map_l (id, map_name) VALUES %s",
            True
        )
    ]
)
@patch.object(DBConn, 'execute')
def test_db_insert(exe_patch, tablename, fields, statement, val, many):
    db = DBConn()
    output = db.insert(tablename, fields)
    kwargs = {
        DBConn._OPSTR: statement,
        DBConn._VAL: val,
        DBConn._MANY: many,
        DBConn._RETURNING: False
    }
    exe_patch.assert_called_with('insert', kwargs)
    assert output is None


@patch.object(DBConn, 'execute_insert')
@patch.object(DBConn, 'connect')
def test_db_execute_calls(connect_patch, insert_patch):
    db = DBConn()
    func = 'insert'
    kwargs = 'foo'
    db.execute(func, kwargs)
    connect_patch.assert_called_once()
    insert_patch.assert_called_with(db, kwargs)
