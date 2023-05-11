from tiles.Tile import Tile
import pygame
from Items import IronOre


class IronOreTile(Tile):
    def __init__(self, screen, tile_size, grid, hardness=2, richness=2):
        image = pygame.image.load("assets/items/IronOre.png")
        super().__init__(screen, tile_size, image, grid,
                         hardness=hardness, richness=richness, item=IronOre)
