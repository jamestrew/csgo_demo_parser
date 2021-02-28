from unittest.mock import patch
from csgo_analysis.ingestion.models.db import DB
import pytest


@pytest.mark.parametrize(
    "tablename, col, val, statement,  many", [
        (
            'map_l',
            ['id', 'map_name'],
            [10, 'de_anubis'],
            "INSERT INTO map_l (id, map_name) VALUES (%s, %s)",
            False
        ),
        (
            'map_l',
            [['id', 'map_name'], ['id', 'map_name']],
            [[10, 'de_anubis'], [11, 'cs_office']],
            "INSERT INTO map_l (id, map_name) VALUES %s",
            True
        )
    ]
)
@patch.object(DB, 'execute')
def test_db_insert(exe_patch, tablename, col, val, statement, many):
    db = DB()
    output = db.insert(tablename, col, val, many)
    kwargs = {
        DB._OPSTR: statement,
        DB._VAL: val,
        DB._MANY: many,
        DB._RETURNING: False
    }
    exe_patch.assert_called_with('insert', kwargs)
    assert output is None


@patch.object(DB, 'execute_insert')
@patch.object(DB, 'connect')
def test_db_execute_calls(connect_patch, insert_patch):
    db = DB()
    func = 'insert'
    kwargs = 'foo'
    db.execute(func, kwargs)
    connect_patch.assert_called_once()
    insert_patch.assert_called_with(db, kwargs)
