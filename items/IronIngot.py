from items.Item import Item
import pygame
STACK = 64


class IronIngot(Item):
    image = pygame.image.load("assets/items/IronIngot.png")
    item_id = "iron_ingot"

    def __init__(self, screen, item_count=1):
        super().__init__(screen, IronIngot.item_id, item_count, STACK)

    def drawInInventory(self, draw_x, draw_y, box_size):
        super().drawInInventory(draw_x, draw_y, box_size, IronIngot.image)

    def drawInHotbar(self, draw_x, draw_y, box_size, amount):
        super().drawInHotbar(draw_x, draw_y, box_size, amount, IronIngot.image)

    @staticmethod
    def get_item_id():
        return Item.get_item_id(IronIngot.item_id)
