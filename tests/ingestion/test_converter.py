from csgo_analysis.ingestion.converter import JsonConverter


def test_begin_new_match(data_txt_begin, data_json_begin):
    output = JsonConverter.convert(data_txt_begin, None, False)
    assert output == data_json_begin
