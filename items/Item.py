import pygame


class Item:
    def __init__(self, screen, item_id, amount, image, stack_size):
        self.screen = screen
        self.item_id = item_id
        self.amount = amount
        self.image = image
        self.stack_size = stack_size
        self.font = "arial"

    def drawInInventory(self, draw_x, draw_y, box_size):
        # Draw the item image scaled by 0.9 and centered in the box
        self.screen.blit(pygame.transform.scale(self.image, (int(box_size * 0.9), int(box_size * 0.9))), (
            draw_x + box_size // 2 - box_size * 0.9 // 2, draw_y + box_size // 2 - box_size * 0.9 // 2))

        # Draw the item count
        text = pygame.font.SysFont(self.font, 20).render(
            str(self.amount), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (draw_x + box_size - 10, draw_y + box_size - 10)
        self.screen.blit(text, textRect)
