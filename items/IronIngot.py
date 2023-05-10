from items.Item import Item
import pygame
STACK = 64


class IronIngot(Item):
    def __init__(self, screen, item_count):
        image = pygame.image.load("assets/items/IronIngot.png")
        super().__init__(screen, "iron_ingot", item_count, image, STACK)
