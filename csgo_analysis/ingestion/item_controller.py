import re
from csgo_analysis.ingestion.models import Item
from csgo_analysis.ingestion.models.db import DB
from csgo_analysis.ingestion.const import EventTypes


class ItemController:

    DEAGLE_MODEL_P = r' (\d+), models\/[a-z]weapons\/v_pist_deagle.mdl'
    P250_MODEL_P = r' (\d+), models\/[a-z]weapons\/v_pist_p250.mdl'
    DEAGLE_DEFINDEX_P = r' item: deagle\s+defindex: (\d+)'
    P250_DEFINDEX_P = r' item: p250\s+defindex: (\d+)'

    DEFINDEX = 'defindex'
    HASSILENCER = 'hassilencer'
    ITEM = 'item'
    WEAPON = 'weapon'
    ITEM_ID = 'item_id'
    USER_ID = 'userid'

    def __init__(self, data_txt, data, player_list):
        self.data_txt = data_txt
        self.data = data
        self.current_item = {player: None for player in player_list}

    def get_model_index(self):
        model_dict = {}
        deagle_model = re.search(self.DEAGLE_MODEL_P, self.data_txt).group(1)
        p250_model = re.search(self.P250_MODEL_P, self.data_txt).group(1)

        model_dict[int(deagle_model)] = Item.DEAGLE
        model_dict[int(p250_model)] = Item.P250
        return model_dict

    def get_defindex(self):
        def_indices = {}
        deagle_defindex = re.findall(self.DEAGLE_DEFINDEX_P, self.data_txt)
        def_indices[Item.DEAGLE] = tuple(map(int, deagle_defindex))

        p250_defindex = re.findall(self.P250_DEFINDEX_P, self.data_txt)
        def_indices[Item.P250] = tuple(map(int, p250_defindex))
        return def_indices

    def get_def_model_index(self):
        index_dict = {}
        for item, indices in self.get_defindex().items():
            for index in indices:
                p = r'402, m_iItemDefinitionIndex = $.+?429, m_nModelIndex = (\d+)'
                p = p.replace('$', str(index))
                pattern = re.compile(p, re.DOTALL | re.MULTILINE)
                match = re.search(pattern, self.data_txt)
                if match is None:
                    index_dict[index] = item
                    continue
                index_dict[index] = int(match.group(1))

        return index_dict

    def get_def_index_ids(self):
        index_item_dict = {}
        model_index = self.get_model_index()
        for defindex, modelindex in self.get_def_model_index().items():
            if modelindex == Item.DEAGLE:
                index_item_dict[defindex] = Item.REVOLVER
            elif modelindex == Item.P250:
                index_item_dict[defindex] = Item.CZ75A
            else:
                index_item_dict[defindex] = model_index[modelindex]

        return index_item_dict

    def sub_item_id(self):
        def_index_ids = self.get_def_index_ids()

        for event in self.data:
            event_name = list(event.keys())[0]
            event_data = event[event_name]

            if self.USER_ID in event_data.keys() and \
                    event_data[self.USER_ID] not in self.current_item.keys():
                continue

            if event_name == EventTypes.ITEM_EQUIP:
                item_id = self.get_equip_id(event_data, def_index_ids)
                userid = event_data[self.USER_ID]
                event_data[self.ITEM_ID] = item_id
                self.current_item[userid] = item_id
                event_data.pop(self.ITEM)

            elif event_name == EventTypes.PLAYER_DEATH:
                attack_item_id, user_item_id = self.get_player_death_id(event_data)
                event_data.pop(self.WEAPON)
                event_data[self.ITEM_ID] = attack_item_id
                event_data['player_item_id'] = user_item_id

            elif event_name == EventTypes.WEAPON_FIRE:
                item_id = self.get_weapon_fire_id(event_data)
                event_data.pop(self.WEAPON)
                event_data[self.ITEM_ID] = item_id

            elif event_name == EventTypes.PLAYER_HURT:
                item_id = self.get_player_hurt_id(event_data)
                event_data.pop(self.WEAPON)
                event_data[self.ITEM_ID] = item_id

        return self.data

    def get_equip_id(self, event_data, def_index_ids):
        item_name = event_data[self.ITEM].strip()
        defindex = int(event_data[self.DEFINDEX])

        item_id = Item.get_id_with_short_name(item_name)
        if item_name in Item.ALT_WEAPONS:
            item_id = def_index_ids.get(defindex).id
        elif item_name in Item.SUPP_WEAPONS:
            suppressed = DB.custom_bool(event_data[self.HASSILENCER])
            if suppressed:
                item_id = Item.get_suppressed_weapon(item_name)

        return item_id

    def get_player_death_id(self, event_data):
        attack_item_name = event_data[self.WEAPON].strip()
        userid = event_data[self.USER_ID]
        attack_item_id = Item.get_id_with_short_wep(attack_item_name)
        user_item_id = self.current_item.get(userid)

        return attack_item_id, user_item_id

    def get_weapon_fire_id(self, event_data):
        item_name = event_data[self.WEAPON].strip()
        return Item.get_id_with_name(item_name)

    def get_player_hurt_id(self, event_data):
        userid = event_data[self.USER_ID]
        return self.current_item.get(userid)
