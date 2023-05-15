import pygame
import math


class Inventory:
    def __init__(self, screen, inventory_size=35):
        self._screen = screen
        self._inventory_size = inventory_size
        self._inventory = [None for x in range(self._inventory_size)]

    def amount_of_item(self, item_id):
        amount = 0
        for x in range(self._inventory_size):
            if self._inventory[x] != None and self._inventory[x].get_item_id() == item_id:
                amount += self._inventory[x].get_amount()
        return amount

    def add_item(self, item):
        for x in range(self._inventory_size):
            if self._inventory[x] != None and self._inventory[x].get_item_id() == item.get_item_id():
                if self._inventory[x].get_stack_size() - self._inventory[x].get_amount() > 0:
                    if self._inventory[x].get_stack_size() - self._inventory[x].get_amount() >= item.get_amount():
                        self._inventory[x].set_amount(
                            self._inventory[x].get_amount() + item.get_amount())
                        return True
                    else:
                        print(
                            f"Item {item.get_item_id()} is too big to fit in the stack. Splitting...")
                        print(f"Item amount: {item.get_amount()}")
                        print(
                            f"Stack size: {self._inventory[x].get_stack_size()}")
                        print(
                            f"Stack amount: {self._inventory[x].get_amount()}")

                        item.set_amount(item.get_amount() - (self._inventory[x].get_stack_size() -
                                        self._inventory[x].get_amount()))

                        self._inventory[x].set_amount(self._inventory[x].get_stack_size(
                        ))
                        return self.add_item(item)

        for x in range(self._inventory_size):
            if self._inventory[x] == None:
                self._inventory[x] = item
                return True

        return False

    def remove_item(self, item_id, amount):
        if amount_of_item(item_id) < amount:
            return False

        for x in range(self._inventory_size):
            if self._inventory[x] != None and self._inventory[x].item_id == item_id:
                if self._inventory[x].amount - amount > 0:
                    self._inventory[x].amount -= amount
                    return True
                else:
                    amount -= self._inventory[x].amount
                    self._inventory[x] = None
                    return self.remove_item(item_id, amount)

        return False
