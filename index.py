import pygame

from sys import exit

from Grid import Grid
from Player import Player

FPS = 100


def draw(screen, grid, player):
    screen.fill((0, 0, 0))

    grid.draw(player.x, player.y)
    player.draw()

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption("Factory Game")
    screen = pygame.display.set_mode((800, 600))

    grid = Grid(screen, tile_size=50, width=50, height=50)

    player = Player(grid,
                    screen,
                    FPS,
                    x=grid.get_width() // 2 * grid.get_tile_size(),
                    y=grid.get_height() // 2 * grid.get_tile_size(),
                    size=10,
                    speed=200)

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player.move(0, -1)
        if keys[pygame.K_s]:
            player.move(0, 1)
        if keys[pygame.K_a]:
            player.move(-1, 0)
        if keys[pygame.K_d]:
            player.move(1, 0)

        # player_x_world_postion = min(
        #     max(player_x_world_postion, 0), grid.get_width() * grid.get_tile_size())
        # player_y_world_postion = min(
        #     max(player_y_world_postion, 0), grid.get_height() * grid.get_tile_size())

        draw(screen, grid, player)


if __name__ == "__main__":
    main()
