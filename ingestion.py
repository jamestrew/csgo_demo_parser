from csgo_analysis.ingestion import parser


if __name__ == '__main__':

    p = parser.Parser()

    with open('csgo_analysis/ingestion/data/raw_match_data.txt') as file:
        data = file.read()

    p.match_info_cleaner(data)
