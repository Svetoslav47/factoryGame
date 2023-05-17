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

    def draw(self, mouse_x_grid, mouse_y_grid):
        # Draw the hotbar background at the bottom of the screen
        total_width = self.__box_size * self.__hotbarSize + self.__box_padding * \
            (self.__hotbarSize + 1)

        pygame.draw.rect(self.__screen, (128, 128, 128), ((self.__screen.get_width() - total_width) // 2,
                                                          self.__screen.get_height() - self.__box_size - self.__box_padding * 2, total_width, self.__box_size + self.__box_padding * 2))
        for x in range(self.__hotbarSize):
            box_x = (self.__screen.get_width() - total_width) // 2 + \
                self.__box_padding + x * \
                (self.__box_size + self.__box_padding)
            box_y = self.__screen.get_height() - self.__box_size - self.__box_padding

            pygame.draw.rect(self.__screen, (255, 255, 255),
                             (box_x, box_y, self.__box_size, self.__box_size))

            if self.__hotbar[x] == None:
                continue

            if self.__selected == x:
                pygame.draw.rect(self.__screen, (255, 0, 0),
                                 (box_x, box_y, self.__box_size, self.__box_size), 5)

            amount = self.__inventory.amount_of_item(
                self.__hotbar[x].get_item_id())

            if self.__hotbar[x] != None:
                self.__hotbar[x].drawInHotbar(
                    box_x, box_y, self.__box_size, amount)

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

    def get_selected(self):
        return self.__selected
