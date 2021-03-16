from csgo_analysis.ingestion.models import Item
from csgo_analysis.ingestion.models.db import DB
from csgo_analysis.ingestion.const import EventTypes


class ItemController:

    DEFINDEX = 'defindex'
    HASSILENCER = 'hassilencer'
    ITEM = 'item'
    WEAPON = 'weapon'
    ITEM_ID = 'item_id'
    USER_ID = 'userid'

    WEP_INDEX_L = {
        1: Item.DEAGLE,
        36: Item.P250,
        63: Item.CZ75A,
        64: Item.REVOLVER
    }

    def __init__(self, data, player_list):
        self.data = data
        self.current_item = {player: None for player in player_list}

    def sub_item_id(self):

        for event in self.data:
            event_name = list(event.keys())[0]
            event_data = event[event_name]

            if self.USER_ID in event_data.keys() and \
                    event_data[self.USER_ID] not in self.current_item.keys():
                continue

            if event_name == EventTypes.ITEM_EQUIP:
                item_id = self._get_equip_id(event_data)
                userid = event_data[self.USER_ID]
                event_data[self.ITEM_ID] = item_id
                self.current_item[userid] = item_id
                event_data.pop(self.ITEM)

            elif event_name == EventTypes.PLAYER_DEATH:
                attack_item_id, user_item_id = self._get_player_death_id(event_data)
                event_data.pop(self.WEAPON)
                event_data[self.ITEM_ID] = attack_item_id
                event_data['player_item_id'] = user_item_id

            elif event_name == EventTypes.WEAPON_FIRE:
                item_id = self._get_weapon_fire_id(event_data)
                event_data.pop(self.WEAPON)
                event_data[self.ITEM_ID] = item_id

            elif event_name == EventTypes.PLAYER_HURT:
                item_id = self.get_player_hurt_id(event_data)
                event_data.pop(self.WEAPON)
                event_data[self.ITEM_ID] = item_id

        return self.data

    def _get_equip_id(self, event_data):
        item_name = event_data[self.ITEM].strip()
        defindex = int(event_data[self.DEFINDEX])

        item_id = Item.get_id_with_short_name(item_name)
        if item_name in Item.ALT_WEAPONS:
            item_id = self.WEP_INDEX_L.get(defindex).id
        elif item_name in Item.SUPP_WEAPONS:
            suppressed = DB.custom_bool(event_data[self.HASSILENCER])
            if suppressed:
                item_id = Item.get_suppressed_weapon(item_name)

        return item_id

    def _get_player_death_id(self, event_data):
        attack_item_name = event_data[self.WEAPON].strip()
        userid = event_data[self.USER_ID]
        attack_item_id = Item.get_id_with_short_wep(attack_item_name)
        user_item_id = self.current_item.get(userid)

        return attack_item_id, user_item_id

    def _get_weapon_fire_id(self, event_data):
        item_name = event_data[self.WEAPON].strip()
        return Item.get_id_with_name(item_name)

    def get_player_hurt_id(self, event_data):
        userid = event_data[self.USER_ID]
        return self.current_item.get(userid)
