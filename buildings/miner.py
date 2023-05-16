import pygame
from buildings.Building import Building


class Miner(Building):
    def __init__(self, screen, x_grid, y_grid, width, height):
        super().__init__(screen, x_grid, y_grid, width, height, pygame.image.load(
            "assets/building/miner.png"))
