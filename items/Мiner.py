from items.BuildableItem import BuildableItem
from buildings.Miner import Miner as MinerBuilding

import pygame
STACK = 64

image = pygame.image.load("assets/items/Miner.png")
item_id = "miner"
item_name = "Miner"


class Miner(BuildableItem):
    image = image
    item_id = item_id
    item_name = item_name

    def __init__(self, screen, item_count=1):
        super().__init__(screen, item_id, item_count, STACK, MinerBuilding)

    def drawInInventory(self, draw_x, draw_y, box_size):
        super().drawInInventory(draw_x, draw_y, box_size, image)

    def drawInHotbar(self, draw_x, draw_y, box_size, amount):
        super().drawInHotbar(draw_x, draw_y, box_size, amount, image)

    @staticmethod
    def draw_item_preview(screen, x, y, box_size):
        BuildableItem.draw_item_preview(screen, x, y, box_size, image)
