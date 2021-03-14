from csgo_analysis.ingestion.event_controller import EventsController
from csgo_analysis.ingestion.models import ItemEquip, PlayerHurt
from unittest.mock import patch, call


# def test_events_prep(event_dirty, event_clean):
#     e = EventsController(event_dirty)
#     output = e.clean_data()
#     assert output == event_clean


def test_player_equip_init():
    player_xuids = [1, 2, 3, 4, 5]
    ec = EventsController(1, None, player_xuids)
    assert ec.player_health == {
        1: 100, 2: 100, 3: 100, 4: 100, 5: 100
    }


@patch.object(ItemEquip, 'build_event')
def test_event_class_calling(build_patch):
    data = [
        {
            "item_equip": {
                "userid": 1,
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
    ec.ingest_prep()

    build_patch.assert_called_once_with(1, event_data, 1, 0)


def test_event_clean_data(events, events_clean):
    ec = EventsController(1, events, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ec.ingest_prep()
    assert ec.clean_data == events_clean
    assert ec.player_health[5] == 21


@patch.object(PlayerHurt, 'build_event')
def test_overkill_damage_correction(build_event_patch, hurt, hurt_clean):
    ec = EventsController(1, hurt, [1])
    ec.ingest_prep()

    args = [
        call(1, data['player_hurt'], i + 1, 0) for i, data in enumerate(hurt_clean)
    ]
    build_event_patch.call_count == 11
    build_event_patch.assert_has_calls(args)
