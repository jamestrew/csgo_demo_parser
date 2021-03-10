import re
from csgo_analysis.ingestion.models import Item


class ItemController:

    DEAGLE_MODEL_P = r' (\d+), models\/[a-z]weapons\/v_pist_deagle.mdl'
    P250_MODEL_P = r' (\d+), models\/[a-z]weapons\/v_pist_p250.mdl'
    DEAGLE_DEFINDEX_P = r' item: deagle\s+defindex: (\d+)'
    P250_DEFINDEX_P = r' item: p250\s+defindex: (\d+)'

    def __init__(self, data):
        self.data = data

    def get_model_index(self):
        model_dict = {}
        deagle_model = re.search(self.DEAGLE_MODEL_P, self.data).group(1)
        p250_model = re.search(self.P250_MODEL_P, self.data).group(1)

        model_dict[int(deagle_model)] = Item.DEAGLE
        model_dict[int(p250_model)] = Item.P250
        return model_dict

    def get_defindex(self):
        def_indices = {}
        deagle_defindex = re.findall(self.DEAGLE_DEFINDEX_P, self.data)
        def_indices[Item.DEAGLE] = tuple(map(int, deagle_defindex))

        p250_defindex = re.findall(self.P250_DEFINDEX_P, self.data)
        def_indices[Item.P250] = tuple(map(int, p250_defindex))
        return def_indices

    def get_def_model_index(self):
        index_dict = {}
        for item, indices in self.get_defindex().items():
            for index in indices:
                p = r'402, m_iItemDefinitionIndex = $.+?429, m_nModelIndex = (\d+)'
                p = p.replace('$', str(index))
                pattern = re.compile(p, re.DOTALL | re.MULTILINE)
                match = re.search(pattern, self.data)
                if match is None:
                    index_dict[index] = item
                    continue
                index_dict[index] = int(match.group(1))

        return index_dict

    def get_def_index_ids(self):
        index_item_dict = {}
        for defindex, modelindex in self.get_def_model_index().items():
            if modelindex == Item.DEAGLE:
                index_item_dict[defindex] = Item.REVOLVER
            elif modelindex == Item.P250:
                index_item_dict[defindex] = Item.CZ75A
            else:
                index_item_dict[defindex] = self.get_model_index()[modelindex]

        return index_item_dict
