from tiles.Tile import Tile
import pygame
from Items import IronOre


class IronOreTile(Tile):
    image = pygame.image.load("assets/items/IronOre.png")

    def __init__(self, screen, grid, hardness=2, richness=2):
        super().__init__(screen, grid,
                         hardness=hardness, richness=richness, item=IronOre)

    @staticmethod
    def draw(screen, x, y, tile_size):
        Tile.draw(screen, x, y, tile_size, IronOreTile.image)
