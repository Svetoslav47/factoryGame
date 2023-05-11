import pygame

from PlayerInventory import PlayerInventory
from systems.Miner import Miner

from tiles.Tile import Tile


class Player:
    def __init__(self, grid, screen, FPS, x, y, size, speed):
        self.grid = grid
        self.screen = screen
        self.FPS = FPS
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.inventory = PlayerInventory(screen, self)
        self.is_inventory_open = False
        self.miner = Miner(grid, 1, self.inventory, FPS)
        self.is_mining = False

    def draw(self):
        draw_x = self.screen.get_width() // 2 - self.size // 2
        draw_y = self.screen.get_height() // 2 - self.size // 2

        if self.x < self.screen.get_width() // 2:
            draw_x = self.x - self.size // 2

        if self.x > self.grid.get_width() * self.grid.get_tile_size() - self.screen.get_width() // 2:
            draw_x = self.x - \
                (self.grid.get_width() * self.grid.get_tile_size() -
                 self.screen.get_width()) - self.size // 2

        if self.y < self.screen.get_height() // 2:
            draw_y = self.y - self.size // 2

        if self.y > self.grid.get_height() * self.grid.get_tile_size() - self.screen.get_height() // 2:
            draw_y = self.y - \
                (self.grid.get_height() * self.grid.get_tile_size() -
                 self.screen.get_height()) - self.size // 2

        pygame.draw.rect(self.screen, (255, 0, 0),
                         (draw_x, draw_y, self.size, self.size))

        if self.is_inventory_open:
            self.inventory.draw()

        if self.is_mining and self.miner.get_mining_tile() != None:
            # draw mining progress bar at the center of the bottom of the screen
            pygame.draw.rect(self.screen, (0, 0, 0), (self.screen.get_width(
            ) // 2 - 50, self.screen.get_height() - 50, 100, 10))
            pygame.draw.rect(self.screen, (255, 255, 255), (self.screen.get_width(
            ) // 2 - 50, self.screen.get_height() - 50, 100 * self.miner.get_progress(), 10))

    def update(self, keys, mouse_buttons, mouse_x, mouse_y):
        if keys[pygame.K_w]:
            self.move(0, -1)
        if keys[pygame.K_s]:
            self.move(0, 1)
        if keys[pygame.K_a]:
            self.move(-1, 0)
        if keys[pygame.K_d]:
            self.move(1, 0)

        if mouse_buttons[2] == 1:
            x, y = self.grid.screen_to_grid(mouse_x, mouse_y, self)
            self.is_mining = True
            self.miner.update(x, y)
        else:
            self.is_mining = None

    def move(self, x, y):
        if (self.is_inventory_open):
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
        self.is_inventory_open = not self.is_inventory_open

    def add_item_to_inventory(self, item):
        self.inventory.add_item(item)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
