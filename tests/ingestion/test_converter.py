from csgo_analysis.ingestion.converter import JsonConverter


def test_begin_new_match(data_txt_begin, data_json_begin):
    output = JsonConverter.convert(data_txt_begin, None, False)
    assert output == data_json_begin


def test_n_unicode_match(unicode_txt, unicode_json):
    output = JsonConverter.convert(unicode_txt, None, False)
    assert output == unicode_json
