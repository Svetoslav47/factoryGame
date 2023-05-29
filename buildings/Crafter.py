import pygame
import random
from buildings.Building import Building

image = pygame.image.load("assets/buildings/Crafter.png")
width = 3
height = 3
piece_width = image.get_width() // width
piece_height = image.get_height() // height
pieces = []
for i in range(height):
    for j in range(width):
        pieces.append(image.subsurface(
            (j * piece_width, i * piece_height, piece_width, piece_height)))

inventory_size = 1
mining_speed = 1


class Crafter(Building):
    image = image
    width = width
    height = height
    piece_width = piece_width
    piece_height = piece_height
    pieces = pieces

    def __init__(self, screen, grid, clock, x_grid, y_grid, item):
        super().__init__(screen, grid, clock, x_grid, y_grid,
                         width, height, "crafter", item, inventory_size)

    def draw(self, player, mouse_hover):
        super().draw(player, mouse_hover, pieces)

    @staticmethod
    def draw_build_preview(screen, grid, player, mouse_x, mouse_y):
        Building.draw_build_preview(screen, grid, player, mouse_x,
                                    mouse_y, pieces, width, height)
