from items.Item import Item
import pygame
STACK = 64

image = pygame.image.load("assets/items/IronIngot.png")
item_id = "iron_ingot"
item_name = "Iron Ingot"


class IronIngot(Item):
    image = image
    item_id = item_id
    item_name = item_name

    def __init__(self, screen, item_count=1):
        super().__init__(screen, item_id, item_count, STACK)

    def drawInInventory(self, draw_x, draw_y, box_size):
        super().drawInInventory(draw_x, draw_y, box_size, image)

    def drawInHotbar(self, draw_x, draw_y, box_size, amount):
        super().drawInHotbar(draw_x, draw_y, box_size, amount, image)

    @staticmethod
    def draw_item_preview(screen, x, y, box_size):
        Item.draw_item_preview(screen, x, y, box_size, image)
