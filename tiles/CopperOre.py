from tiles.Tile import Tile
import pygame
from Items import CopperOre


image = pygame.image.load("assets/items/CopperOre.png")
hardness = 1
richness = 200
item = CopperOre


class CopperOreTile(Tile):
    image = image

    def __init__(self, screen, grid):
        super().__init__(screen, grid,
                         hardness, richness, item)

    @staticmethod
    def draw(screen, x, y, tile_size):
        Tile.draw(screen, x, y, tile_size, image)
