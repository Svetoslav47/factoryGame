from items.Item import Item
import pygame
STACK = 64


class CopperPlate(Item):
    image = pygame.image.load("assets/items/CopperIngot.png")

    def __init__(self, screen, item_count):
        super().__init__(screen, "copper_plate", item_count, STACK)

    def drawInInventory(self, draw_x, draw_y, box_size):
        super().drawInInventory(draw_x, draw_y, box_size, CopperPlate.image)
