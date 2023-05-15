import pygame


class Building():
    def __init__(self, screen, x_grid, y_grid, width, height, image):
        self.screen = screen
        self.x_grid = x_grid
        self.y_grid = y_grid
        self.width = width
        self.height = height

        # split the image into width * height pieces
        self.image = image
        self.piece_width = image.get_width() // self.width
        self.piece_height = image.get_height() // self.height
        self.pieces = [[None] * self.width] * self.height
        for i in range(self.height):
            for j in range(self.width):
                self.pieces[i][j] = image.subsurface(
                    (j * self.piece_width, i * self.piece_height, self.piece_width, self.piece_height))

    def draw(self, x_grid, y_grid, grid):
        for i in range(self.height):
            for j in range(self.width):
                pygame.blit(self.pieces[i * self.width + j], (self.piece_width, self.piece_height),
                            (grid.grid_to_screen(x_grid + j), grid.grid_to_screen(y_grid + i)))

    def draw_build_preview(self, x_grid, y_grid):
        for i in range(self.height):
            for j in range(self.width):
                pygame.blit(self.pieces[i * self.width + j], (self.piece_width, self.piece_height),
                            (x_grid + j, y_grid + i))
