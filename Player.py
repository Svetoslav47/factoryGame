import pygame

from PlayerInventory import PlayerInventory

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
        self.isInventoryOpen = False
        self.miningTile = None
        self.miningProgress = 0
        self.miningSpeed = 1
        self.miningHardness = 0

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

        if self.isInventoryOpen:
            self.inventory.draw()

        if self.miningTile != None:
            # draw mining progress bar at the center of the bottom of the screen
            pygame.draw.rect(self.screen, (0, 0, 0), (self.screen.get_width(
            ) // 2 - 50, self.screen.get_height() - 50, 100, 10))
            pygame.draw.rect(self.screen, (255, 255, 255), (self.screen.get_width(
            ) // 2 - 50, self.screen.get_height() - 50, 100 * self.miningProgress / self.miningHardness, 10))

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
            self.mine(x, y)
        else:
            self.miningTile = None

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

    def mine(self, x, y):
        if isinstance(self.grid.get_tile(x, y), Tile) == False:
            return

        if self.miningTile != (x, y):
            self.miningTile = (x, y)
            self.miningProgress = 0
            self.miningHardness = self.grid.get_tile(x, y).get_hardness()

        if self.miningProgress >= self.grid.get_tile(x, y).get_hardness():
            self.grid.get_tile(x, y).mine(self.inventory)
            self.miningProgress = 0
            self.miningTile = None
            self.miningHardness = 0
            return

        self.miningProgress += self.miningSpeed * (1 / self.FPS)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
