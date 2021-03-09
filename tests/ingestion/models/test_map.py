import pytest
from csgo_analysis.ingestion.models import Map


@pytest.mark.parametrize(
    'map_name, id', [
        ('de_dust2', 1),
        ('de_mirage', 2),
        ('de_inferno', 3),
        ('de_cache', 4),
        ('de_overpass', 5),
        ('de_train', 6),
        ('de_nuke', 7),
        ('de_cbble', 8),
        ('de_vertigo', 9)
    ]
)
def test_get_map_id(map_name, id):
    assert Map.get_map_id(map_name) == id
