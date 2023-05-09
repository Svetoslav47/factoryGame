from Inventory import Inventory
import math
import pygame


class PlayerInventory(Inventory):
    def __init__(self, screen, player):
        super().__init__(screen, 35)
        self.player = player
        self.screen_size_x = screen.get_width() * 3 / 4
        self.screen_size_y = screen.get_height() * 3 / 4
        self.columns = 5
        self.box_size = self.screen_size_x / \
            (math.ceil(self.inventory_size / self.columns) * 1.49)
        self.box_padding = self.box_size / 10

    def draw(self):
        # Draw the inventory background at the middle of the screen
        pygame.draw.rect(self.screen, (128, 128, 128), (self.screen.get_width() // 2 - self.screen_size_x // 2,
                                                        self.screen.get_height() // 2 - self.screen_size_y // 2, self.screen_size_x, self.screen_size_y))

        for x in range(self.columns):
            for y in range(math.ceil(self.inventory_size / self.columns)):

                if y*self.columns + x >= self.inventory_size:
                    break

                box_x = self.screen.get_width() // 2 - self.screen_size_x // 2 + \
                    self.box_padding + x * (self.box_size + self.box_padding)

                box_y = self.screen.get_height() // 2 - self.screen_size_y // 2 + \
                    self.box_padding + y * (self.box_size + self.box_padding)

                pygame.draw.rect(self.screen, (255, 255, 255),
                                 (box_x, box_y, self.box_size, self.box_size))

                if self.inventory[y*self.columns + x] != None:
                    self.inventory[y*self.columns + x].drawInInventory(
                        box_x, box_y, self.box_size)
