from csgo_analysis.ingestion.models.db import Lookup, ItemLookup


class ItemType:

    _EQUIPMENT = Lookup(0, 'equipment')
    _PISTOL = Lookup(1, 'pistol')
    _SMG = Lookup(2, 'smg')
    _SHOTGUN = Lookup(3, 'shotgun')
    _LMG = Lookup(4, 'lmg')
    _RIFLE = Lookup(5, 'rifle')
    _SNIPER = Lookup(6, 'sniper')
    _GRENADE = Lookup(7, 'grenade')
    _MELEE = Lookup(8, 'melee')


class Item:

    CZ75A = ItemLookup(1, 'weapon_cz75a', 'p250')
    DEAGLE = ItemLookup(2, 'weapon_deagle', 'deagle')
    ELITE = ItemLookup(3, 'weapon_elite', 'elite')
    FIVESEVEN = ItemLookup(4, 'weapon_fiveseven', 'fiveseven')
    GLOCK = ItemLookup(5, 'weapon_glock', 'glock')
    HKP2000 = ItemLookup(6, 'weapon_hkp2000', 'hkp2000')
    P250 = ItemLookup(7, 'weapon_p250', 'p250')
    REVOLVER = ItemLookup(8, 'weapon_revolver', 'deagle')
    TEC9 = ItemLookup(9, 'weapon_tec9', 'tec9')
    USP_SILENCER = ItemLookup(10, 'weapon_usp_silencer', 'hkp2000')
    MAG7 = ItemLookup(11, 'weapon_mag7', 'mag7')
    NOVA = ItemLookup(12, 'weapon_nova', 'nova')
    SAWEDOFF = ItemLookup(13, 'weapon_sawedoff', 'sawedoff')
    XM1014 = ItemLookup(14, 'weapon_xm1014', 'xm1014')
    M249 = ItemLookup(15, 'weapon_m249', 'm249')
    NEGEV = ItemLookup(16, 'weapon_negev', 'negev')
    MAC10 = ItemLookup(17, 'weapon_mac10', 'mac10')
    MP5SD = ItemLookup(18, 'weapon_mp5sd', 'mp7')
    MP7 = ItemLookup(19, 'weapon_mp7', 'mp7')
    MP9 = ItemLookup(20, 'weapon_mp9', 'mp9')
    P90 = ItemLookup(21, 'weapon_p90', 'p90')
    BIZON = ItemLookup(22, 'weapon_bizon', 'bizon')
    UMP45 = ItemLookup(23, 'weapon_ump45', 'ump45')
    AK47 = ItemLookup(24, 'weapon_ak47', 'ak47')
    AUG = ItemLookup(25, 'weapon_aug', 'aug')
    FAMAS = ItemLookup(26, 'weapon_famas', 'famas')
    GALILAR = ItemLookup(27, 'weapon_galilar', 'galilar')
    M4A1_SILENCER = ItemLookup(28, 'weapon_m4a1_silencer', 'm4a1')
    M4A1 = ItemLookup(29, 'weapon_m4a1', 'm4a1')
    SG556 = ItemLookup(30, 'weapon_sg556', 'sg556')
    AWP = ItemLookup(31, 'weapon_awp', 'awp')
    G3SG1 = ItemLookup(32, 'weapon_g3sg1', 'g3sg1')
    SCAR20 = ItemLookup(33, 'weapon_scar20', 'scar20')
    SSG08 = ItemLookup(34, 'weapon_ssg08', 'ssg08')
    TASER = ItemLookup(35, 'weapon_taser', 'taser')
    HEGRENADE = ItemLookup(36, 'weapon_hegrenade', 'hegrenade')
    FLASHBANG = ItemLookup(37, 'weapon_flashbang', 'flashbang')
    SMOKEGRENADE = ItemLookup(38, 'weapon_smokegrenade', 'smokegrenade')
    INCGRENADE = ItemLookup(39, 'weapon_incgrenade', 'incgrenade')
    MOLOTOV = ItemLookup(40, 'weapon_molotov', 'molotov')
    DECOY = ItemLookup(41, 'weapon_decoy', 'decoy')
    KNIFE = ItemLookup(42, 'weapon_knife', 'knife')
    KNIFE_T = ItemLookup(42, 'weapon_knife_t', 'knife')
    KNIFEGG = ItemLookup(42, 'weapon_knifegg', 'knife')
    KNIFE_CSS = ItemLookup(42, 'weapon_knife_css', 'knife')
    BAYONET = ItemLookup(42, 'weapon_bayonet', 'knife')
    KNIFE_FLIP = ItemLookup(42, 'weapon_knife_flip', 'knife')
    KNIFE_GUT = ItemLookup(42, 'weapon_knife_gut', 'knife')
    KNIFE_KARAMBIT = ItemLookup(42, 'weapon_knife_karambit', 'knife')
    KNIFE_M9_BAYONET = ItemLookup(42, 'weapon_knife_m9_bayonet', 'knife')
    KNIFE_TACTICAL = ItemLookup(42, 'weapon_knife_tactical', 'knife')
    KNIFE_BUTTERFLY = ItemLookup(42, 'weapon_knife_butterfly', 'knife')
    KNIFE_FALCHION = ItemLookup(42, 'weapon_knife_falchion', 'knife')
    KNIFE_PUSH = ItemLookup(42, 'weapon_knife_push', 'knife')
    KNIFE_SURVIVAL = ItemLookup(42, 'weapon_knife_survival', 'knife')
    KNIFE_URSUS = ItemLookup(42, 'weapon_knife_ursus', 'knife')
    KNIFE_GYPSY_JACKKNIFE = ItemLookup(42, 'weapon_knife_gypsy_jackknife', 'knife')
    KNIFE_STILETTO = ItemLookup(42, 'weapon_knife_stiletto', 'knife')
    KNIFE_WIDOWMAKER = ItemLookup(42, 'weapon_knife_widowmaker', 'knife')
    KNIFE_GHOST = ItemLookup(42, 'weapon_knife_ghost', 'knife')
    KNIFE_CANIS = ItemLookup(42, 'weapon_knife_canis', 'knife')
    KNIFE_CORD = ItemLookup(42, 'weapon_knife_cord', 'knife')
    KNIFE_SKELETON = ItemLookup(42, 'weapon_knife_skeleton', 'knife')
    KNIFE_OUTDOOR = ItemLookup(42, 'weapon_knife_outdoor', 'knife')
    KEVLAR = ItemLookup(65, 'item_kevlar', 'vest')
    ASSAULTSUIT = ItemLookup(66, 'item_assaultsuit', 'vesthelm')
    DEFUSER = ItemLookup(67, 'item_defuser', 'defuser')
    C4 = ItemLookup(68, 'weapon_c4', 'c4')

    NAME_L = {
        CZ75A.name: CZ75A,
        DEAGLE.name: DEAGLE,
        ELITE.name: ELITE,
        FIVESEVEN.name: FIVESEVEN,
        GLOCK.name: GLOCK,
        HKP2000.name: HKP2000,
        P250.name: P250,
        REVOLVER.name: REVOLVER,
        TEC9.name: TEC9,
        USP_SILENCER.name: USP_SILENCER,
        MAG7.name: MAG7,
        NOVA.name: NOVA,
        SAWEDOFF.name: SAWEDOFF,
        XM1014.name: XM1014,
        M249.name: M249,
        NEGEV.name: NEGEV,
        MAC10.name: MAC10,
        MP5SD.name: MP5SD,
        MP7.name: MP7,
        MP9.name: MP9,
        P90.name: P90,
        BIZON.name: BIZON,
        UMP45.name: UMP45,
        AK47.name: AK47,
        AUG.name: AUG,
        FAMAS.name: FAMAS,
        GALILAR.name: GALILAR,
        M4A1_SILENCER.name: M4A1_SILENCER,
        M4A1.name: M4A1,
        SG556.name: SG556,
        AWP.name: AWP,
        G3SG1.name: G3SG1,
        SCAR20.name: SCAR20,
        SSG08.name: SSG08,
        TASER.name: TASER,
        HEGRENADE.name: HEGRENADE,
        FLASHBANG.name: FLASHBANG,
        SMOKEGRENADE.name: SMOKEGRENADE,
        INCGRENADE.name: INCGRENADE,
        MOLOTOV.name: MOLOTOV,
        DECOY.name: DECOY,
        KNIFE.name: KNIFE,
        KNIFE_T.name: KNIFE_T,
        KNIFEGG.name: KNIFEGG,
        KNIFE_CSS.name: KNIFE_CSS,
        BAYONET.name: BAYONET,
        KNIFE_FLIP.name: KNIFE_FLIP,
        KNIFE_GUT.name: KNIFE_GUT,
        KNIFE_KARAMBIT.name: KNIFE_KARAMBIT,
        KNIFE_M9_BAYONET.name: KNIFE_M9_BAYONET,
        KNIFE_TACTICAL.name: KNIFE_TACTICAL,
        KNIFE_BUTTERFLY.name: KNIFE_BUTTERFLY,
        KNIFE_FALCHION.name: KNIFE_FALCHION,
        KNIFE_PUSH.name: KNIFE_PUSH,
        KNIFE_SURVIVAL.name: KNIFE_SURVIVAL,
        KNIFE_URSUS.name: KNIFE_URSUS,
        KNIFE_GYPSY_JACKKNIFE.name: KNIFE_GYPSY_JACKKNIFE,
        KNIFE_STILETTO.name: KNIFE_STILETTO,
        KNIFE_WIDOWMAKER.name: KNIFE_WIDOWMAKER,
        KNIFE_GHOST.name: KNIFE_GHOST,
        KNIFE_CANIS.name: KNIFE_CANIS,
        KNIFE_CORD.name: KNIFE_CORD,
        KNIFE_SKELETON.name: KNIFE_SKELETON,
        KNIFE_OUTDOOR.name: KNIFE_OUTDOOR,
        KEVLAR.name: KEVLAR,
        ASSAULTSUIT.name: ASSAULTSUIT,
        DEFUSER.name: DEFUSER,
        C4.name: C4,
    }

    SHORT_NAME_L = {
        DEAGLE.short_name: DEAGLE,
        ELITE.short_name: ELITE,
        FIVESEVEN.short_name: FIVESEVEN,
        GLOCK.short_name: GLOCK,
        HKP2000.short_name: HKP2000,
        P250.short_name: P250,
        TEC9.short_name: TEC9,
        MAG7.short_name: MAG7,
        NOVA.short_name: NOVA,
        SAWEDOFF.short_name: SAWEDOFF,
        XM1014.short_name: XM1014,
        M249.short_name: M249,
        NEGEV.short_name: NEGEV,
        MAC10.short_name: MAC10,
        MP7.short_name: MP7,
        MP9.short_name: MP9,
        P90.short_name: P90,
        BIZON.short_name: BIZON,
        UMP45.short_name: UMP45,
        AK47.short_name: AK47,
        AUG.short_name: AUG,
        FAMAS.short_name: FAMAS,
        GALILAR.short_name: GALILAR,
        M4A1.short_name: M4A1,
        SG556.short_name: SG556,
        AWP.short_name: AWP,
        G3SG1.short_name: G3SG1,
        SCAR20.short_name: SCAR20,
        SSG08.short_name: SSG08,
        TASER.short_name: TASER,
        HEGRENADE.short_name: HEGRENADE,
        FLASHBANG.short_name: FLASHBANG,
        SMOKEGRENADE.short_name: SMOKEGRENADE,
        INCGRENADE.short_name: INCGRENADE,
        MOLOTOV.short_name: MOLOTOV,
        DECOY.short_name: DECOY,
        KNIFE.short_name: KNIFE,
        KNIFE_T.short_name: KNIFE_T,
        KNIFEGG.short_name: KNIFEGG,
        KNIFE_CSS.short_name: KNIFE_CSS,
        BAYONET.short_name: BAYONET,
        KNIFE_FLIP.short_name: KNIFE_FLIP,
        KNIFE_GUT.short_name: KNIFE_GUT,
        KNIFE_KARAMBIT.short_name: KNIFE_KARAMBIT,
        KNIFE_M9_BAYONET.short_name: KNIFE_M9_BAYONET,
        KNIFE_TACTICAL.short_name: KNIFE_TACTICAL,
        KNIFE_BUTTERFLY.short_name: KNIFE_BUTTERFLY,
        KNIFE_FALCHION.short_name: KNIFE_FALCHION,
        KNIFE_PUSH.short_name: KNIFE_PUSH,
        KNIFE_SURVIVAL.short_name: KNIFE_SURVIVAL,
        KNIFE_URSUS.short_name: KNIFE_URSUS,
        KNIFE_GYPSY_JACKKNIFE.short_name: KNIFE_GYPSY_JACKKNIFE,
        KNIFE_STILETTO.short_name: KNIFE_STILETTO,
        KNIFE_WIDOWMAKER.short_name: KNIFE_WIDOWMAKER,
        KNIFE_GHOST.short_name: KNIFE_GHOST,
        KNIFE_CANIS.short_name: KNIFE_CANIS,
        KNIFE_CORD.short_name: KNIFE_CORD,
        KNIFE_SKELETON.short_name: KNIFE_SKELETON,
        KNIFE_OUTDOOR.short_name: KNIFE_OUTDOOR,
        KEVLAR.short_name: KEVLAR,
        ASSAULTSUIT.short_name: ASSAULTSUIT,
        DEFUSER.short_name: DEFUSER,
        C4.short_name: C4,
    }

    SHORT_WEP_L = {
        CZ75A.short_wep: CZ75A,
        DEAGLE.short_wep: DEAGLE,
        ELITE.short_wep: ELITE,
        FIVESEVEN.short_wep: FIVESEVEN,
        GLOCK.short_wep: GLOCK,
        HKP2000.short_wep: HKP2000,
        P250.short_wep: P250,
        REVOLVER.short_wep: REVOLVER,
        TEC9.short_wep: TEC9,
        USP_SILENCER.short_wep: USP_SILENCER,
        MAG7.short_wep: MAG7,
        NOVA.short_wep: NOVA,
        SAWEDOFF.short_wep: SAWEDOFF,
        XM1014.short_wep: XM1014,
        M249.short_wep: M249,
        NEGEV.short_wep: NEGEV,
        MAC10.short_wep: MAC10,
        MP5SD.short_wep: MP5SD,
        MP7.short_wep: MP7,
        MP9.short_wep: MP9,
        P90.short_wep: P90,
        BIZON.short_wep: BIZON,
        UMP45.short_wep: UMP45,
        AK47.short_wep: AK47,
        AUG.short_wep: AUG,
        FAMAS.short_wep: FAMAS,
        GALILAR.short_wep: GALILAR,
        M4A1_SILENCER.short_wep: M4A1_SILENCER,
        M4A1.short_wep: M4A1,
        SG556.short_wep: SG556,
        AWP.short_wep: AWP,
        G3SG1.short_wep: G3SG1,
        SCAR20.short_wep: SCAR20,
        SSG08.short_wep: SSG08,
        TASER.short_wep: TASER,
        HEGRENADE.short_wep: HEGRENADE,
        FLASHBANG.short_wep: FLASHBANG,
        SMOKEGRENADE.short_wep: SMOKEGRENADE,
        INCGRENADE.short_wep: INCGRENADE,
        MOLOTOV.short_wep: MOLOTOV,
        DECOY.short_wep: DECOY,
        KNIFE.short_wep: KNIFE,
        KNIFE_T.short_wep: KNIFE_T,
        KNIFEGG.short_wep: KNIFEGG,
        KNIFE_CSS.short_wep: KNIFE_CSS,
        BAYONET.short_wep: BAYONET,
        KNIFE_FLIP.short_wep: KNIFE_FLIP,
        KNIFE_GUT.short_wep: KNIFE_GUT,
        KNIFE_KARAMBIT.short_wep: KNIFE_KARAMBIT,
        KNIFE_M9_BAYONET.short_wep: KNIFE_M9_BAYONET,
        KNIFE_TACTICAL.short_wep: KNIFE_TACTICAL,
        KNIFE_BUTTERFLY.short_wep: KNIFE_BUTTERFLY,
        KNIFE_FALCHION.short_wep: KNIFE_FALCHION,
        KNIFE_PUSH.short_wep: KNIFE_PUSH,
        KNIFE_SURVIVAL.short_wep: KNIFE_SURVIVAL,
        KNIFE_URSUS.short_wep: KNIFE_URSUS,
        KNIFE_GYPSY_JACKKNIFE.short_wep: KNIFE_GYPSY_JACKKNIFE,
        KNIFE_STILETTO.short_wep: KNIFE_STILETTO,
        KNIFE_WIDOWMAKER.short_wep: KNIFE_WIDOWMAKER,
        KNIFE_GHOST.short_wep: KNIFE_GHOST,
        KNIFE_CANIS.short_wep: KNIFE_CANIS,
        KNIFE_CORD.short_wep: KNIFE_CORD,
        KNIFE_SKELETON.short_wep: KNIFE_SKELETON,
        KNIFE_OUTDOOR.short_wep: KNIFE_OUTDOOR,
        KEVLAR.short_wep: KEVLAR,
        ASSAULTSUIT.short_wep: ASSAULTSUIT,
        DEFUSER.short_wep: DEFUSER,
        C4.short_wep: C4
    }

    ALT_WEAPONS = [P250.short_name, DEAGLE.short_name]
    SUPP_WEAPONS = [HKP2000.short_name, M4A1.short_name, MP7.short_name]
    SUPP_WEAPONS_L = {
        HKP2000.short_name: USP_SILENCER,
        M4A1.short_name: M4A1_SILENCER,
        MP7.short_name: MP5SD
    }

    @classmethod
    def get_id_with_name(cls, item_name):
        return cls.NAME_L.get(item_name).id

    @classmethod
    def get_id_with_short_name(cls, item_short_name):
        return cls.SHORT_NAME_L.get(item_short_name).id

    @classmethod
    def get_id_with_short_wep(cls, short_wep):
        return cls.SHORT_WEP_L.get(short_wep).id

    @classmethod
    def get_suppressed_weapon(cls, short_name):
        return cls.SUPP_WEAPONS_L.get(short_name).id
