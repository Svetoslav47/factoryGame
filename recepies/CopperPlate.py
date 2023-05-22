from recepies.Recepie import Recepie
from Items import CopperIngot

from Items import CopperPlate

ingredients = [(CopperIngot, 1)]
time_to_craft = 1
result = CopperPlate
amount = 1


class CopperPlate(Recepie):
    ingredients = ingredients
    time_to_craft = time_to_craft
    result = result
    amount = amount

    def can_craft(inventory):
        return Recepie.can_craft(ingredients, inventory)

    def get_ingredients():
        return Recepie.get_ingredients(ingredients)

    def get_craft_time():
        return Recepie.get_craft_time(time_to_craft)

    def get_result(screen):
        return Recepie.get_result(screen, result,
                                  amount)

    def draw_preview(screen, x, y, box_size):
        return result.draw_item_preview(screen, x, y, box_size)
