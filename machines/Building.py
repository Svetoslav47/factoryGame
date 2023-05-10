import pygame


class Building():
    def __init__(self, screen, x, y, width, height, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.image = pygame.image.load(image)
