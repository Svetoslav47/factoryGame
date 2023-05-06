import pygame


class InventoryItem:
    def __init__(self, screen, box_x, box_y, box_size, item_id, item_count, image, stack_size=64, font=pygame.font.SysFont("Arial", 20)):
        self.screen = screen
        self.box_x = box_x
        self.box_y = box_y
        self.box_size = box_size
        self.item_id = item_id
        self.item_count = item_count
        self.image = image
        self.stack_size = stack_size
        self.font = font

    def draw(self):
        pass
