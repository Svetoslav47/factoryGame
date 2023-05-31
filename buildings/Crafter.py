import pygame
import random
from buildings.Building import Building
from systems.Crafter import Crafter as CrafterSystem
from systems.Inventory import Inventory

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
crafting_speed = 1


class Crafter(Building):
    image = image
    width = width
    height = height
    piece_width = piece_width
    piece_height = piece_height
    pieces = pieces
    name = "Crafter"

    def __init__(self, screen, grid, clock, x_grid, y_grid, rotation, item, result_inventory=None):
        super().__init__(screen, grid, clock, x_grid, y_grid, rotation,
                         width, height, "crafter", item, inventory_size)
        if result_inventory is not None:
            self._result_inventory = result_inventory
        else:
            print("create result inv")
            self._result_inventory = Inventory(self._screen, 1)

        self._crafter = CrafterSystem(
            screen, clock, self._inventory, self._result_inventory)

    def draw(self, player, mouse_hover):
        super().draw(player, mouse_hover, pieces)

    def set_recepie(self, recepie):
        self._crafter.set_recepie(recepie)

    @staticmethod
    def draw_build_preview(screen, grid, player, mouse_x, mouse_y, rotation):
        Building.draw_build_preview(screen, grid, player, mouse_x,
                                    mouse_y, rotation, pieces, width, height)

    def get_inventory(self):
        return self._inventory, self._result_inventory

    def update(self):
        self._crafter.update()
