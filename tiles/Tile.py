import pygame


class Tile:
    def __init__(self, screen, grid, hardness=1, richness=None, item=None):
        self.__screen = screen
        self.__hardness = hardness
        self.__richness = richness
        self.__item = item
        self.__grid = grid

    @staticmethod
    def draw(screen, x, y, tile_size, image):
        screen.blit(pygame.transform.scale(
            image, (tile_size, tile_size)), (x, y))

    def mine(self, inventory):
        if self.__item != None:
            inventory.add_item(self.__item(self.__screen, 1))
            self.__richness -= 1
            if self.__richness <= 0:
                self.__item = None
                self.__richness = None
                self.__image = None
                tile_coordinates = self.__grid.get_tile_coordinates(self)
                if tile_coordinates != None:
                    self.__grid.set_tile(
                        *tile_coordinates, None)
                return False
            return True

    def is_solid(self):
        return True

    def get_hardness(self):
        return self.__hardness
