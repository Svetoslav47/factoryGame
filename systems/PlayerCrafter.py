class PlayerCrafter:
    def __init__(self, screen, clock, inventory, craft_speed=1):
        self._screen = screen
        self._clock = clock
        self._inventory = inventory
        self._queue = []
        self._crafting_progress = 0
        self._crafting_time = 0
        self._craft_speed = craft_speed
        self._is_crafting = False
        self._type = "crafter"

    def update(self):
        if self._is_crafting:
            self._crafting_progress += 1 / (self._crafting_time *
                                            (1 / self._clock.get_fps()))
            if self._crafting_progress >= 1:
                self._crafting_progress = 0
                self._is_crafting = False
                result, amount = self._queue.pop(0).get_result()
                self._inventory.add_item(result(self._screen, amount))

    def _add_to_queue(self, recepie):
        self._queue.append(recepie)

    def start_crafting(self, recepie):
        if recepie.can_craft(self._inventory):
            self._add_to_queue(recepie)
            self._crafting_time = recepie.get_craft_time(self._craft_speed)
            self._is_crafting = True

    def get_queue(self):
        return self._queue

    def get_crafting_progress(self):
        return self._crafting_progress
