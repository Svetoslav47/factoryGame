class Recepie:
    def __init__(self, screen, ingredients, result, time_to_craft, amount=1):
        self._screen = screen
        self._ingredients = []  # list of tuples (item_id, amount)
        self._result = None  # Item class
        self._amount = amount
        self._time_to_craft = time_to_craft

    def can_craft(self, inventory):
        for ingredient in self._ingredients:
            if inventory.amount_of_item(ingredient[0]) < ingredient[1]:
                return False
        return True

    def get_craft_time(self, craft_speed):
        return self._time_to_craft / craft_speed

    def get_result(self):
        return self._result, self._amount
