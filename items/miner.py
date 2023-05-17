from items.BuildableItem import BuildableItem
from buildings.miner import Miner as MinerBuilding

import pygame
STACK = 64


class Miner(BuildableItem):
    image = pygame.image.load("assets/items/Miner.png")

    def __init__(self, screen, item_count=1):
        super().__init__(screen, "miner", item_count, STACK, MinerBuilding)

    def drawInInventory(self, draw_x, draw_y, box_size):
        super().drawInInventory(draw_x, draw_y, box_size, Miner.image)

    def drawInHotbar(self, draw_x, draw_y, box_size, amount):
        super().drawInHotbar(draw_x, draw_y, box_size, amount, Miner.image)
