from items.Item import Item


class PlayerHand():
    def __init__(self, screen, grid, player, player_hotbar, box_size=50):
        self.__screen = screen
        self.__grid = grid
        self.__player = player
        self.__item = None
        self.__box_size = box_size
        self.__player_hotbar = player_hotbar

    def draw(self, mouse_x, mouse_y, is_mouse_in_inventory_screen):
        if self.__item is not None:
            if not self.__item.is_buildable():
                self.__item.drawInInventory(mouse_x, mouse_y, self.__box_size)
                return

            if is_mouse_in_inventory_screen:
                self.__item.drawInInventory(mouse_x, mouse_y, self.__box_size)
            else:
                self.__item.draw_build_preview(
                    self.__grid, self.__player, mouse_x, mouse_y)

    def left_click(self, mouse_x, mouse_y, is_mouse_in_inventory_screen, inventory, index, replenish=False):
        if is_mouse_in_inventory_screen:
            self.grab(inventory, index, replenish)
            return

        if self.__item is None:
            return

        if not self.__item.is_buildable():
            return

        if self.__item.build(self.__grid, self.__player, mouse_x, mouse_y):
            self.__item.set_amount(self.__item.get_amount() - 1)
            if self.__item.get_amount() <= 0:
                self.__item = None

    def grab(self, inventory, index, replenish=False):
        if index is None:
            return

        if replenish is None:
            self.__player_hotbar.select(None)

        self.__replenish = replenish
        if self.__item is None:
            self.__item = inventory.pop_slot(index)
            return True

        if inventory.get_slot(index) is None:
            inventory.set_slot(index, self.__item)
            self.__item = None
            return True

        if not self.__item.get_item_id() == inventory.get_slot(index).get_item_id():
            temp = self.__item
            self.__item = inventory.pop_slot(index)
            inventory.set_slot(index, temp)
            return True

        if self.__item.get_amount() + inventory.get_slot(index).get_amount() <= self.__item.get_stack_size():
            inventory.get_slot(index).set_amount(
                inventory.get_slot(index).get_amount() + self.__item.get_amount())
            self.__item = None
            return True

        if self.__item.get_amount() + inventory.get_slot(index).get_amount() > self.__item.get_stack_size():
            self.__item.set_amount(self.__item.get_amount() -
                                   (self.__item.get_stack_size() - inventory.get_slot(index).get_amount()))
            inventory.get_slot(index).set_amount(self.__item.get_stack_size())
            return True

    # def update(self):
    #     if self.__item is not None:
    #         if self.__item.get_amount() <= 0:
    #             self.__item = None