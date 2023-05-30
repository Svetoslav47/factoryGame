import pygame
import random
from buildings.Building import Building

image = pygame.image.load("assets/buildings/Grabber.png")
width = 1
height = 1
piece_width = image.get_width() // width
piece_height = image.get_height() // height
pieces = []
for i in range(height):
    for j in range(width):
        pieces.append(image.subsurface(
            (j * piece_width, i * piece_height, piece_width, piece_height)))

inventory_size = 1
action_speed = 1


class Grabber(Building):
    image = image
    width = width
    height = height
    piece_width = piece_width
    piece_height = piece_height
    pieces = pieces

    def __init__(self, screen, grid, clock, x_grid, y_grid, rotation, item):
        super().__init__(screen, grid, clock, x_grid, y_grid, rotation,
                         width, height, "grabber", item, inventory_size)
        self._action_step = 0

    def draw(self, player, mouse_hover):
        super().draw(player, mouse_hover, pieces)

    def update(self):
        self._action_step += self._clock.get_time()
        if self._action_step >= action_speed:
            x_behind = self._x_grid - (self._x_grid - 1) * \
                (self._rotation == 3) - (self._x_grid + 1) * \
                (self._rotation == 1)

            y_behind = self._y_grid - (self._y_grid - 1) * \
                (self._rotation == 0) - (self._y_grid + 1) * \
                (self._rotation == 2)

            x_infront = self._x_grid + (self._x_grid - 1) * \
                (self._rotation == 1) + (self._x_grid + 1) * \
                (self._rotation == 3)

            y_infront = self._y_grid + (self._y_grid - 1) * \
                (self._rotation == 2) + (self._y_grid + 1) * \
                (self._rotation == 0)

            tile_behind = self._grid.get_tile_building(x_behind, y_behind)
            tile_infront = self._grid.get_tile_building(x_infront, y_infront)

            if tile_behind is None or tile_infront is None:
                return

    @staticmethod
    def draw_build_preview(screen, grid, player, mouse_x, mouse_y, rotation):
        Building.draw_build_preview(screen, grid, player, mouse_x,
                                    mouse_y, rotation, pieces, width, height)
