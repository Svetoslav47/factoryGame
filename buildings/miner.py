import pygame
from buildings.Building import Building


class Miner(Building):
    image = pygame.image.load("assets/buildings/miner.png")
    width = 3
    height = 3
    piece_width = image.get_width() // width
    piece_height = image.get_height() // height
    pieces = []
    for i in range(height):
        for j in range(width):
            pieces.append(image.subsurface(
                (j * piece_width, i * piece_height, piece_width, piece_height)))

    def __init__(self, screen, grid, x_grid, y_grid):
        super().__init__(screen, grid, x_grid, y_grid, Miner.width, Miner.height, "miner")

    def draw(self, player, mouse_hover):
        super().draw(player, mouse_hover, Miner.pieces)

    @staticmethod
    def draw_build_preview(screen, grid, player, mouse_x, mouse_y):
        Building.draw_build_preview(screen, grid, player, mouse_x,
                                    mouse_y, Miner.pieces, Miner.width, Miner.height)
