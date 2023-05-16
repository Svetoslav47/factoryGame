import pygame

from sys import exit

from Grid import Grid
from Player import Player

FPS = 100


def draw(screen, grid, player, mouse_buttons, mouse_x, mouse_y):
    screen.fill((0, 0, 0))

    grid.draw(player, mouse_x, mouse_y)
    player.draw(mouse_buttons, mouse_x, mouse_y)

    pygame.display.update()


def update(player, keys, mouse_buttons, mouse_x, mouse_y, events):
    player.update(keys, mouse_buttons, mouse_x, mouse_y, events)


def main():
    clock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption("Factory Game")
    screen = pygame.display.set_mode((800, 600))

    grid = Grid(screen, tile_size=50, width=20, height=20)

    player = Player(grid,
                    screen,
                    clock,
                    x=grid.get_width() // 2 * grid.get_tile_size(),
                    y=grid.get_height() // 2 * grid.get_tile_size(),
                    size=10,
                    speed=200)

    while True:
        clock.tick(FPS)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    player.toggle_inventory()

        keys = pygame.key.get_pressed()

        mouse_buttons = pygame.mouse.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_x_grid, mouse_y_grid = grid.screen_to_grid(
            mouse_x, mouse_y, player)

        update(player, keys, mouse_buttons,
               mouse_x, mouse_y, events)

        draw(screen, grid, player, mouse_buttons,
             mouse_x_grid, mouse_y_grid)


if __name__ == "__main__":
    main()
