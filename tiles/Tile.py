import pygame


class Tile:
    def __init__(self, screen, tile_size, image, hardness=1, richness=None, item=None):
        self.screen = screen
        self.tile_size = tile_size
        self.image = image
        self.hardness = hardness
        self.richness = richness
        self.item = item

    def draw(self, x, y):
        self.screen.blit(self.image, (x, y))

    def mine(self, inventory):
        if self.item != None:
            inventory.add_item(self.item(self.screen, 1))
            self.richness -= 1
            if self.richness <= 0:
                self.item = None
                self.richness = None
                self.image = pygame.image.load("assets/tiles/empty.png")
                return False
            return True

    def get_hardness(self):
        return self.hardness
