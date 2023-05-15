from items.Item import Item
import pygame
STACK = 64


class CopperIngot(Item):
    image = pygame.image.load("assets/items/CopperIngot.png")

    def __init__(self, screen, item_count=1):
        super().__init__(screen, "copper_ingot", item_count, STACK)

    def drawInInventory(self, draw_x, draw_y, box_size):
        super().drawInInventory(draw_x, draw_y, box_size, CopperIngot.image)

    def drawInHotbar(self, draw_x, draw_y, box_size, amount):
        super().drawInHotbar(draw_x, draw_y, box_size, amount, CopperIngot.image)
