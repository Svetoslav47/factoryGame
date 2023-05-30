from items.Item import Item


class PlayerHand():
    def __init__(self, screen, grid, clock, player, player_hotbar, hud, box_size=50):
        self.__screen = screen
        self.__grid = grid
        self.__clock = clock
        self.__player = player
        self.__item = None
        self.__box_size = box_size
        self.__player_hotbar = player_hotbar
        self.__hud = hud
        self._rotation = 0

    def draw(self, mouse_x, mouse_y, is_inventory_open):
        if self.__item is not None:
            if not self.__item.is_buildable():
                self.__item.drawInInventory(mouse_x, mouse_y, self.__box_size)
                return

            if self.__hud.is_mouse_in_inventory_window(mouse_x, mouse_y) and is_inventory_open:
                self.__item.drawInInventory(mouse_x, mouse_y, self.__box_size)
            else:
                self.__item.draw_build_preview(
                    self.__grid, self.__player, mouse_x, mouse_y, self._rotation)

    def left_click(self, mouse_x, mouse_y, is_inventory_open):

        if self.__hud.is_mouse_in_inventory_window(mouse_x, mouse_y) and is_inventory_open:
            if not self.__hud.is_mouse_in_player_recipies(mouse_x, mouse_y):
                inventory, index = self.__hud.get_box_from_screen(
                    mouse_x, mouse_y)

                self._grab(inventory, index)
                return

        if self.__hud.is_mouse_in_player_recipies(mouse_x, mouse_y) and is_inventory_open:
            recepie = self.__hud.get_recepie_from_screen(mouse_x, mouse_y)
            if recepie is None:
                return
            self.__player.craft(recepie)
            return

        if self.__item is None:
            x_grid, y_grid = self.__grid.screen_to_grid(
                mouse_x, mouse_y, self.__player)
            building = self.__grid.get_tile_building(x_grid, y_grid)
            if building is not None:
                self.__player.open_building(building)
            return

        if not self.__item.is_buildable():
            return

        if self.__item.build(self.__grid, self.__clock, self.__player, mouse_x, mouse_y, self._rotation):
            self.__item.set_amount(self.__item.get_amount() - 1)
            if self.__item.get_amount() <= 0:
                self.__item = None

    def rotate(self):
        self._rotation += 1
        if self._rotation > 3:
            self._rotation = 0

    def _grab(self, inventory, index):
        if self.__item is None:
            self.__item = inventory.pop_slot(index)
            return True

        if inventory.get_slot(index) is None:
            inventory.set_slot(index, self.__item)
            self.__item = None
            return True

        if not self.__item.item_id == inventory.get_slot(index).item_id:
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
