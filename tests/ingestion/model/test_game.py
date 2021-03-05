from psycopg2._psycopg import TimestampFromTicks
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
