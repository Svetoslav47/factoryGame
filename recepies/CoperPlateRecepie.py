from recepies.Recepie import Recepie
from Items import CopperIngot

from Items import CopperPlate


class CopperPlateRecepie(Recepie):
    ingredients = [(CopperIngot, 1)]
    time_to_craft = 1
    result = CopperPlate
    amount = 1

    def can_craft(inventory):
        return Recepie.can_craft(CopperPlateRecepie.ingredients, inventory)

    def get_ingredients():
        return Recepie.get_ingredients(CopperPlateRecepie.ingredients)

    def get_craft_time():
        return Recepie.get_craft_time(CopperPlateRecepie.time_to_craft)

    def get_result(screen):
        return Recepie.get_result(screen, CopperPlateRecepie.result,
                                  CopperPlateRecepie.amount)

    def draw_preview(screen, x, y, box_size):
        return Recepie.draw_preview(screen, x, y, CopperPlateRecepie.result.image, box_size)
