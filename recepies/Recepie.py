import pygame


class Recepie:
    def can_craft(ingredients, inventory):
        for ingredient in ingredients:
            if inventory.amount_of_item(ingredient[0].item_id) < ingredient[1]:
                # print(ingredient[0])
                # print("Not enough " +
                #       ingredient[0].item_id + " to craft")
                return False
        return True

    def get_ingredients(ingredients):
        return ingredients

    def get_craft_time(time_to_craft):
        return time_to_craft

    def get_result(screen, result, amount):
        return result(screen, amount)

    def draw_preview(screen, x, y, image, box_size):
        image = pygame.transform.scale(image, (box_size, box_size))
        screen.blit(image, (x, y))
