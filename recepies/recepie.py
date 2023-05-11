class Recepie:
    def __init__(self, screen, ingredients, result, time_to_craft):
        self._screen = screen
        self._ingredients = []  # list of tuples (item_id, amount)
        self._result = None  # Item object
        self._time_to_craft = time_to_craft

    def can_craft(self, inventory):
        for ingredient in self._ingredients:
            if inventory.amount_of_item(ingredient[0]) < ingredient[1]:
                return False
        return True
