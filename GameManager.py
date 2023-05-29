import pygame
from sys import exit

from Grid import Grid
from Player import Player

from items.Miner import Miner
from items.CopperIngot import CopperIngot


class GameManager:
    __instance = None

    def __init__(self, FPS=100, tile_size=50, grid_width=20, grid_height=20):
        self.FPS = FPS
        self.grid_tile_size = tile_size
        self.grid_width = grid_width
        self.grd_height = grid_height
        self.clock = pygame.time.Clock()
        pygame.init()
        pygame.display.set_caption("Factory Game")
        self.screen = pygame.display.set_mode((800, 600))

        self.grid = Grid(self.screen, tile_size=50,
                         width=grid_width, height=grid_height)

        self.player = Player(screen=self.screen,
                             grid=self.grid,
                             clock=self.clock,
                             x=self.grid.get_width() // 2 * self.grid.get_tile_size(),
                             y=self.grid.get_height() // 2 * self.grid.get_tile_size(),
                             size=10,
                             speed=200)

        if GameManager.__instance is None:
            GameManager.__instance = self

    @staticmethod
    def get_instance():
        if GameManager.__instance is None:
            GameManager()
        return GameManager.__instance

    def mainloop(self):
        while True:
            self.clock.tick(self.FPS)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_u:
                        self.player.add_item_to_inventory(Miner(self.screen))
                    if event.key == pygame.K_i:
                        self.player.add_item_to_inventory(
                            CopperIngot(self.screen))

            keys = pygame.key.get_pressed()

            mouse_buttons = pygame.mouse.get_pressed()
            mouse_x, mouse_y = pygame.mouse.get_pos()

            self.update(keys, mouse_buttons,
                        mouse_x, mouse_y, events)

            self.draw(mouse_buttons,
                      mouse_x, mouse_y)

    def update(self, keys, mouse_buttons, mouse_x, mouse_y, events):
        self.player.update(keys, mouse_buttons, mouse_x, mouse_y, events)
        self.grid.update_buildings()

    def draw(self, mouse_buttons, mouse_x, mouse_y):
        self.screen.fill((0, 0, 0))

        self.grid.draw(self.player, mouse_x, mouse_y)
        self.player.draw(mouse_buttons, mouse_x, mouse_y)

        pygame.display.update()

    def can_build(self, building, x, y):
        return self.grid.can_build(building, x, y)

    def build(self, building, x, y):
        self.grid.build(item, x, y)
