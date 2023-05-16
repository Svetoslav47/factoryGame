from systems.Inventory import Inventory
import math
import pygame


class PlayerInventory(Inventory):
    def __init__(self, screen, player):
        super().__init__(screen, 35)
        self.__player = player
        self.__screen_size_x = screen.get_width() * 3 / 4
        self.__screen_size_y = screen.get_height() * 3 / 4
        self.__inventory_screen_size_x = self.__screen_size_x//2
        self.__inventory_screen_size_y = self.__screen_size_y
        self.__columns = 5
        box_width = self.__inventory_screen_size_x / (self.__columns*1.1)
        # acount for the rightmost padding

        number_of_rows = math.ceil(self._inventory_size / self.__columns)
        box_height = self.__inventory_screen_size_y / (number_of_rows*1.1)
        self.__box_size = min(box_width, box_height)

        self.__box_padding_x = (self.__inventory_screen_size_x - (self.__box_size * self.__columns)) / \
            (self.__columns + 1)
        self.__box_padding_y = (self.__inventory_screen_size_y - (self.__box_size * number_of_rows)) / \
            (number_of_rows + 1)

    def draw(self):
        # Draw the inventory background at the middle of the screen
        pygame.draw.rect(self._screen, (128, 128, 128), (self._screen.get_width() // 2 - self.__screen_size_x // 2,
                                                         self._screen.get_height() // 2 - self.__screen_size_y // 2, self.__screen_size_x, self.__screen_size_y))

        for x in range(self.__columns):
            for y in range(math.ceil(self._inventory_size / self.__columns)):

                box_x = self._screen.get_width() // 2 - self.__screen_size_x // 2 + self.__box_padding_x + \
                    x * (self.__box_size + self.__box_padding_x)
                box_y = self._screen.get_height() // 2 - self.__screen_size_y // 2 + self.__box_padding_y + \
                    y * (self.__box_size + self.__box_padding_y)

                pygame.draw.rect(self._screen, (255, 255, 255),
                                 (box_x, box_y, self.__box_size, self.__box_size))

                # draw box index
                # text = pygame.font.SysFont("arial", 20).render(
                #     str(y*self.__columns + x), True, (0, 0, 0))
                # textRect = text.get_rect()
                # textRect.center = (box_x + self.__box_size //
                #                    2, box_y + self.__box_size // 2)
                # self._screen.blit(text, textRect)

                if self._inventory[y*self.__columns + x] != None:
                    self._inventory[y*self.__columns + x].drawInInventory(
                        box_x, box_y, self.__box_size)

    def get_box_index_from_screen(self, mouse_x, mouse_y):
        mouse_x -= self._screen.get_width() // 2 - self.__screen_size_x // 2
        mouse_y -= self._screen.get_height() // 2 - self.__screen_size_y // 2

        mouse_x -= self.__box_padding_x
        mouse_y -= self.__box_padding_y

        if mouse_x < 0 or mouse_y < 0:
            return None

        if mouse_x > self.__inventory_screen_size_x or mouse_y > self.__inventory_screen_size_y:
            return None

        mouse_x_index = int(
            mouse_x // (self.__box_size + self.__box_padding_x))
        mouse_y_index = int(
            mouse_y // (self.__box_size + self.__box_padding_y))

        print(mouse_y_index * self.__columns + mouse_x_index)
        return mouse_y_index * self.__columns + mouse_x_index

    def is_mouse_in_inventory_screen(self, mouse_x, mouse_y):
        inventory_x = self._screen.get_width() // 2 - \
            self.__screen_size_x // 2
        inventory_y = self._screen.get_height() // 2 - \
            self.__screen_size_y // 2

        if not mouse_x > inventory_x:
            return False

        if not mouse_x < inventory_x + self.__screen_size_x:
            return False

        if not mouse_y > inventory_y:
            return False

        if not mouse_y < inventory_y + self.__screen_size_y:
            return False

        return True

    def get_screen_size(self):
        return (self.__screen_size_x, self.__screen_size_y)
