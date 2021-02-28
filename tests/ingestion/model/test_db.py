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
    db.insert(tablename, col, val, many)
    exe_patch.assert_called_with(statement, val, many)
