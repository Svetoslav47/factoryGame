from recepies.Recepie import Recepie
from items.Items import CopperPlate


class CopperPlateRecepie(Recepie):
    def __init__(self):
        super().__init__(time_to_craft=1)
        self.ingredients = [("copper_ingot", 1)]
        self.result = (CopperPlate, 1)
