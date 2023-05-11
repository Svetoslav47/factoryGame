import pygame


class Item:
    def __init__(self, screen, item_id, amount, image, stack_size):
        self._screen = screen
        self._item_id = item_id
        self._amount = amount
        self._image = image
        self._stack_size = stack_size
        self._font = "arial"

    def drawInInventory(self, draw_x, draw_y, box_size):
        # Draw the item image scaled by 0.9 and centered in the box
        self._screen.blit(pygame.transform.scale(self._image, (int(box_size * 0.9), int(box_size * 0.9))), (
            draw_x + box_size // 2 - box_size * 0.9 // 2, draw_y + box_size // 2 - box_size * 0.9 // 2))

        # Draw the item count
        text = pygame.font.SysFont(self._font, 20).render(
            str(self._amount), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (draw_x + box_size - 10, draw_y + box_size - 10)
        self._screen.blit(text, textRect)

    def get_item_id(self):
        return self._item_id

    def get_amount(self):
        return self._amount

    def set_amount(self, amount):
        self._amount = amount

    def get_stack_size(self):
        return self._stack_size
