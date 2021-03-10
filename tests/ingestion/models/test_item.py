from csgo_analysis.ingestion.models import ItemType, Item


def test_itemtype():
    assert ItemType._PISTOL.id == 1
    assert ItemType._PISTOL.name == 'pistol'


def test_item():
    assert Item.AK47.id == 24
    assert Item.AK47.name == 'weapon_ak47'
    assert Item.AK47.short_name == 'ak47'


def test_get_id_with_name():
    assert Item.get_id_with_name('weapon_ak47') == 24


def test_get_id_with_short_name():
    assert Item.get_id_with_short_name('ak47') == 24
