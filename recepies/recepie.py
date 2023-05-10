class Recepie:
    def __init__(self, time_to_craft, screen):
        ingredients = []  # list of tuples (item, amount)
        self.result = None  # tuple (item, amount)
        self.time_to_craft = time_to_craft

    def can_craft(self, inventory):
        for ingredient in self.ingredients:
            if inventory.amount_of_item(ingredient[0]) < ingredient[1]:
                return False
        return True
