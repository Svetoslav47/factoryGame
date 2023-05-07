from items.Item import Item
import pygame
STACK = 64


class CopperIngot(Item):
    def __init__(self, screen, item_count):
        image = pygame.image.load("assets/items/CopperIngot.png")
        super().__init__(screen, "copper_ingot", item_count, image, STACK)
