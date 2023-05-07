import pygame

from Inventory import Inventory


class Player:
    def __init__(self, grid, screen, FPS, x, y, size, speed):
        self.grid = grid
        self.screen = screen
        self.FPS = FPS
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.inventory = Inventory(screen, self)
        self.isInventoryOpen = False

    def draw(self):
        draw_x = self.screen.get_width() // 2 - self.size // 2
        draw_y = self.screen.get_height() // 2 - self.size // 2

        if (self.x < self.screen.get_width() // 2):
            draw_x = self.x - self.size // 2

        if (self.x > self.grid.get_width() * self.grid.get_tile_size() - self.screen.get_width() // 2):
            draw_x = self.x - \
                (self.grid.get_width() * self.grid.get_tile_size() -
                 self.screen.get_width()) - self.size // 2

        if (self.y < self.screen.get_height() // 2):
            draw_y = self.y - self.size // 2

        if (self.y > self.grid.get_height() * self.grid.get_tile_size() - self.screen.get_height() // 2):
            draw_y = self.y - \
                (self.grid.get_height() * self.grid.get_tile_size() -
                 self.screen.get_height()) - self.size // 2

        pygame.draw.rect(self.screen, (255, 0, 0),
                         (draw_x, draw_y, self.size, self.size))

        if (self.isInventoryOpen):
            self.inventory.draw()

    def move(self, x, y):
        if (self.isInventoryOpen):
            return

        x = min(max(x, -1), 1)
        y = min(max(y, -1), 1)
        self.x += x * self.speed * (1 / self.FPS)
        self.y += y * self.speed * (1 / self.FPS)

        self.x = min(max(self.x, 0), self.grid.get_width()
                     * self.grid.get_tile_size())
        self.y = min(max(self.y, 0), self.grid.get_height()
                     * self.grid.get_tile_size())

    def toggle_inventory(self):
        self.isInventoryOpen = not self.isInventoryOpen

    def add_item_to_inventory(self, item):
        self.inventory.add_item(item)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
