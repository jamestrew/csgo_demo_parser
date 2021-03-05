from csgo_analysis.ingestion.models.db import DB
import pytest


@pytest.mark.parametrize(
    'value, output', [
        ("0 ", False),
        ("1 ", True),
    ]
)
def test_custom_bool(value, output):
    db = DB()
    assert db.custom_bool(value) == output
