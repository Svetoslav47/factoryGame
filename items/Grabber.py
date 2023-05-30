from items.BuildableItem import BuildableItem
from buildings.Grabber import Grabber as GrabberBuilding

import pygame
STACK = 64

image = pygame.image.load("assets/items/Grabber.png")
item_id = "grabber"
item_name = "Grabber"


class Grabber(BuildableItem):
    image = image
    item_id = item_id
    item_name = item_name

    def __init__(self, screen, item_count=1):
        super().__init__(screen, item_id, item_count, STACK, GrabberBuilding)

    def drawInInventory(self, draw_x, draw_y, box_size):
        super().drawInInventory(draw_x, draw_y, box_size, image)

    def drawInHotbar(self, draw_x, draw_y, box_size, amount):
        super().drawInHotbar(draw_x, draw_y, box_size, amount, image)

    @staticmethod
    def draw_item_preview(screen, x, y, box_size):
        BuildableItem.draw_item_preview(screen, x, y, box_size, image)
