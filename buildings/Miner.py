import pygame
import random
from buildings.Building import Building

from systems.Miner import Miner as MinerSystem

image = pygame.image.load("assets/buildings/Miner.png")
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
mining_speed = 0.5


class Miner(Building):
    image = image
    width = width
    height = height
    piece_width = piece_width
    piece_height = piece_height
    pieces = pieces

    def __init__(self, screen, grid, clock, x_grid, y_grid, rotation, item):
        super().__init__(screen, grid, clock, x_grid, y_grid, rotation,
                         width, height, "miner", item, inventory_size)
        self._miner = MinerSystem(
            grid, mining_speed, self._inventory, clock)

    def draw(self, player, mouse_hover):
        super().draw(player, mouse_hover, pieces)

    @staticmethod
    def draw_build_preview(screen, grid, player, mouse_x, mouse_y, rotation):
        Building.draw_build_preview(screen, grid, player, mouse_x,
                                    mouse_y, rotation, pieces, width, height)

    def update(self):
        grid_section = self._grid.get_section(
            self._x_grid, self._y_grid, self._width, self._height)

        grid_tiles_coordinates = []
        for i in range(self._height):
            for j in range(self._width):
                if grid_section[i][j] != None:
                    grid_tiles_coordinates.append(
                        (i + self._x_grid, j + self._y_grid))

        mining_tile = self._miner.get_mining_tile()
        if len(grid_tiles_coordinates) == 0:
            return
        if mining_tile == None:
            mining_tile = grid_tiles_coordinates[random.randint(
                0, len(grid_tiles_coordinates) - 1)]

        for i in range(self._inventory.get_size()):
            if self._inventory.get_slot(i) == None:
                self._miner.update(*mining_tile)
                return
            if self._inventory.get_slot(i).item_id == grid_section[mining_tile[0] - self._x_grid][mining_tile[1] - self._y_grid].get_result_id():
                if self._inventory.get_slot(i).get_amount() < self._inventory.get_slot(i).get_stack_size():
                    self._miner.update(*mining_tile)
                    return
        print("miner is full")
