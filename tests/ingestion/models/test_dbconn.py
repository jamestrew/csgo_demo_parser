from unittest.mock import patch
from csgo_analysis.ingestion.db.dbconn import DBConn
from csgo_analysis.ingestion.models.db import DB
from csgo_analysis.ingestion.models.game import Game
import pytest


@pytest.mark.parametrize(
    "tablename, fields, val, statement, returning, many", [
        (
            'test_table',
            {DB._ID: 10, DB._TEAM_L_ID: 2},
            [10, 2],
            "INSERT INTO test_table (id, team_l_id) VALUES (%s, %s)",
            False,
            False
        ),
        (
            'test_table',
            {DB._ID: 10, DB._TEAM_L_ID: 2},
            [10, 2],
            "INSERT INTO test_table (id, team_l_id) VALUES (%s, %s) RETURNING id",
            True,
            False
        ),
        (
            'test_table',
            [{DB._ID: 10, DB._TEAM_L_ID: 2}, {DB._ID: 11, DB._TEAM_L_ID: 3}],
            [[10, 2], [11, 3]],
            "INSERT INTO test_table (id, team_l_id) VALUES %s",
            False,
            True
        ),
    ]
)
@patch.object(DBConn, 'execute')
def test_db_insert(exe_patch, tablename, fields, statement, val, returning, many):
    db = DBConn()
    db.insert(tablename, fields, returning)
    kwargs = {
        DBConn._OPSTR: statement,
        DBConn._VAL: val,
        DBConn._MANY: many,
        DBConn._RETURNING: returning
    }
    exe_patch.assert_called_with('insert', kwargs)


@patch.object(DBConn, 'execute_insert')
@patch.object(DBConn, 'connect')
def test_db_execute_insert_calls(connect_patch, insert_patch):
    db = DBConn()
    func = 'insert'
    kwargs = 'foo'
    db.execute(func, kwargs)
    connect_patch.assert_called_once()
    insert_patch.assert_called_with(db, kwargs)


@patch.object(DBConn, 'execute_select')
@patch.object(DBConn, 'connect')
def test_db_execute_select_calls(connect_patch, select_patch):
    db = DBConn()
    func = 'select'
    kwargs = 'foo'
    db.execute(func, kwargs)
    connect_patch.assert_called_once()
    select_patch.assert_called_with(db, kwargs)


@patch.object(DBConn, 'execute')
def test_select_statement_create_basic(execute_patch):
    execute_patch.return_value = True
    tablename = 'game'
    select = 'select * from game'
    kwargs = {DBConn._OPSTR: select}

    db = DBConn()
    output = db.select(tablename)
    execute_patch.called_once_with('select', kwargs)


@patch.object(DBConn, 'execute')
def test_select_statement_complex(execute_patch):
    execute_patch.return_value = True
    tablename = 'game'
    kwargs = {
        DBConn.SELECT: [Game._ID, Game._SHARE_CODE],
        DBConn.WHERE: {Game._SHARE_CODE: 'CSGO_STAT'},
        DBConn.ORDER_BY: {Game._SHARE_CODE: DBConn.DESC, Game._ID: DBConn.ASC}
    }
    select = """SELECT id, share_code
                FROM game WHERE share_code = 'CSGO_STAT'
                ORDER BY share_code DESC, id ASC"""

    db = DBConn()
    output = db.select(tablename, **kwargs)
    execute_patch.called_once_with('select', {DBConn._OPSTR: select})
