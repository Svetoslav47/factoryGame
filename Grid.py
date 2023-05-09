import pygame
import math


import random
import numpy as np

TILES_TEXTURE = {
    # "grass": pygame.image.load("assets/tiles/grass.png"),
    # "dirt": pygame.image.load("assets/tiles/dirt.png"),
    # "stone": pygame.image.load("assets/tiles/stone.png"),
    # "iron_ore": pygame.image.load("assets/tiles/iron_ore.png"),
    # "copper_ore": pygame.image.load("assets/tiles/copper_ore.png"),
}


class Grid:
    def __init__(self, screen, tile_size, width=200, height=200):
        self.screen = screen
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.grid = [[0 for x in range(self.width)]
                     for y in range(self.height)]
        self.generate_ore(12345, "copper_ore", size=5)
        self.generate_ore(67890, "iron_ore", size=5)

    def generate_ore(self, seed, ore_type, size=20):
        random.seed(seed)
        x, y = random.randint(
            0, self.width - size), random.randint(0, self.height - size)

        for i in range(size):
            for j in range(size):
                self.grid[x + i][y + j] = ore_type
                print(x + i, y + j)

    def draw(self, player):
        player_x = player.get_x()
        player_y = player.get_y()

        if player_x < self.screen.get_width() // 2:
            player_x = self.screen.get_width() // 2

        if player_x > self.width * self.tile_size - self.screen.get_width() // 2:
            player_x = self.width * self.tile_size - self.screen.get_width() // 2

        if player_y < self.screen.get_height() // 2:
            player_y = self.screen.get_height() // 2

        if player_y > self.height * self.tile_size - self.screen.get_height() // 2:
            player_y = self.height * self.tile_size - self.screen.get_height() // 2

        square_offset_x = player_x % self.tile_size
        square_offset_y = player_y % self.tile_size

        start_square_x_index = player_x // self.tile_size - \
            self.screen.get_width() // 2 // self.tile_size
        start_square_y_index = player_y // self.tile_size - \
            self.screen.get_height() // 2 // self.tile_size

        num_squares_x = self.screen.get_width() // self.tile_size + 2
        num_squares_y = self.screen.get_height() // self.tile_size + 2

        for x in range(num_squares_x):
            for y in range(num_squares_y):
                square_x = x * self.tile_size - square_offset_x
                square_y = y * self.tile_size - square_offset_y

                square_x_index = int(x + start_square_x_index)
                square_y_index = int(y + start_square_y_index)

                if square_x_index < 0 or square_x_index >= self.width or square_y_index < 0 or square_y_index >= self.height:
                    continue

                color = (255, 255, 255)
                if self.grid[square_x_index][square_y_index] == "iron_ore":
                    color = (128, 128, 128)  # gray
                elif self.grid[square_x_index][square_y_index] == "copper_ore":
                    color = (0, 255, 0)

                pygame.draw.rect(self.screen, color,
                                 (square_x, square_y, self.tile_size, self.tile_size))

    def screen_to_world(self, mouse_x, mouse_y, player):
        x_in_world = mouse_x + player.get_x() - self.screen.get_width() // 2
        y_in_world = mouse_y + player.get_y() - self.screen.get_height() // 2

        if player.x < self.screen.get_width() / 2:
            x_in_world = mouse_x

        if player.x > self.width * self.tile_size - self.screen.get_width() / 2:
            x_in_world = mouse_x + self.width * self.tile_size - self.screen.get_width()

        if player.y < self.screen.get_height() / 2:
            y_in_world = mouse_y

        if player.y > self.height * self.tile_size - self.screen.get_height() / 2:
            y_in_world = mouse_y + self.height * self.tile_size - self.screen.get_height()

        return (int(x_in_world),
                int(y_in_world))

    def world_to_grid(self, x, y):
        return (int(x // self.tile_size), int(y // self.tile_size))

    def screen_to_grid(self, x, y, player):
        return self.world_to_grid(*self.screen_to_world(x, y, player))

    def get_tile(self, x, y):
        return self.grid[x][y]

    def set_tile(self, x, y, value):
        self.grid[x][y] = value

    def get_tile_size(self):
        return self.tile_size

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
