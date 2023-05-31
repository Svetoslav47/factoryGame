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
        self._action_step += 1 / self._clock.get_fps()
        if self._action_step >= action_speed:
            x_behind = self._x_grid
            y_behind = self._y_grid

            x_infront = self._x_grid
            y_infront = self._y_grid

            if self._rotation == 0:
                y_behind -= 1
                y_infront += 1
            elif self._rotation == 1:
                x_behind -= 1
                x_infront += 1
            elif self._rotation == 2:
                y_behind += 1
                y_infront -= 1
            elif self._rotation == 3:
                x_behind += 1
                x_infront -= 1

            tile_behind = self._grid.get_tile_building(x_behind, y_behind)
            tile_infront = self._grid.get_tile_building(x_infront, y_infront)

            if tile_behind is None or tile_infront is None:
                return

            tile_behind_slot = tile_behind.get_inventory().get_slot_with_item()

            if tile_behind_slot is None:
                return

            tile_behind_item = tile_behind.get_inventory().get_slot(tile_behind_slot)

            print(tile_behind.get_inventory().amount_of_item(
                tile_behind_item.item_id))
            if tile_behind.get_inventory().remove_item(tile_behind_item.item_id, 1):
                tile_infront.get_inventory().add_item(
                    tile_behind_item.__class__(self._screen, 1))
                self._action_step = 0

    @staticmethod
    def draw_build_preview(screen, grid, player, mouse_x, mouse_y, rotation):
        Building.draw_build_preview(screen, grid, player, mouse_x,
                                    mouse_y, rotation, pieces, width, height)
