from tiles.Tile import Tile
import pygame
from Items import IronOre


class IronOreTile(Tile):
    def __init__(self, screen, tile_size, hardness=2, richness=100):
        image = pygame.image.load("assets/items/IronOre.png")
        image = pygame.transform.scale(image, (tile_size, tile_size))
        super().__init__(screen, tile_size, image, hardness, richness, item=IronOre)
