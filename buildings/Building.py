import pygame
from systems.Inventory import Inventory

import numpy as np


class Building():
    def __init__(self, screen, grid, clock, x_grid, y_grid, rotation, width, height, building_id, item, inventory_size, hardness=1):
        self._screen = screen
        self._grid = grid
        self._clock = clock
        self._x_grid = x_grid
        self._y_grid = y_grid
        self._rotation = rotation
        self._width = width
        self._height = height
        self._id = building_id
        self._item = item
        self.__hardness = hardness
        self._inventory = Inventory(screen, inventory_size)

    def draw(self, player, mouse_hover, pieces):
        pieces = np.array(pieces)
        pieces = pieces.reshape(self._height, self._width)
        pieces = np.rot90(pieces, self._rotation)
        pieces = pieces.flatten()

        for i in range(self._height):
            for j in range(self._width):
                piece = pieces[i * self._width + j]
                piece = pygame.transform.rotate(piece, self._rotation * 90)

                draw_x, draw_y = self._grid.grid_to_screen(
                    self._x_grid + j, self._y_grid + i, player)
                self._screen.blit(pygame.transform.scale(
                    piece, (self._grid.get_tile_size(), self._grid.get_tile_size())), (draw_x, draw_y))

        if mouse_hover:
            border_width = 2
            draw_x, draw_y = self._grid.grid_to_screen(
                self._x_grid, self._y_grid, player)
            pygame.draw.rect(self._screen, (0, 0, 0), (draw_x, draw_y, self._width *
                             self._grid.get_tile_size(), self._height * self._grid.get_tile_size()), border_width)

    def mine(self, inventory):
        inventory.add_item(self._item(self._screen, 1))
        for i in range(self._inventory.get_size()):
            item = self._inventory.get_slot(i)
            if item != None:
                inventory.add_item(item)

        self._grid.deconstruct_building(
            self._x_grid, self._y_grid, self._width, self._height, self)

    def get_hardness(self):
        return self.__hardness

    def get_id(self):
        return self._id

    def get_x_grid(self):
        return self._x_grid

    def get_y_grid(self):
        return self._y_grid

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def update(self):
        print("building doesn't have update method")

    def draw_inventory(self, screen, draw_x, draw_y, draw_zone_width, draw_zone_height):
        # draw "this building doesnt have an openable inventory" text
        font = pygame.font.SysFont("Arial", 20)
        text = font.render(
            "This building doesn't have an openable inventory", True, (0, 0, 0))
        # rotate the text to go from top left to bottom right
        text = pygame.transform.rotate(text, 45)

        text_rect = text.get_rect()
        text_rect.center = (draw_x + draw_zone_width // 2,
                            draw_y + draw_zone_height // 2)
        screen.blit(text, text_rect)

    def get_box_from_inventory(self, mouse_x, mouse_y, draw_x, draw_y, draw_zone_width, draw_zone_height):
        return self._inventory, None

    def get_inventory(self):
        return self._inventory

    @staticmethod
    def draw_build_preview(screen, grid, player, mouse_x, mouse_y, rotation, pieces, width, height):
        mouse_x_grid, mouse_y_grid = grid.screen_to_grid(
            mouse_x, mouse_y, player)

        if mouse_x_grid < 0:
            mouse_x_grid = 0

        if mouse_y_grid < 0:
            mouse_y_grid = 0

        if mouse_x_grid + width > grid.get_width():
            mouse_x_grid = grid.get_width() - width

        if mouse_y_grid + height > grid.get_height():
            mouse_y_grid = grid.get_height() - height

        pieces = np.array(pieces)
        pieces = np.reshape(pieces, (height, width))
        pieces = np.rot90(pieces, rotation)
        pieces = pieces.flatten()

        for i in range(height):
            for j in range(width):
                draw_x, draw_y = grid.grid_to_screen(
                    mouse_x_grid + j, mouse_y_grid + i, player)

                piece = pieces[i * width + j]
                piece = pygame.transform.rotate(piece, rotation * 90)

                screen.blit(pygame.transform.scale(
                    piece, (grid.get_tile_size(), grid.get_tile_size())), (draw_x, draw_y))
