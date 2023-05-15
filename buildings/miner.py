import pygame


class Miner:
    def __init__(self, screen, x, y, width, height):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.image = pygame.image.load("assets/machines/miner.png")

    def mine(self):
        pass
