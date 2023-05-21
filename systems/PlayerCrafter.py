class PlayerCrafter:
    def __init__(self, screen, clock, inventory, craft_speed=1):
        self._screen = screen
        self._clock = clock
        self._inventory = inventory
        self._queue = []
        self._crafting_time = 0
        self._craft_speed = craft_speed
        self._is_crafting = False
        self._type = "crafter"

    def update(self):
        if len(self._queue) > 0:
            self._is_crafting = True
            self._crafting_time += self._craft_speed / \
                self._clock.get_fps()
            if self._crafting_time >= self._queue[0].get_craft_time():
                self._crafting_time = 0
                self._inventory.add_item(
                    self._queue[0].get_result(self._screen))
                self._queue.pop(0)
                self.is_crafting = False

    def _add_to_queue(self, recepie):
        self._queue.append(recepie)

    def craft(self, recepie):
        if recepie.can_craft(self._inventory):
            for ingredient in recepie.get_ingredients():
                self._inventory.remove_item(
                    ingredient[0].get_item_id(), ingredient[1])
            self._add_to_queue(recepie)

    def get_queue(self):
        return self._queue

    def get_crafting_progress(self):
        return self._queue[0].get_craft_time() / self._crafting_time
