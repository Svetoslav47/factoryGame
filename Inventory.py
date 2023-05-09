import pygame
import math


class Inventory:
    def __init__(self, screen, inventory_size=35):
        self.screen = screen
        self.inventory_size = inventory_size
        self.inventory = [None for x in range(self.inventory_size)]

    def amount_of_item(self, item_id):
        amount = 0
        for x in range(self.inventory_size):
            if self.inventory[x] != None and self.inventory[x].item_id == item_id:
                amount += self.inventory[x].amount
        return amount

    def add_item(self, item):
        for x in range(self.inventory_size):
            if self.inventory[x] != None and self.inventory[x].item_id == item.item_id:
                if self.inventory[x].stack_size - self.inventory[x].amount > 0:
                    if self.inventory[x].stack_size - self.inventory[x].amount >= item.amount:
                        self.inventory[x].amount += item.amount
                        return True
                    else:
                        item.amount -= self.inventory[x].stack_size - \
                            self.inventory[x].amount
                        self.inventory[x].amount = self.inventory[x].stack_size
                        return self.add_item(item)

        for x in range(self.inventory_size):
            if self.inventory[x] == None:
                self.inventory[x] = item
                return True

        return False

    def remove_item(self, item_id, amount):
        if amount_of_item(item_id) < amount:
            return False

        for x in range(self.inventory_size):
            if self.inventory[x] != None and self.inventory[x].item_id == item_id:
                if self.inventory[x].amount - amount > 0:
                    self.inventory[x].amount -= amount
                    return True
                else:
                    amount -= self.inventory[x].amount
                    self.inventory[x] = None
                    return self.remove_item(item_id, amount)

        return False
