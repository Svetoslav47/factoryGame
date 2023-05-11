import pygame


class Building():
    def __init__(self, screen, x, y, width, height, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # split the image into width * height pieces
        self.image = image
        self.piece_width = image.get_width() // self.width
        self.piece_height = image.get_height() // self.height
        self.pieces = []
        for i in range(self.height):
            for j in range(self.width):
                self.pieces.append(self.image.subsurface(
                    j * self.piece_width, i * self.piece_height, self.piece_width, self.piece_height))
