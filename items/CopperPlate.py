from items.Item import Item
import pygame
STACK = 64


class CopperPlate(Item):
    def __init__(self, screen, item_count):
        image = pygame.image.load("assets/items/CopperIngot.png")
        super().__init__(screen, "copper_plate", item_count, image, STACK)
