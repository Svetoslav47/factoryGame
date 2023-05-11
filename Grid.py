import pygame
import math


import random
import numpy as np

from tiles.Tile import Tile
from tiles.IronOre import IronOreTile

ores = {
    "iron_ore": IronOreTile
}


class Grid:
    def __init__(self, screen, tile_size, width=200, height=200):
        self.__screen = screen
        self.__width = width
        self.__height = height
        self.__tile_size = tile_size
        self.__grid = [[0 for x in range(self.__width)]
                       for y in range(self.__height)]
        self.__generate_ore(12345, "iron_ore", size=5)
        # self.__generate_ore(67890, "iron_ore", size=5)

    def __generate_ore(self, seed, ore_type, size=20):
        random.seed(seed)
        x, y = random.randint(
            0, self.__width - size), random.randint(0, self.__height - size)

        for i in range(size):
            for j in range(size):
                self.__grid[x + i][y + j] = ores[ore_type](
                    self.__screen, self.__tile_size, self)

    def draw(self, player, mouse_x_grid, mouse_y_grid):
        player_x = player.get_x()
        player_y = player.get_y()

        if player_x < self.__screen.get_width() // 2:
            player_x = self.__screen.get_width() // 2

        if player_x > self.__width * self.__tile_size - self.__screen.get_width() // 2:
            player_x = self.__width * self.__tile_size - self.__screen.get_width() // 2

        if player_y < self.__screen.get_height() // 2:
            player_y = self.__screen.get_height() // 2

        if player_y > self.__height * self.__tile_size - self.__screen.get_height() // 2:
            player_y = self.__height * self.__tile_size - self.__screen.get_height() // 2

        square_offset_x = player_x % self.__tile_size
        square_offset_y = player_y % self.__tile_size

        start_square_x_index = player_x // self.__tile_size - \
            self.__screen.get_width() // 2 // self.__tile_size
        start_square_y_index = player_y // self.__tile_size - \
            self.__screen.get_height() // 2 // self.__tile_size

        num_squares_x = self.__screen.get_width() // self.__tile_size + 2
        num_squares_y = self.__screen.get_height() // self.__tile_size + 2

        for x in range(num_squares_x):
            for y in range(num_squares_y):
                square_x = x * self.__tile_size - square_offset_x
                square_y = y * self.__tile_size - square_offset_y

                square_x_index = int(x + start_square_x_index)
                square_y_index = int(y + start_square_y_index)

                if square_x_index < 0 or square_x_index >= self.__width or square_y_index < 0 or square_y_index >= self.__height:
                    continue

                pygame.draw.rect(self.__screen, (200, 200, 200), (square_x, square_y,
                                                                  self.__tile_size, self.__tile_size))

                if self.is_tile_minable(square_x_index, square_y_index):
                    self.__grid[square_x_index][square_y_index].draw(
                        square_x, square_y)
                    if square_x_index == mouse_x_grid and square_y_index == mouse_y_grid:
                        pygame.draw.rect(self.__screen, (0, 0, 0), (square_x, square_y,
                                                                    self.__tile_size, self.__tile_size), 2)

    def screen_to_world(self, mouse_x, mouse_y, player):
        x_in_world = mouse_x + player.get_x() - self.__screen.get_width() // 2
        y_in_world = mouse_y + player.get_y() - self.__screen.get_height() // 2

        if player.get_x() < self.__screen.get_width() / 2:
            x_in_world = mouse_x

        if player.get_x() > self.__width * self.__tile_size - self.__screen.get_width() / 2:
            x_in_world = mouse_x + self.__width * \
                self.__tile_size - self.__screen.get_width()

        if player.get_y() < self.__screen.get_height() / 2:
            y_in_world = mouse_y

        if player.get_y() > self.__height * self.__tile_size - self.__screen.get_height() / 2:
            y_in_world = mouse_y + self.__height * \
                self.__tile_size - self.__screen.get_height()

        return (int(x_in_world),
                int(y_in_world))

    def world_to_grid(self, x, y):
        return (int(x // self.__tile_size), int(y // self.__tile_size))

    def screen_to_grid(self, x, y, player):
        return self.world_to_grid(*self.screen_to_world(x, y, player))

    def get_tile(self, x, y):
        return self.__grid[x][y]

    def get_tile_coordinates(self, tile):
        for x in range(self.__width):
            for y in range(self.__height):
                if self.__grid[x][y] == tile:
                    return (x, y)
        return None

    def is_tile_minable(self, x, y):
        return isinstance(self.__grid[x][y], Tile)

    def set_tile(self, x, y, value):
        self.__grid[x][y] = value

    def get_tile_size(self):
        return self.__tile_size

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height
