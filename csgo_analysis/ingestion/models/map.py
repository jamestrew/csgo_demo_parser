from csgo_analysis.ingestion.const import Map


class MapL:

    MAP_L = {
        'de_dust2': Map.DUST2,
        'de_mirage': Map.MIRAGE,
        'de_inferno': Map.INFERNO,
        'de_cache': Map.CACHE,
        'de_overpass': Map.OVERPASS,
        'de_train': Map.TRAIN,
        'de_nuke': Map.NUKE,
        'de_cbble': Map.CBBLE,
        'de_vertigo': Map.VERTIGO
    }

    def get_map_l_id(self, map_name):
        return self.MAP_L.get(map_name).value
