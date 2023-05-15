import pygame

from buildings.Building import Building


class Item:
    def __init__(self, screen, item_id, amount=1, stack_size=64):
        self._screen = screen
        self._item_id = item_id
        self._amount = amount
        self._stack_size = stack_size
        self._font = "arial"

    def drawInInventory(self, draw_x, draw_y, box_size, image):
        self._screen.blit(pygame.transform.scale(image, (int(box_size * 0.9), int(box_size * 0.9))), (
            draw_x + box_size // 2 - box_size * 0.9 // 2, draw_y + box_size // 2 - box_size * 0.9 // 2))

        text = pygame.font.SysFont(self._font, 20).render(
            str(self._amount), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (draw_x + box_size - 10, draw_y + box_size - 10)
        self._screen.blit(text, textRect)

    def drawInHotbar(self, draw_x, draw_y, box_size, amount, image):
        if amount == 0:
            # draw the image wtih a red tint
            tint = pygame.Surface((box_size, box_size))
            tint.fill((255, 0, 0))
            tint.set_alpha(128)
            self._screen.blit(tint, (draw_x, draw_y))

        self._screen.blit(pygame.transform.scale(image, (int(box_size * 0.9), int(box_size * 0.9))), (
            draw_x + box_size // 2 - box_size * 0.9 // 2, draw_y + box_size // 2 - box_size * 0.9 // 2))

        text = pygame.font.SysFont(self._font, 20).render(
            str(amount), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (draw_x + box_size - 10, draw_y + box_size - 10)
        self._screen.blit(text, textRect)

    def is_buildable(self):
        return isinstance(self, Building)

    def get_item_id(self):
        return self._item_id

    def get_amount(self):
        return self._amount

    def set_amount(self, amount):
        self._amount = amount

    def get_stack_size(self):
        return self._stack_size
