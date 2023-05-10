from recepies.Recepie import Recepie
from items.Items import CopperPlate


class CopperPlateRecepie(Recepie):
    def __init__(self, screen):
        super().__init__(time_to_craft=1, screen=screen)
        self.ingredients = [("copper_ingot", 1)]
        self.result = CopperPlate(1)
