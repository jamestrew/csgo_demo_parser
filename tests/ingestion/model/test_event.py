from csgo_analysis.ingestion.models import EventsController


def test_events_prep(event_dirty, event_clean):
    e = EventsController(event_dirty)
    output = e.clean_data()
    assert output == event_clean
