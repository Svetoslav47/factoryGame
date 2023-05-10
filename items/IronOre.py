from items.Item import Item
import pygame
STACK = 64


class IronOre(Item):
    def __init__(self, screen, item_count):
        image = pygame.image.load("assets/items/IronOre.png")
        super().__init__(screen, "iron_ore", item_count, image, STACK)
