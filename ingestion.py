from csgo_analysis.ingestion import parser


if __name__ == '__main__':

    p = parser.Parser()
    p.dem_file = '003464678600035270745_0899595961.dem'

    p.demo_parse()
