from csgo_analysis.ingestion.models.db import Lookup


class Map:

    DUST2 = Lookup(1, 'de_dust2')
    MIRAGE = Lookup(2, 'de_mirage')
    INFERNO = Lookup(3, 'de_inferno')
    CACHE = Lookup(4, 'de_cache')
    OVERPASS = Lookup(5, 'de_overpass')
    TRAIN = Lookup(6, 'de_train')
    NUKE = Lookup(7, 'de_nuke')
    CBBLE = Lookup(8, 'de_cbble')
    VERTIGO = Lookup(9, 'de_vertigo')

    MAPS = [
        DUST2,
        MIRAGE,
        INFERNO,
        CACHE,
        OVERPASS,
        TRAIN,
        NUKE,
        CBBLE,
        VERTIGO
    ]

    MAP_L = {
        DUST2.name: DUST2,
        MIRAGE.name: MIRAGE,
        INFERNO.name: INFERNO,
        CACHE.name: CACHE,
        OVERPASS.name: OVERPASS,
        TRAIN.name: TRAIN,
        NUKE.name: NUKE,
        CBBLE.name: CBBLE,
        VERTIGO.name: VERTIGO
    }

    @classmethod
    def get_map_id(cls, map_name):
        return cls.MAP_L.get(map_name).id
