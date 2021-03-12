from csgo_analysis.ingestion.models.db import DB, ItemLookup
import pytest


@pytest.mark.parametrize(
    'value, output', [
        ("0 ", False),
        ("1 ", True),
    ]
)
def test_custom_bool(value, output):
    db = DB()
    assert db.custom_bool(value) == output


@pytest.mark.parametrize(
    'full_name, short_name', [
        ('weapon_cz75a', 'cz75a'),
        ('weapon_deagle', 'deagle'),
        ('weapon_elite', 'elite'),
        ('weapon_fiveseven', 'fiveseven'),
        ('weapon_glock', 'glock'),
        ('weapon_hkp2000', 'hkp2000'),
        ('weapon_p250', 'p250'),
        ('weapon_revolver', 'revolver'),
        ('weapon_tec9', 'tec9'),
        ('weapon_usp_silencer', 'usp_silencer'),
        ('weapon_mag7', 'mag7'),
        ('weapon_nova', 'nova'),
        ('weapon_sawedoff', 'sawedoff'),
        ('weapon_xm1014', 'xm1014'),
        ('weapon_m249', 'm249'),
        ('weapon_negev', 'negev'),
        ('weapon_mac10', 'mac10'),
        ('weapon_mp5sd', 'mp5sd'),
        ('weapon_mp7', 'mp7'),
        ('weapon_mp9', 'mp9'),
        ('weapon_p90', 'p90'),
        ('weapon_bizon', 'bizon'),
        ('weapon_ump45', 'ump45'),
        ('weapon_ak47', 'ak47'),
        ('weapon_aug', 'aug'),
        ('weapon_famas', 'famas'),
        ('weapon_galilar', 'galilar'),
        ('weapon_m4a1_silencer', 'm4a1_silencer'),
        ('weapon_m4a1', 'm4a1'),
        ('weapon_sg556', 'sg556'),
        ('weapon_awp', 'awp'),
        ('weapon_g3sg1', 'g3sg1'),
        ('weapon_scar20', 'scar20'),
        ('weapon_ssg08', 'ssg08'),
        ('weapon_taser', 'taser'),
        ('weapon_hegrenade', 'hegrenade'),
        ('weapon_flashbang', 'flashbang'),
        ('weapon_smokegrenade', 'smokegrenade'),
        ('weapon_incgrenade', 'incgrenade'),
        ('weapon_molotov', 'molotov'),
        ('weapon_decoy', 'decoy'),
        ('weapon_knife', 'knife'),
        ('weapon_knife_t', 'knife_t'),
        ('weapon_knifegg', 'knifegg'),
        ('weapon_knife_css', 'knife_css'),
        ('weapon_bayonet', 'bayonet'),
        ('weapon_knife_flip', 'knife_flip'),
        ('weapon_knife_gut', 'knife_gut'),
        ('weapon_knife_karambit', 'knife_karambit'),
        ('weapon_knife_m9_bayonet', 'knife_m9_bayonet'),
        ('weapon_knife_tactical', 'knife_tactical'),
        ('weapon_knife_butterfly', 'knife_butterfly'),
        ('weapon_knife_falchion', 'knife_falchion'),
        ('weapon_knife_push', 'knife_push'),
        ('weapon_knife_survival', 'knife_survival'),
        ('weapon_knife_ursus', 'knife_ursus'),
        ('weapon_knife_gypsy_jackknife', 'knife_gypsy_jackknife'),
        ('weapon_knife_stiletto', 'knife_stiletto'),
        ('weapon_knife_widowmaker', 'knife_widowmaker'),
        ('weapon_knife_ghost', 'knife_ghost'),
        ('weapon_knife_canis', 'knife_canis'),
        ('weapon_knife_cord', 'knife_cord'),
        ('weapon_knife_skeleton', 'knife_skeleton'),
        ('weapon_knife_outdoor', 'knife_outdoor'),
        ('item_kevlar', 'kevlar'),
        ('item_assaultsuit', 'assaultsuit'),
        ('item_defuser', 'defuser'),
        ('weapon_c4', 'c4')
    ]
)
def test_get_short_wep(full_name, short_name):
    il = ItemLookup(None, full_name, None)

    assert il.short_wep == short_name
