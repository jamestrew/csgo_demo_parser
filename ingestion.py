from csgo_analysis.ingestion import parser


if __name__ == '__main__':
    url = 'steam://rungame/730/76561202255233023/+csgo_download_match%20CSGO-xQKYC-4Nbc4-h43V2-Jc66v-EWtrD'

    p = parser.Parser()
    p.scode = 'CSGO-xQKYC-4Nbc4-h43V2-Jc66v-EWtrD'
    with open('csgo_analysis/ingestion/data/003464678600035270745_0899595961.txt', encoding='ascii', errors='ignore') as f:
        p.data_txt = f.read()

    with open('csgo_analysis/ingestion/data/raw_match_data.txt') as f:
        p.raw_match_data = f.read()

    p.load_game_data()
    print(p.game_id)
