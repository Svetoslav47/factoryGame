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

        self.__inventory_rows = math.ceil(
            self._inventory.get_size() / self.__inventory_columns)
        inventory_box_height = self.__inventory_screen_size_y / \
            (self.__inventory_rows*1.1)
        self.__inventory_box_size = min(
            inventory_box_width, inventory_box_height)

        self.__inventory_box_padding_x = (self.__inventory_screen_size_x - (self.__inventory_box_size * self.__inventory_columns)) / \
            (self.__inventory_columns + 1)
        self.__inventory_box_padding_y = (self.__inventory_screen_size_y - (self.__inventory_box_size * self.__inventory_rows)) / \
            (self.__inventory_rows + 1)

        self._building_open = False

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
        self.__recepies = recepies
        self.__recepie_screen_size_x = self.__window_screen_size_x - \
            self.__inventory_screen_size_x
        self.__recepie_screen_size_y = self.__window_screen_size_y

        self.__recepie_screen_columns = math.floor(
            len(recepies)**0.5)

        crafting_recepie_box_width = self.__recepie_screen_size_x / \
            (self.__recepie_screen_columns*1.1)

        self.__recepie_screen_rows = math.ceil(
            len(recepies) / self.__recepie_screen_columns)
        crafting_recepie_box_height = self.__recepie_screen_size_y / \
            (self.__recepie_screen_rows*1.1)

        self.__recepie_box_size = min(
            crafting_recepie_box_width, crafting_recepie_box_height)

        self.__recepie_box_padding_x = (self.__recepie_screen_size_x - (self.__recepie_box_size * self.__recepie_screen_columns)) / \
            (self.__recepie_screen_columns + 1)
        self.__recepie_box_padding_y = (self.__recepie_screen_size_y - (self.__recepie_box_size * self.__recepie_screen_rows)) / \
            (self.__recepie_screen_rows + 1)

        # crafting queue
        self.__recepie_queue = []

    def is_mouse_in_inventory_window(self, mouse_x, mouse_y):
        return (self._screen.get_width() / 2 - self.__window_screen_size_x / 2 <= mouse_x <= self._screen.get_width() / 2 + self.__window_screen_size_x / 2) and (self._screen.get_height() / 2 - self.__window_screen_size_y / 2 <= mouse_y <= self._screen.get_height() / 2 + self.__window_screen_size_y / 2)

    def _is_mouse_in_player_inventory(self, mouse_x, mouse_y):
        return (self._screen.get_width() / 2 - self.__window_screen_size_x / 2 <= mouse_x <= self._screen.get_width() / 2 - self.__window_screen_size_x / 2 + self.__inventory_screen_size_x) and (self._screen.get_height() / 2 - self.__window_screen_size_y / 2 <= mouse_y <= self._screen.get_height() / 2 - self.__window_screen_size_y / 2 + self.__inventory_screen_size_y)

    def _is_mouse_in_building_inventory(self, mouse_x, mouse_y):
        if self._building_open is None:
            return False

        return (self._screen.get_width() / 2 + self.__window_screen_size_x / 2 - self.__recepie_screen_size_x <= mouse_x <= self._screen.get_width() / 2 + self.__window_screen_size_x / 2) and (self._screen.get_height() / 2 - self.__window_screen_size_y / 2 <= mouse_y <= self._screen.get_height() / 2 - self.__window_screen_size_y / 2 + self.__recepie_screen_size_y)

    def is_mouse_in_player_recipies(self, mouse_x, mouse_y):
        if self._building_open is not None:
            return False

        return (self._screen.get_width() / 2 + self.__window_screen_size_x / 2 - self.__recepie_screen_size_x <= mouse_x <= self._screen.get_width() / 2 + self.__window_screen_size_x / 2) and (self._screen.get_height() / 2 - self.__window_screen_size_y / 2 <= mouse_y <= self._screen.get_height() / 2 - self.__window_screen_size_y / 2 + self.__recepie_screen_size_y)

    def is_mouse_in_hotbar(self, mouse_x, mouse_y):
        return (self._screen.get_width() / 2 - self.__window_screen_size_x / 2 <= mouse_x <= self._screen.get_width() / 2 + self.__window_screen_size_x / 2) and (self._screen.get_height() / 2 + self.__window_screen_size_y / 2 - self.__hotbar_screen_size_y <= mouse_y <= self._screen.get_height() / 2 + self.__window_screen_size_y / 2)

    def get_recepie_from_screen(self, mouse_x, mouse_y):
        recepie_index = None
        if self.is_mouse_in_player_recipies(mouse_x, mouse_y):
            x = math.floor((mouse_x - (self._screen.get_width() / 2 + self.__window_screen_size_x / 2 - self.__recepie_screen_size_x +
                            self.__recepie_box_padding_x)) / (self.__recepie_box_size + self.__recepie_box_padding_x))
            y = math.floor((mouse_y - (self._screen.get_height() / 2 - self.__window_screen_size_y / 2 +
                            self.__recepie_box_padding_y)) / (self.__recepie_box_size + self.__recepie_box_padding_y))
            recepie_index = x + y * self.__recepie_screen_columns

            # if the mouse is between the boxes
            box_x = self._screen.get_width() / 2 + self.__window_screen_size_x / 2 - self.__recepie_screen_size_x + \
                self.__recepie_box_padding_x + \
                (self.__recepie_box_size + self.__recepie_box_padding_x) * x

            box_y = self._screen.get_height() / 2 - self.__window_screen_size_y / 2 + \
                self.__recepie_box_padding_y + \
                (self.__recepie_box_size + self.__recepie_box_padding_y) * y

            if mouse_x < box_x or mouse_x > box_x + self.__recepie_box_size or mouse_y < box_y or mouse_y > box_y + self.__recepie_box_size:
                recepie_index = None

        if recepie_index is None:
            return None

        if recepie_index >= len(self.__recepies) or recepie_index < 0:
            return None

        return self.__recepies[recepie_index]

    def get_box_from_screen(self, mouse_x, mouse_y):
        if self._is_mouse_in_player_inventory(mouse_x, mouse_y):
            x = math.floor((mouse_x - (self._screen.get_width() / 2 - self.__window_screen_size_x / 2 +
                           self.__inventory_box_padding_x)) / (self.__inventory_box_size + self.__inventory_box_padding_x))
            y = math.floor((mouse_y - (self._screen.get_height() / 2 - self.__window_screen_size_y / 2 +
                           self.__inventory_box_padding_y)) / (self.__inventory_box_size + self.__inventory_box_padding_y))
            return self._inventory, x + y * self.__inventory_columns
        elif self._building_open is not None and self._is_mouse_in_building_inventory(mouse_x, mouse_y):
            # self, mouse_x, mouse_y, draw_x, draw_y, draw_zone_width, draw_zone_height
            return self._building_open.get_box_from_inventory(mouse_x, mouse_y, self._screen.get_width() / 2 + self.__window_screen_size_x / 2 - self.__recepie_screen_size_x,
                                                              self._screen.get_height() / 2 - self.__window_screen_size_y /
                                                              2, self.__recepie_screen_size_x - self.__recepie_box_padding_x,
                                                              self.__recepie_screen_size_y - self.__recepie_box_padding_y)
        else:
            return None, None

    def draw(self, mouse_x, mouse_y, is_window_open, building_open, is_mining, mining_progress, crafting_queue, crafting_progress):
        self.__draw_hotbar()
        self._building_open = building_open
        if is_window_open:
            self.__draw_window()
            self.__draw_inventory()
            if building_open is not None:
                draw_x = self._screen.get_width() // 2 - self.__window_screen_size_x // 2 + \
                    self.__inventory_screen_size_x
                draw_y = self._screen.get_height() // 2 - self.__window_screen_size_y // 2

                draw_zone_width = self.__window_screen_size_x - self.__inventory_screen_size_x
                draw_zone_height = self.__window_screen_size_y

                building_open.draw_inventory(
                    self._screen, draw_x, draw_y, draw_zone_width, draw_zone_height)
            else:
                self.__draw_crafting_recepies(mouse_x, mouse_y)

        if is_mining:
            self.__draw_mining_progress_bar(mining_progress)

        if len(crafting_queue) > 0:
            self.__draw_crafting_queue(crafting_queue, crafting_progress)

    def __draw_window(self):
        pygame.draw.rect(self._screen, (128, 128, 128), (self._screen.get_width() / 2 - self.__window_screen_size_x / 2,
                                                         self._screen.get_height() / 2 - self.__window_screen_size_y / 2,
                                                         self.__window_screen_size_x,
                                                         self.__window_screen_size_y))

    def __draw_inventory(self):
        for x in range(self.__inventory_columns):
            for y in range(self.__inventory_rows):

                box_x = self._screen.get_width() // 2 - self.__window_screen_size_x // 2 + self.__inventory_box_padding_x + \
                    x * (self.__inventory_box_size +
                         self.__inventory_box_padding_x)
                box_y = self._screen.get_height() // 2 - self.__window_screen_size_y // 2 + self.__inventory_box_padding_y + \
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

            slot = self._hotbar.get_slot(i)
            if slot[0] != None:
                slot[0].drawInHotbar(
                    box_x, box_y, self.__hotbar_box_size, slot[1])

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

    def __draw_crafting_recepies(self, mouse_x, mouse_y):

        for i in range(self.__recepie_screen_columns):
            for j in range(self.__recepie_screen_rows):
                box_x = self._screen.get_width() // 2 - self.__window_screen_size_x // 2 + self.__inventory_screen_size_x + self.__recepie_box_padding_x + \
                    i * (self.__recepie_box_size +
                         self.__recepie_box_padding_x)
                box_y = self._screen.get_height() // 2 - self.__window_screen_size_y // 2 + self.__recepie_box_padding_y + \
                    j * (self.__recepie_box_size +
                         self.__recepie_box_padding_y)

                if j*self.__recepie_screen_columns + i > len(self.__recepies) - 1:
                    break

                pygame.draw.rect(self._screen, (255, 255, 255),
                                 (box_x, box_y, self.__recepie_box_size, self.__recepie_box_size))

                self.__recepies[j*self.__recepie_screen_columns + i].draw_preview(
                    self._screen, box_x, box_y, self.__recepie_box_size)

        hovered_recepie = self.get_recepie_from_screen(mouse_x, mouse_y)
        if hovered_recepie != None:
            ingredients = hovered_recepie.get_ingredients()
            ingredient_box_size = 40
            hover_width = 230
            hover_height = 0.2*ingredient_box_size + \
                (ingredient_box_size + 0.2 *
                 ingredient_box_size) * len(ingredients)
            pygame.draw.rect(self._screen, (180, 180, 180),
                             (mouse_x, mouse_y, hover_width, hover_height))
            for k in range(len(ingredients)):
                ingredients[k][0].draw_item_preview(self._screen,
                                                    mouse_x + ingredient_box_size*0.2, mouse_y + ingredient_box_size*0.2 * (k+1) + (ingredient_box_size) * k, ingredient_box_size)

                text = pygame.font.SysFont("arial", 20).render(
                    f"{ingredients[k][0].item_name}: {ingredients[k][1]}", True, (0, 0, 0))
                textRect = text.get_rect()
                textRect.center = (mouse_x + ingredient_box_size*0.2 + ingredient_box_size + textRect.width // 2, mouse_y +
                                   ingredient_box_size*0.2 * (k+1) + (ingredient_box_size) * k + ingredient_box_size//2)
                self._screen.blit(text, textRect)

    def __draw_crafting_queue(self, crafting_queue, crafting_progress):
        box_size = 40
        box_padding = box_size * 0.2
        for i in range(len(crafting_queue)):
            box_x = box_padding + \
                i * (box_size + box_padding)
            box_y = box_padding

            pygame.draw.rect(self._screen, (255, 255, 255),
                             (box_x, box_y, box_size, box_size))

            crafting_queue[i].draw_preview(
                self._screen, box_x, box_y, box_size)

        # draw crafting progress bar
        bar_x = + box_padding
        bar_y = box_padding + box_size + box_padding * 2
        bar_width = box_size
        bar_height = 10
        pygame.draw.rect(self._screen, (180, 180, 180), (bar_x, bar_y,
                                                         bar_width, bar_height))

        pygame.draw.rect(self._screen, (80, 80, 80), (bar_x, bar_y,
                                                      bar_width * crafting_progress, bar_height))
