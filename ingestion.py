from csgo_analysis.ingestion import parser, converter


def ingestion():
    url = 'steam://rungame/730/76561202255233023/+csgo_download_match%20CSGO-xQKYC-4Nbc4-h43V2-Jc66v-EWtrD'

    p = parser.Parser()
    p.scode = 'CSGO-xQKYC-4Nbc4-h43V2-Jc66v-EWtrD'
    p.output_path = 'csgo_analysis/ingestion/data/003464678600035270745_0899595961.txt'
    with open(p.output_path, encoding='ascii', errors='ignore') as f:
        p.data_txt = f.read()

    with open('csgo_analysis/ingestion/data/raw_match_data.txt') as f:
        p.raw_match_data = f.read()

    p.load_game_data()


def conversion():
    output_path = 'csgo_analysis/ingestion/data/003464678600035270745_0899595961.txt'
    with open(output_path, encoding='ascii', errors='ignore') as f:
        data_txt = f.read()

    c = converter.JsonConverter()
    c.convert(c, data_txt, output_path)


if __name__ == '__main__':
    ingestion()
