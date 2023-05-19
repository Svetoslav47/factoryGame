import pygame


class Building():
    def __init__(self, screen, grid, x_grid, y_grid, width, height, building_id):
        self._screen = screen
        self._grid = grid
        self._x_grid = x_grid
        self._y_grid = y_grid
        self._width = width
        self._height = height
        self._id = building_id

    def draw(self, player, mouse_hover, pieces):
        for i in range(self._height):
            for j in range(self._width):
                draw_x, draw_y = self._grid.grid_to_screen(
                    self._x_grid + j, self._y_grid + i, player)
                self._screen.blit(pygame.transform.scale(
                    pieces[i * self._width + j], (self._grid.get_tile_size(), self._grid.get_tile_size())), (draw_x, draw_y))
        if mouse_hover:
            # draw black border
            border_width = 2
            draw_x, draw_y = self._grid.grid_to_screen(
                self._x_grid, self._y_grid, player)
            pygame.draw.rect(self._screen, (0, 0, 0), (draw_x, draw_y, self._width *
                             self._grid.get_tile_size(), self._height * self._grid.get_tile_size()), border_width)

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

    @staticmethod
    def draw_build_preview(screen, grid, player, mouse_x, mouse_y, pieces, width, height):
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

        for i in range(height):
            for j in range(width):
                draw_x, draw_y = grid.grid_to_screen(
                    mouse_x_grid + j, mouse_y_grid + i, player)

                screen.blit(pygame.transform.scale(
                    pieces[i * width + j], (grid.get_tile_size(), grid.get_tile_size())), (draw_x, draw_y))
