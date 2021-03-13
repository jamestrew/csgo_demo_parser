from datetime import datetime
import pytest
from psycopg2._psycopg import TimestampFromTicks
import psycopg2
from csgo_analysis.ingestion.models import Game
from unittest.mock import patch


@patch.object(Game, 'insert')
def test_ingest_data(insert_patch, raw_match_txt):
    g = Game()
    scode = 'CSGO-xQKYC-4Nbc4-h43V2-Jc66v-EWtrD'
    map_name = 'de_dust2'

    fields = {
        'share_code': scode,
        'match_time': TimestampFromTicks(1613364114),
        'match_duration': 2319,
        'map_l_id': 1,
        'final_score_two': 10,
        'final_score_three': 16
    }

    g.ingest_data(raw_match_txt, scode, map_name)
    assert g.recordset['share_code'] == scode
    assert str(g.recordset['match_time']) == str(TimestampFromTicks(1613364114))
    assert g.recordset['match_duration'] == 2319
    assert g.recordset['map_l_id'] == 1
    assert g.recordset['final_score_two'] == 10
    assert g.recordset['final_score_three'] == 16
    assert set(g.recordset.keys()) == set(fields.keys())
    insert_patch.assert_called_with('game', g.recordset, returning=True)


@pytest.mark.ingestion  # noqa
@patch.object(Game, 'connect')
@patch.object(Game, 'close')
def test_game_ingestion_insert(connect_patch, close_patch, db_cur, db_conn, raw_match_txt):
    g = Game()
    g.cur = db_cur
    g.conn = db_conn
    scode = 'CSGO-xQKYC-4Nbc4-h43V2-Jc66v-EWtrD'
    map_name = 'de_dust2'

    return_id = g.ingest_data(raw_match_txt, scode, map_name)
    connect_patch.assert_called_once()
    close_patch.assert_called_once()

    db_cur.execute("SELECT * FROM game WHERE id = (%s)", (return_id,))
    id, sc, mt, md, mlid, fs2, fs3 = db_cur.fetchone()

    assert id == return_id
    assert sc == scode
    assert mt == datetime(2021, 2, 14, 23, 41, 54)
    assert md == 2319
    assert mlid == 1
    assert fs2 == 10
    assert fs3 == 16


@pytest.mark.ingestion  # noqa
@patch.object(Game, 'connect')
@patch.object(Game, 'close')
def test_game_ingestion_duplicate(connect_patch, close_patch, db_cur, db_conn, raw_match_txt):
    insert_str = "INSERT INTO game (share_code, match_time, match_duration, map_l_id, final_score_two, final_score_three) VALUES (%s, %s, %s, %s, %s, %s)"
    val = ['CSGO-xQKYC-4Nbc4-h43V2-Jc66v-EWtrX', TimestampFromTicks(1613364114), 2319, 1, 10, 16]

    scode = 'CSGO-xQKYC-4Nbc4-h43V2-Jc66v-EWtrX'
    g1 = Game()
    g1.cur = db_cur
    g1.conn = db_conn
    g1.ingest_data(raw_match_txt, scode, 'de_dust2')
    print(g1.cur, g1.conn)

    with pytest.raises(psycopg2.errors.UniqueViolation):
        db_cur.execute(insert_str, val)
