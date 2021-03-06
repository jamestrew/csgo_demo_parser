from csgo_analysis.ingestion.event_controller import EventsController
from csgo_analysis.ingestion.models import ItemEquip
from unittest.mock import patch


# def test_events_prep(event_dirty, event_clean):
#     e = EventsController(event_dirty)
#     output = e.clean_data()
#     assert output == event_clean


def test_player_equip_init():
    player_xuids = [1, 2, 3, 4, 5]
    ec = EventsController(1, None, player_xuids)
    assert ec.player_equip_state == {
        1: None, 2: None, 3: None, 4: None, 5: None
    }


@patch.object(ItemEquip, 'build_event')
def test_event_class_calling(build_patch):
    data = [
        {
            "item_equip": {
                "userid": 76561198133822308,
                "item": "knife ",
                "defindex": "508 ",
                "canzoom": "0 ",
                "hassilencer": "0 ",
                "issilenced": "0 ",
                "hastracers": "0 ",
                "weptype": "0 ",
                "ispainted": "1 "
            }
        },
        {
            "item_equip": {
                "userid": "Waldo (id:16)",
                "item": "famas ",
                "defindex": "10 ",
                "canzoom": "0 ",
                "hassilencer": "0 ",
                "issilenced": "0 ",
                "hastracers": "1 ",
                "weptype": "3 ",
                "ispainted": "0 "
            }
        }
    ]

    event_data = data[0]['item_equip']

    ec = EventsController(1, data, [1, 2, 3])
    ec.ingest_data()

    build_patch.assert_called_once_with(1, event_data, 1, 0)
