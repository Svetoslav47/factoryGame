from items.Item import Item
import pygame
STACK = 64


class IronOre(Item):
    image = pygame.image.load("assets/items/IronOre.png")

    def __init__(self, screen, item_count):
        super().__init__(screen, "iron_ore", item_count, STACK)

    def drawInInventory(self, draw_x, draw_y, box_size):
        super().drawInInventory(draw_x, draw_y, box_size, IronOre.image)
