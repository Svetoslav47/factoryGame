import pygame

from systems.Inventory import Inventory
from systems.Miner import Miner
from systems.PlayerCrafter import PlayerCrafter
from systems.PlayerHotbar import PlayerHotbar
from systems.PlayerHand import PlayerHand
from systems.PlayerHud import PlayerHud

from tiles.Tile import Tile

from Items import IronOre

from Recepies import RecepiesArray


class Player:
    def __init__(self, grid, screen, clock, x, y, size, speed):
        self.__grid = grid
        self.__screen = screen
        self.__clock = clock
        self.__x = x
        self.__y = y
        self.__size = size
        self.__speed = speed
        self.__inventory = Inventory(screen)
        self.__is_inventory_open = False
        self.__miner = Miner(grid, 1, self.__inventory, clock, is_player=True)
        self.__crafter = PlayerCrafter(screen, clock, self.__inventory)
        self.__hotbar = PlayerHotbar(screen, self, self.__inventory)

        self.__hud = PlayerHud(
            screen, self, self.__inventory, self.__hotbar, RecepiesArray)

        self.__player_hand = PlayerHand(
            screen, self.__grid, self.__clock, self, self.__hotbar, self.__hud)

        self.__hotbar.set_slot(0, IronOre(screen=self.__screen))  # temp

    def __calculate_draw_x_y(self):
        draw_x = self.__screen.get_width() // 2 - self.__size // 2
        draw_y = self.__screen.get_height() // 2 - self.__size // 2
        if self.__x < self.__screen.get_width() // 2:
            draw_x = self.__x - self.__size // 2

        if self.__x > self.__grid.get_width() * self.__grid.get_tile_size() - self.__screen.get_width() // 2:
            draw_x = self.__x - \
                (self.__grid.get_width() * self.__grid.get_tile_size() -
                 self.__screen.get_width()) - self.__size // 2

        if self.__y < self.__screen.get_height() // 2:
            draw_y = self.__y - self.__size // 2

        if self.__y > self.__grid.get_height() * self.__grid.get_tile_size() - self.__screen.get_height() // 2:
            draw_y = self.__y - \
                (self.__grid.get_height() * self.__grid.get_tile_size() -
                 self.__screen.get_height()) - self.__size // 2

        return draw_x, draw_y

    def draw(self, mouse_buttons, mouse_x, mouse_y):
        draw_x, draw_y = self.__calculate_draw_x_y()

        mouse_x_grid, mouse_y_grid = self.__grid.screen_to_grid(
            mouse_x, mouse_y, self)

        is_mining = mouse_buttons[2] and self.__miner.get_mining_tile() != None
        pygame.draw.rect(self.__screen, (255, 0, 0),
                         (draw_x, draw_y, self.__size, self.__size))

        self.__hud.draw(mouse_x, mouse_y,
                        self.__is_inventory_open, is_mining, self.__miner.get_progress(), self.__crafter.get_queue(), self.__crafter.get_crafting_progress())

        self.__player_hand.draw(
            mouse_x, mouse_y, self.__is_inventory_open)

    def update(self, keys, mouse_buttons, mouse_x, mouse_y, events):
        mouse_x_grid, mouse_y_grid = self.__grid.screen_to_grid(
            mouse_x, mouse_y, self)
        if keys[pygame.K_w]:
            self.move(0, -1)
        if keys[pygame.K_s]:
            self.move(0, 1)
        if keys[pygame.K_a]:
            self.move(-1, 0)
        if keys[pygame.K_d]:
            self.move(1, 0)

        left_mouse_button_down_event = False
        right_mouse_button_down_event = False

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    right_mouse_button_down_event = True
                if event.button == 1:
                    left_mouse_button_down_event = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    self.toggle_inventory()

        if left_mouse_button_down_event:
            self.__player_hand.left_click(
                mouse_x, mouse_y, self.__is_inventory_open)
        if self.__is_inventory_open:
            self.is_mining = False

        if mouse_buttons[2] == 1:
            self.__miner.update(mouse_x_grid, mouse_y_grid)

        self.__crafter.update()

    def move(self, x, y):
        x = min(max(x, -1), 1)
        y = min(max(y, -1), 1)
        self.__x += x * self.__speed * (1 / self.__clock.get_fps())
        self.__y += y * self.__speed * (1 / self.__clock.get_fps())

        self.__x = min(max(self.__x, 0), self.__grid.get_width()
                       * self.__grid.get_tile_size())
        self.__y = min(max(self.__y, 0), self.__grid.get_height()
                       * self.__grid.get_tile_size())

    def craft(self, recepie):
        self.__crafter.craft(recepie)

    def toggle_inventory(self):
        self.__is_inventory_open = not self.__is_inventory_open

    def add_item_to_inventory(self, item):
        self.__inventory.add_item(item)

    def get_inventory(self):
        return self.__inventory

    def get_is_inventory_open(self):
        return self.__is_inventory_open

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y
