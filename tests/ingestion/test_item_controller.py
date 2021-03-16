from unittest.mock import patch
import unittest
from csgo_analysis.ingestion.models import Item
from csgo_analysis.ingestion.item_controller import ItemController
import pytest


@pytest.fixture
def item_controller():
    return ItemController(None, [1, 2, 3])


def test_item_controller_init(item_controller):
    assert item_controller.data is None
    assert item_controller.current_item == {1: None, 2: None, 3: None}


def test_sub_item_id(weapons_data, weapons_data_clean):
    ic = ItemController(weapons_data, [1, 2, 3, 4, 5, 8, 9])

    output = ic.sub_item_id()
    items = {1: 42, 4: 42, 3: 10, 2: 10, 5: 10, 9: 5, 8: 1}
    assert output == weapons_data_clean
    unittest.TestCase.assertCountEqual(None, ic.current_item, items)
