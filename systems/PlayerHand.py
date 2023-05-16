from items.Item import Item


class PlayerHand():
    def __init__(self, screen, box_size=50):
        self.__screen = screen
        self.__item = None
        self.__box_size = box_size

    def draw(self, mouse_x, mouse_y):
        if self.__item is not None:
            self.__item.drawInInventory(mouse_x, mouse_y, self.__box_size)

    def grab(self, inventory, index):
        if index is None:
            return

        if self.__item is None:
            self.__item = inventory.pop_slot(index)
            return True

        temp = self.__item
        self.__item = inventory.pop_slot(index)
        inventory.set_slot(index, temp)
