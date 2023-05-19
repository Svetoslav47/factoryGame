import pygame
from buildings.Building import Building


class PlayerHotbar:
    def __init__(self, screen, player, inventory):
        self.__screen = screen
        self.__player = player
        self.__inventory = inventory
        self.__hotbarSize = 10
        self.__hotbar = [None] * self.__hotbarSize
        self.__selected = None
        self.__box_size = 40
        self.__box_padding = self.__box_size // 10

    def select(self, index):
        if index == self.__selected:
            self.__selected = None
        elif index == None:
            self.__selected = None
        elif index < len(self.__hotbar) and self.__hotbar[index] != None:
            self.__selected = index

    def get_selected_item(self):
        if self.__selected == -1:
            return None
        return self.__hotbar[self.__selected]

    def is_selected_item_buildable(self):
        if self.__selected == -1:
            return False
        return self.__hotbar[self.__selected].is_buildable()

    def set_slot(self, index, item):
        self.__hotbar[index] = item

    def get_slot(self, index):
        return (self.__hotbar[index], self.__inventory.amount_of_item(self.__hotbar[index]))

    def get_size(self):
        return self.__hotbarSize

    def get_selected(self):
        return self.__selected
