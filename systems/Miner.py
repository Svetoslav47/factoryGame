import pygame

from tiles.Tile import Tile


class Miner:
    def __init__(self, grid, miningSpeed, inventory, clock):
        self.__clock = clock
        self.__grid = grid
        self.__mining_tile = None
        self.__mining_progress = 0
        self.__mining_speed = 1
        self.__mining_hardness = 0
        self.__inventory = inventory
        self.__is_mining = False

    def update(self, tile_x, tile_y):
        if self.__grid.is_tile_minable(tile_x, tile_y) == False:
            return

        if self.__mining_tile != (tile_x, tile_y):
            self.__mining_tile = (tile_x, tile_y)
            self.__mining_progress = 0
            self.__mining_hardness = self.__grid.get_tile(
                tile_x, tile_y).get_hardness()

        if self.__mining_progress >= self.__mining_hardness:
            self.__grid.get_tile(*self.__mining_tile).mine(self.__inventory)
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
