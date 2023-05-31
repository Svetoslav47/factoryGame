import pygame

from tiles.Tile import Tile
from buildings.Building import Building


class Miner:
    def __init__(self, grid, miningSpeed, inventory, clock, is_player=False):
        self.__clock = clock
        self.__grid = grid
        self.__mining_tile = None
        self.__mining_progress = 0
        self.__mining_speed = miningSpeed
        self.__mining_hardness = 0
        self.__inventory = inventory
        self.__is_mining = False
        self.__is_player = is_player

    def update(self, tile_x, tile_y):
        if self.__grid.is_tile_minable(tile_x, tile_y, self.__is_player) == False:
            return

        tyle_type = "tile"
        if isinstance(self.__grid.get_tile(tile_x, tile_y, self.__is_player), Building):
            tyle_type = "building"

        if tyle_type == "building":
            tile_x = self.__grid.get_tile(
                tile_x, tile_y, self.__is_player).get_x_grid()
            tile_y = self.__grid.get_tile(
                tile_x, tile_y, self.__is_player).get_y_grid()

        if self.__mining_tile != (tile_x, tile_y):
            self.__mining_tile = (tile_x, tile_y)
            self.__mining_progress = 0
            self.__mining_hardness = self.__grid.get_tile(
                tile_x, tile_y, self.__is_player).get_hardness()

        if self.__mining_progress >= self.__mining_hardness:
            self.__grid.get_tile(*self.__mining_tile,
                                 self.__is_player).mine(self.__inventory)
            self.__mining_progress = 0
            self.__mining_tile = None
            self.__mining_hardness = 0
            return

        self.__mining_progress += self.__mining_speed * \
            (1 / self.__clock.get_fps())

    def get_progress(self):
        if self.__mining_tile == None:
            return 0
        return self.__mining_progress / self.__mining_hardness

    def get_mining_tile(self):
        return self.__mining_tile
