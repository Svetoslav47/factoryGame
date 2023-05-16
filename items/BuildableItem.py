from items.Item import Item
import pygame


class BuildableItem(Item):
    def __init__(self, screen, item_id, amount=1, stack_size=64):
        super().__init__(screen, item_id, amount, stack_size)
