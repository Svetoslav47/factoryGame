import pygame


class Keybinds:
    keybinds = {
        "move_up": pygame.K_w,
        "move_down": pygame.K_s,
        "move_left": pygame.K_a,
        "move_right": pygame.K_d,
        "toggle_inventory": pygame.K_e,
        "toggle_pause": pygame.K_ESCAPE,
        "toggle_debug": pygame.K_F3,
        "toggle_grid": pygame.K_F4,
        "toggle_fps": pygame.K_F5,
        "mine": 2,
        "place": 0,
        "rotate": pygame.K_r,
        "select_1": pygame.K_1,
        "select_2": pygame.K_2,
        "select_3": pygame.K_3,
        "select_4": pygame.K_4,
        "select_5": pygame.K_5,
        "select_6": pygame.K_6,
        "select_7": pygame.K_7,
        "select_8": pygame.K_8,
        "select_9": pygame.K_9,
        "select_10": pygame.K_0,
    }

    def get_keybind(key):
        return Keybinds.keybinds[key]
