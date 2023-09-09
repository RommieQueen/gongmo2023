import pygame

pygame.init()

class Button:
    def __init__(self, input_screen, x_pos, y_pos, input_image, image_width, image_height, action = None):
        mouse_pos = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed()
        if x_pos + image_width > mouse_pos[0] > x_pos and y_pos + image_height > mouse_pos[1] > y_pos:
            input_screen.blit(input_image, (x_pos, y_pos))
            if mouse_press[0] and action is not None:
                action()                            
        else:
            input_screen.blit(input_image, (x_pos, y_pos))

def collision_entity(entity_1, entity_2):
    collisions = pygame.sprite.spritecollide(entity_1, entity_2, False, pygame.sprite.collide_mask)
    if collisions:
        return True
    return False
