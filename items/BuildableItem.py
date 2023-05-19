from items.Item import Item
import pygame


class BuildableItem(Item):
    def __init__(self, screen, item_id, amount=1, stack_size=64,  building=None):
        self.__building = building
        super().__init__(screen, item_id, amount, stack_size)

    def draw_build_preview(self, grid, player, mouse_x, mouse_y):
        if self.__building is not None:
            self.__building.draw_build_preview(self._screen,
                                               grid, player, mouse_x, mouse_y)

    def build(self, grid, player, mouse_x, mouse_y):
        mouse_x_grid, mouse_y_grid = grid.screen_to_grid(
            mouse_x, mouse_y, player)

        if mouse_x_grid < 0:
            mouse_x_grid = 0

        if mouse_y_grid < 0:
            mouse_y_grid = 0

        if mouse_x_grid + self.__building.width > grid.get_width():
            mouse_x_grid = grid.get_width() - self.__building.width

        if mouse_y_grid + self.__building.height > grid.get_height():
            mouse_y_grid = grid.get_height() - self.__building.height

        if self.__building is not None:
            return grid.build(mouse_x_grid, mouse_y_grid, self.__building(self._screen, grid, mouse_x_grid, mouse_y_grid, self.__class__), self.__building.width, self.__building.width)

    def is_buildable(self):
        return True
