import pygame
import random
import math
from buildings.Building import Building


image = pygame.image.load("assets/buildings/Chest.png")
width = 1
height = 1
piece_width = image.get_width() // width
piece_height = image.get_height() // height
pieces = []
for i in range(height):
    for j in range(width):
        pieces.append(image.subsurface(
            (j * piece_width, i * piece_height, piece_width, piece_height)))

inventory_size = 35


class Chest(Building):
    image = image
    width = width
    height = height
    piece_width = piece_width
    piece_height = piece_height
    pieces = pieces
    name = "Chest"

    def __init__(self, screen, grid, clock, x_grid, y_grid, rotation, item):
        super().__init__(screen, grid, clock, x_grid, y_grid, rotation,
                         width, height, "chest", item, inventory_size)

    def draw(self, player, mouse_hover):
        super().draw(player, mouse_hover, pieces)

    def update(self):
        pass

    def draw_inventory(self, screen, draw_x, draw_y, draw_zone_width, draw_zone_height):
        inventory_screen_size_x = draw_zone_width
        inventory_screen_size_y = draw_zone_height
        inventory_columns = math.floor(self._inventory.get_size()**0.5)
        inventory_box_width = inventory_screen_size_x / \
            (inventory_columns*1.1)

        inventory_rows = math.ceil(
            self._inventory.get_size() / inventory_columns)
        inventory_box_height = inventory_screen_size_y / \
            (inventory_rows*1.1)
        inventory_box_size = min(
            inventory_box_width, inventory_box_height)

        inventory_box_padding_x = (inventory_screen_size_x - (inventory_box_size * inventory_columns)) / \
            (inventory_columns + 1)
        inventory_box_padding_y = (inventory_screen_size_y - (inventory_box_size * inventory_rows)) / \
            (inventory_rows + 1)

        for x in range(inventory_columns):
            for y in range(inventory_rows):
                box_x = draw_x + inventory_box_padding_x + \
                    (inventory_box_size + inventory_box_padding_x) * x
                box_y = draw_y + inventory_box_padding_y + \
                    (inventory_box_size + inventory_box_padding_y) * y
                pygame.draw.rect(
                    screen, (255, 255, 255), (box_x, box_y, inventory_box_size, inventory_box_size))
                if self._inventory.get_slot(x + y * inventory_columns) != None:
                    self._inventory.get_slot(x + y * inventory_columns).drawInInventory(
                        box_x, box_y, inventory_box_size)

    def get_box_from_inventory(self, mouse_x, mouse_y, draw_x, draw_y, draw_zone_width, draw_zone_height):
        inventory_screen_size_x = draw_zone_width
        inventory_screen_size_y = draw_zone_height
        inventory_columns = math.floor(self._inventory.get_size()**0.5)
        inventory_box_width = inventory_screen_size_x / \
            (inventory_columns*1.1)

        inventory_rows = math.ceil(
            self._inventory.get_size() / inventory_columns)
        inventory_box_height = inventory_screen_size_y / \
            (inventory_rows*1.1)
        inventory_box_size = min(
            inventory_box_width, inventory_box_height)

        inventory_box_padding_x = (inventory_screen_size_x - (inventory_box_size * inventory_columns)) / \
            (inventory_columns + 1)
        inventory_box_padding_y = (inventory_screen_size_y - (inventory_box_size * inventory_rows)) / \
            (inventory_rows + 1)

        for x in range(inventory_columns):
            for y in range(inventory_rows):
                box_x = draw_x + inventory_box_padding_x + \
                    (inventory_box_size + inventory_box_padding_x) * x
                box_y = draw_y + inventory_box_padding_y + \
                    (inventory_box_size + inventory_box_padding_y) * y
                if mouse_x >= box_x and mouse_x <= box_x + inventory_box_size and mouse_y >= box_y and mouse_y <= box_y + inventory_box_size:
                    return self._inventory, x + y * inventory_columns

        return self._inventory, None

    @staticmethod
    def draw_build_preview(screen, grid, player, mouse_x, mouse_y, rotation):
        Building.draw_build_preview(screen, grid, player, mouse_x,
                                    mouse_y, rotation, pieces, width, height)
