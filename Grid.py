
import pygame
import math


class Grid:
    def __init__(self, screen, tile_size, width=200, height=200):
        self.screen = screen
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.grid = [[0 for x in range(self.width)]
                     for y in range(self.height)]

    def draw(self, player_x_world_position, player_y_world_position):

        start_tile_x = player_x_world_position // self.tile_size - \
            self.screen.get_width() // self.tile_size // 2

        start_tile_y = player_y_world_position // self.tile_size - \
            self.screen.get_height() // self.tile_size // 2

        tile_x_offset = player_x_world_position % self.tile_size
        tile_y_offset = player_y_world_position % self.tile_size

        if self.width - start_tile_x < self.screen.get_width() // self.tile_size:
            start_tile_x = self.width - self.screen.get_width() // self.tile_size
            tile_x_offset = 0

        if start_tile_x < 0:
            start_tile_x = 0
            tile_x_offset = 0

        if self.height - start_tile_y < self.screen.get_height() // self.tile_size:
            start_tile_y = self.height - self.screen.get_height() // self.tile_size
            tile_y_offset = 0

        start_tile_x = min(max(start_tile_x, 0), self.width - 1)
        start_tile_y = min(max(start_tile_y, 0), self.height - 1)

        num_tiles_x = math.ceil(self.screen.get_width() +
                                player_x_world_position) // self.tile_size
        num_tiles_y = math.ceil(self.screen.get_height() +
                                player_x_world_position) // self.tile_size

        for x in range(num_tiles_x):
            for y in range(num_tiles_y):
                tile_x = start_tile_x + x
                tile_y = start_tile_y + y

                if tile_x < 0 or tile_x >= self.width or tile_y < 0 or tile_y >= self.height:
                    continue

                pygame.draw.rect(self.screen, (255, 255, 255),
                                 (x * self.tile_size - tile_x_offset,
                                  y * self.tile_size - tile_y_offset,
                                  self.tile_size, self.tile_size), 1)

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
