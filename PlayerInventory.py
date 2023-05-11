from systems.Inventory import Inventory
import math
import pygame


class PlayerInventory(Inventory):
    def __init__(self, screen, player):
        super().__init__(screen, 35)
        self.__player = player
        self.__screen_size_x = screen.get_width() * 3 / 4
        self.__screen_size_y = screen.get_height() * 3 / 4
        self.__columns = 5
        self.__box_size = self.__screen_size_x / \
            (math.ceil(self._inventory_size / self.__columns) * 1.49)
        self.__box_padding = self.__box_size / 10

    def draw(self):
        # Draw the inventory background at the middle of the screen
        pygame.draw.rect(self._screen, (128, 128, 128), (self._screen.get_width() // 2 - self.__screen_size_x // 2,
                                                         self._screen.get_height() // 2 - self.__screen_size_y // 2, self.__screen_size_x, self.__screen_size_y))

        for x in range(self.__columns):
            for y in range(math.ceil(self._inventory_size / self.__columns)):

                if y*self.__columns + x >= self._inventory_size:
                    break

                box_x = self._screen.get_width() // 2 - self.__screen_size_x // 2 + \
                    self.__box_padding + x * \
                    (self.__box_size + self.__box_padding)

                box_y = self._screen.get_height() // 2 - self.__screen_size_y // 2 + \
                    self.__box_padding + y * \
                    (self.__box_size + self.__box_padding)

                pygame.draw.rect(self._screen, (255, 255, 255),
                                 (box_x, box_y, self.__box_size, self.__box_size))

                if self._inventory[y*self.__columns + x] != None:
                    self._inventory[y*self.__columns + x].drawInInventory(
                        box_x, box_y, self.__box_size)
