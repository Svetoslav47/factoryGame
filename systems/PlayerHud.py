import pygame
import math


class PlayerHud:
    def __init__(self, screen, player, inventory, hotbar, recepies):
        self._screen = screen
        self._player = player
        self.__window_screen_size_x = screen.get_width() * 3 / 4
        self.__window_screen_size_y = screen.get_height() * 3 / 4
        self._inventory = inventory
        self._hotbar = hotbar
        # inventory things

        self.__inventory_screen_size_x = self.__window_screen_size_x//2
        self.__inventory_screen_size_y = self.__window_screen_size_y
        self.__inventory_columns = math.floor(self._inventory.get_size()**0.5)
        inventory_box_width = self.__inventory_screen_size_x / \
            (self.__inventory_columns*1.1)
        # acount for the rightmost padding

        number_of_rows = math.ceil(
            self._inventory.get_size() / self.__inventory_columns)
        inventory_box_height = self.__inventory_screen_size_y / \
            (number_of_rows*1.1)
        self.__inventory_box_size = min(
            inventory_box_width, inventory_box_height)

        self.__inventory_box_padding_x = (self.__inventory_screen_size_x - (self.__inventory_box_size * self.__inventory_columns)) / \
            (self.__inventory_columns + 1)
        self.__inventory_box_padding_y = (self.__inventory_screen_size_y - (self.__inventory_box_size * number_of_rows)) / \
            (number_of_rows + 1)

        # hotbar things
        self.__hotbar_screen_size_x = self.__window_screen_size_x / 4 * 3

        self.__hotbar_box_size = self.__hotbar_screen_size_x / \
            (self._hotbar.get_size()*1.1)

        self.__hotbar_screen_size_y = self.__hotbar_box_size * 1.2

        self.__hotbar_box_padding_x = (self.__hotbar_screen_size_x - (self.__hotbar_box_size * self._hotbar.get_size())) / \
            (self._hotbar.get_size() + 1)
        self.__hotbar_box_padding_y = (
            self.__hotbar_screen_size_y - self.__hotbar_box_size) / 2

        # mining progress bar
        self.__mining_progress_bar_width = self.__hotbar_screen_size_x
        self.__mining_progress_bar_height = 10

        # crafting recepies select
        self.__crafting_screen_size_x = self.__window_screen_size_x / 2
        self.__crafting_screen_size_y = self.__window_screen_size_y
        self.__crafting_box_size = self.__crafting_screen_size_y / 5
        self.__crafting_box_padding_x = (self.__crafting_screen_size_x - (self.__crafting_box_size * 3)) / \
            (3 + 1)
        self.__crafting_box_padding_y = (self.__crafting_screen_size_y - (self.__crafting_box_size * 3)) / \
            (3 + 1)

        # crafting queue

        # crafting progress bar

    def is_mouse_in_inventory_window(self, mouse_x, mouse_y):
        return (self._screen.get_width() / 2 - self.__window_screen_size_x / 2 <= mouse_x <= self._screen.get_width() / 2 + self.__window_screen_size_x / 2) and (self._screen.get_height() / 2 - self.__window_screen_size_y / 2 <= mouse_y <= self._screen.get_height() / 2 + self.__window_screen_size_y / 2)

    def __is_mouse_in_player_inventory(self, mouse_x, mouse_y):
        return (self._screen.get_width() / 2 - self.__window_screen_size_x / 2 <= mouse_x <= self._screen.get_width() / 2 - self.__window_screen_size_x / 2 + self.__inventory_screen_size_x) and (self._screen.get_height() / 2 - self.__window_screen_size_y / 2 <= mouse_y <= self._screen.get_height() / 2 - self.__window_screen_size_y / 2 + self.__inventory_screen_size_y)

    def get_box_from_screen(self, mouse_x, mouse_y):
        if self.__is_mouse_in_player_inventory(mouse_x, mouse_y):
            x = math.floor((mouse_x - (self._screen.get_width() / 2 - self.__window_screen_size_x / 2 +
                           self.__inventory_box_padding_x)) / (self.__inventory_box_size + self.__inventory_box_padding_x))
            y = math.floor((mouse_y - (self._screen.get_height() / 2 - self.__window_screen_size_y / 2 +
                           self.__inventory_box_padding_y)) / (self.__inventory_box_size + self.__inventory_box_padding_y))
            return self._inventory, x + y * self.__inventory_columns
        else:
            return None, None

    def draw(self, mouse_x, mouse_y, is_window_open, is_mining, mining_progress, is_crafting, crafting_queue, crafting_progress):
        if is_window_open:
            self.__draw_window()
            self.__draw_inventory()

        self.__draw_hotbar()
        if is_mining:
            self.__draw_mining_progress_bar(mining_progress)

    def __draw_window(self):
        pygame.draw.rect(self._screen, (128, 128, 128), (self._screen.get_width() / 2 - self.__window_screen_size_x / 2,
                                                         self._screen.get_height() / 2 - self.__window_screen_size_y / 2,
                                                         self.__window_screen_size_x,
                                                         self.__window_screen_size_y))

    def __draw_inventory(self):
        for x in range(self.__inventory_columns):
            for y in range(math.ceil(self._inventory.get_size() / self.__inventory_columns)):

                box_x = self._screen.get_width() // 2 - self.__inventory_screen_size_x + self.__inventory_box_padding_x + \
                    x * (self.__inventory_box_size +
                         self.__inventory_box_padding_x)
                box_y = self._screen.get_height() // 2 - self.__inventory_screen_size_y // 2 + self.__inventory_box_padding_y + \
                    y * (self.__inventory_box_size +
                         self.__inventory_box_padding_y)

                if y*self.__inventory_columns + x > self._inventory.get_size() - 1:
                    break

                pygame.draw.rect(self._screen, (255, 255, 255),
                                 (box_x, box_y, self.__inventory_box_size, self.__inventory_box_size))

                # draw box index
                # text = pygame.font.SysFont("arial", 20).render(
                #     str(y*self.__inventory_columns + x), True, (0, 0, 0))
                # textRect = text.get_rect()
                # textRect.center = (box_x + self.__inventory_box_size //
                #                    2, box_y + self.__inventory_box_size // 2)
                # self._screen.blit(text, textRect)

                if self._inventory.get_slot(y*self.__inventory_columns + x) != None:
                    self._inventory.get_slot(y*self.__inventory_columns + x).drawInInventory(
                        box_x, box_y, self.__inventory_box_size)

    def __draw_hotbar(self):
        # draw hotbar background
        pygame.draw.rect(self._screen, (128, 128, 128), (self._screen.get_width() // 2 - self.__hotbar_screen_size_x // 2, self._screen.get_height() - self.__hotbar_screen_size_y,
                                                         self.__hotbar_screen_size_x, self.__hotbar_screen_size_y))

        # draw hotbar boxes
        for i in range(self._hotbar.get_size()):
            box_x = self._screen.get_width() // 2 - self.__hotbar_screen_size_x // 2 + self.__hotbar_box_padding_x + \
                i * (self.__hotbar_box_size + self.__hotbar_box_padding_x)
            box_y = self._screen.get_height() - self.__hotbar_screen_size_y + \
                self.__hotbar_box_padding_y

            pygame.draw.rect(self._screen, (255, 255, 255),
                             (box_x, box_y, self.__hotbar_box_size, self.__hotbar_box_size))

            if self._hotbar.get_slot(i)[0] != None:
                self._hotbar.get_slot(i)[0].drawInHotbar(
                    box_x, box_y, self.__hotbar_box_size, self._hotbar.get_slot(i)[1])

    def __draw_mining_progress_bar(self, mining_progress):
        # draw mining progress bar background 10 px above hotbar
        pygame.draw.rect(self._screen, (128, 128, 128), (self._screen.get_width() // 2 - self.__mining_progress_bar_width // 2,
                                                         self._screen.get_height() - self.__hotbar_screen_size_y -
                                                         10 - self.__mining_progress_bar_height,
                                                         self.__mining_progress_bar_width, self.__mining_progress_bar_height))

        # draw mining progress bar
        pygame.draw.rect(self._screen, (0, 128, 0), (self._screen.get_width() // 2 - self.__mining_progress_bar_width // 2,
                                                     self._screen.get_height() - self.__hotbar_screen_size_y -
                                                     10 - self.__mining_progress_bar_height,
                                                     self.__mining_progress_bar_width * mining_progress, self.__mining_progress_bar_height))
