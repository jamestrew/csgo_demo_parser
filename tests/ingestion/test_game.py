from csgo_analysis.ingestion import parser

import pytest


@pytest.mark.parametrize(
    'input', 'output', [
        ('steam://rungame/730/76561202255233023/+csgo_download_match%20CSGO-WHujK-oFZSm-azzvG-Sac3A-uT2JE', 'CSGO-WHujK-oFZSm-azzvG-Sac3A-uT2JE'),
        ('garbage', False),
        ('CSGO-also-garbage', False)
    ]
)
def test_get_match_data(input, output):
    p = parser.Parser()
    test_output = p.extract_sharecode(input)
    assert test_output == output
