import unittest
from csgo_analysis.ingestion.models import Items
from csgo_analysis.ingestion.item_controller import ItemController
import pytest


@pytest.fixture
def item_controller(item_data):
    return ItemController(item_data)


def test_item_controller_init(item_controller, item_data):
    assert item_controller.data == item_data


def test_get_model_index(item_controller):
    model_dict = item_controller.get_model_index()
    data = {444: Items._DEAGLE, 657: Items._P250}
    unittest.TestCase.assertCountEqual(None, model_dict, data)


def test_get_defindex(item_controller):
    def_indices = item_controller.get_defindex()
    data = {Items._DEAGLE: (1, 64), Items._P250: (36, 63)}
    unittest.TestCase.assertCountEqual(None, def_indices, data)


def test_get_def_model_index(item_controller):
    index_dict = item_controller.get_def_model_index()
    data = {1: 444, 64: Items._DEAGLE, 63: Items._P250, 36: 657}
    unittest.TestCase.assertCountEqual(None, index_dict, data)


def test_get_def_index_ids(item_controller):
    output = item_controller.get_def_index_ids()
    data = {
        1: Items._DEAGLE,
        64: Items._REVOLVER,
        63: Items._CZ75A,
        36: Items._P250
    }
    unittest.TestCase.assertCountEqual(None, output, data)
