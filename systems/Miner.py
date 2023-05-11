import pygame

from tiles.Tile import Tile


class Miner:
    def __init__(self, grid, miningSpeed, inventory, FPS):
        self.FPS = FPS
        self.grid = grid
        self.miningTile = None
        self.miningProgress = 0
        self.miningSpeed = 1
        self.miningHardness = 0
        self.inventory = inventory
        self.is_mining = False

    def update(self, tile_x, tile_y):
        if isinstance(self.grid.get_tile(tile_x, tile_y), Tile) == False:
            return

        if self.miningTile != (tile_x, tile_y):
            self.miningTile = (tile_x, tile_y)
            self.miningProgress = 0
            self.miningHardness = self.grid.get_tile(
                tile_x, tile_y).get_hardness()

        if self.miningProgress >= self.miningHardness:
            self.grid.get_tile(*self.miningTile).mine(self.inventory)
            self.miningProgress = 0
            self.miningTile = None
            self.miningHardness = 0
            return

        self.miningProgress += self.miningSpeed * (1 / self.FPS)

    def get_progress(self):
        if self.miningTile == None:
            return 0
        return self.miningProgress / self.miningHardness

    def get_mining_tile(self):
        return self.miningTile
