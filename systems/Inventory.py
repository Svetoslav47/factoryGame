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
            if self._inventory[x] != None and self._inventory[x].item_id == item_id:
                amount += self._inventory[x].get_amount()
        return amount

    def add_item(self, item):
        for x in range(self._inventory_size):
            if self._inventory[x] != None and self._inventory[x].item_id == item.item_id:
                if self._inventory[x].get_stack_size() - self._inventory[x].get_amount() > 0:
                    if self._inventory[x].get_stack_size() - self._inventory[x].get_amount() >= item.get_amount():
                        self._inventory[x].set_amount(
                            self._inventory[x].get_amount() + item.get_amount())
                        return True
                    else:

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
        if self.amount_of_item(item_id) < amount:
            return False

        for x in range(self._inventory_size):
            if self._inventory[x] != None and self._inventory[x].item_id == item_id:
                if self._inventory[x].get_amount() - amount > 0:
                    self._inventory[x].set_amount(
                        self._inventory[x].get_amount() - amount)
                    return True
                else:
                    amount -= self._inventory[x].get_amount()
                    self._inventory[x] = None
                    if amount == 0:
                        return True
                    return self.remove_item(item_id, amount)

        return False

    def get_slot(self, index):
        if index < 0 or index >= self._inventory_size or index is None:
            return None
        return self._inventory[index]

    def get_slot_with_item(self):
        for x in range(self._inventory_size):
            if self._inventory[x] != None:
                return x

        return None

    def pop_slot(self, index):
        item = self._inventory[index]
        self._inventory[index] = None
        return item

    def pop_slot_with_item(self, item_id):
        for x in range(self._inventory_size):
            if self._inventory[x] != None and self._inventory[x].item_id == item_id:
                item = self._inventory[x]
                self._inventory[x] = None
                return item

        return None

    def get_size(self):
        return self._inventory_size

    def has_space_for_item(self, item_id, stack_size, amount):
        space_available = 0
        for x in range(self._inventory_size):
            if self._inventory[x] == None:
                space_available += stack_size
                if space_available >= stack_size:
                    return True
            if self._inventory[x].item_id == item_id:
                space_available += stack_size - \
                    self._inventory[x].get_amount()
                if space_available >= amount:
                    return True

        if space_available >= amount:
            return True

        return False

    def set_slot(self, index, item):
        if self._inventory[index] == None:
            self._inventory[index] = item
            return True

        return False
