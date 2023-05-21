from items.Item import Item
import pygame
STACK = 64


class CopperPlate(Item):
    image = pygame.image.load("assets/items/CopperPlate.png")
    item_id = "copper_plate"

    def __init__(self, screen, item_count=1):
        super().__init__(screen, CopperPlate.item_id, item_count, STACK)

    def drawInInventory(self, draw_x, draw_y, box_size):
        super().drawInInventory(draw_x, draw_y, box_size, CopperPlate.image)

    def drawInHotbar(self, draw_x, draw_y, box_size, amount):
        super().drawInHotbar(draw_x, draw_y, box_size, amount, CopperPlate.image)

    @staticmethod
    def get_item_id():
        return Item.get_item_id(CopperPlate.item_id)
