import pytest
import os
from unittest.mock import patch
from csgo_analysis.ingestion.parser import Parser
from csgo_analysis.ingestion.models.dbconn import DBConn


@pytest.mark.integration
def test_cleanup_ingestion(raw_match_txt, fixture_path):
    parser = Parser()

    parser.scode = 'CSGO-xYZ1-P250-CZ75a-AK47M-M4A1S'
    parser.raw_match_data = raw_match_txt

    path = os.path.join(os.getcwd(), 'csgo_analysis', 'ingestion', 'data')
    filename = os.path.join(path, '003467091076722983021_0879396408.txt')
    print(filename)
    parser.output_path = filename
    with open(filename, encoding='ascii', errors='ignore') as txt:
        parser.data_txt = txt.read()

    parser.load_game_data()
