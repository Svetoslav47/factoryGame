import pygame

from PlayerInventory import PlayerInventory
from systems.Miner import Miner

from tiles.Tile import Tile


class Player:
    def __init__(self, grid, screen, clock, x, y, size, speed):
        self.__grid = grid
        self.__screen = screen
        self.__clock = clock
        self.__x = x
        self.__y = y
        self.__size = size
        self.__speed = speed
        self.__inventory = PlayerInventory(screen, self)
        self.__is_inventory_open = False
        self.__miner = Miner(grid, 1, self.__inventory, clock)

    def draw(self, mouse_buttons, mouse_x_grid, mouse_y_grid):
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

        pygame.draw.rect(self.__screen, (255, 0, 0),
                         (draw_x, draw_y, self.__size, self.__size))

        if self.__is_inventory_open:
            self.__inventory.draw()

        if mouse_buttons[2] and self.__grid.is_tile_minable(mouse_x_grid, mouse_y_grid) and self.__miner.get_mining_tile() != None:
            # draw mining progress bar at the center of the bottom of the screen
            pygame.draw.rect(self.__screen, (0, 0, 0), (self.__screen.get_width(
            ) // 2 - 50, self.__screen.get_height() - 50, 100, 10))
            pygame.draw.rect(self.__screen, (255, 255, 255), (self.__screen.get_width(
            ) // 2 - 50, self.__screen.get_height() - 50, 100 * self.__miner.get_progress(), 10))

    def update(self, keys, mouse_buttons, mouse_x_grid, mouse_y_grid):
        if keys[pygame.K_w]:
            self.move(0, -1)
        if keys[pygame.K_s]:
            self.move(0, 1)
        if keys[pygame.K_a]:
            self.move(-1, 0)
        if keys[pygame.K_d]:
            self.move(1, 0)

        if self.__is_inventory_open:
            self.is_mining = False
            return

        if mouse_buttons[2] == 1:
            self.__miner.update(mouse_x_grid, mouse_y_grid)

    def move(self, x, y):
        if (self.__is_inventory_open):
            return

        x = min(max(x, -1), 1)
        y = min(max(y, -1), 1)
        self.__x += x * self.__speed * (1 / self.__clock.get_fps())
        self.__y += y * self.__speed * (1 / self.__clock.get_fps())

        self.__x = min(max(self.__x, 0), self.__grid.get_width()
                       * self.__grid.get_tile_size())
        self.__y = min(max(self.__y, 0), self.__grid.get_height()
                       * self.__grid.get_tile_size())

    def toggle_inventory(self):
        self.__is_inventory_open = not self.__is_inventory_open

    def add_item_to_inventory(self, item):
        self.__inventory.add_item(item)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y
