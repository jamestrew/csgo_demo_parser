from unittest.mock import patch
import unittest
from csgo_analysis.ingestion.models import Item
from csgo_analysis.ingestion.item_controller import ItemController
import pytest


@pytest.fixture
def item_controller(item_data):
    return ItemController(item_data, None, [1, 2, 3])


def test_item_controller_init(item_controller, item_data):
    assert item_controller.data_txt == item_data
    assert item_controller.data is None
    assert item_controller.current_item == {1: None, 2: None, 3: None}


def test_get_model_index(item_controller):
    model_dict = item_controller._get_model_index()
    data = {444: Item.DEAGLE, 657: Item.P250}
    unittest.TestCase.assertCountEqual(None, model_dict, data)


def test_get_defindex(item_controller):
    def_indices = item_controller._get_defindex()
    data = {Item.DEAGLE: (1, 64), Item.P250: (36, 63)}
    unittest.TestCase.assertCountEqual(None, def_indices, data)


def test_get_def_model_index(item_controller):
    index_dict = item_controller._get_def_model_index()
    data = {1: 444, 64: Item.DEAGLE, 63: Item.P250, 36: 657}
    unittest.TestCase.assertCountEqual(None, index_dict, data)


def test_get_def_index_ids(item_controller):
    output = item_controller._get_def_index_ids()
    data = {
        1: Item.DEAGLE,
        64: Item.REVOLVER,
        63: Item.CZ75A,
        36: Item.P250
    }
    unittest.TestCase.assertCountEqual(None, output, data)


@patch.object(ItemController, '_get_def_index_ids')
def test_sub_item_id(get_def_index_ids_patch, weapons_data, weapons_data_clean):
    get_def_index_ids_patch.return_value = {999: Item.P250, 64: Item.CZ75A}
    ic = ItemController(None, weapons_data, [1, 2, 3, 4, 5, 8, 9])

    output = ic.sub_item_id()
    items = {1: 42, 4: 42, 3: 10, 2: 10, 5: 10, 9: 5, 8: 1}
    assert output == weapons_data_clean
    unittest.TestCase.assertCountEqual(None, ic.current_item, items)
