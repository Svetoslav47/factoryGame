from tiles.Tile import Tile
import pygame
from Items import IronOre


class IronOreTile(Tile):
    image = pygame.image.load("assets/items/IronOre.png")

    def __init__(self, screen, tile_size, grid, hardness=2, richness=2):
        super().__init__(screen, tile_size, grid,
                         hardness=hardness, richness=richness, item=IronOre)

    def draw(self, x, y):
        super().draw(x, y, IronOreTile.image)
