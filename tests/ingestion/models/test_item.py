from csgo_analysis.ingestion.models import ItemType


def test_itemtype():
    assert ItemType._PISTOL.id == 1
    assert ItemType._PISTOL.name == 'pistol'
