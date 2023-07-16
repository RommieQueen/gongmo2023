import pygame
pygame.init()
import import_image as images

class Player:
    def position(self):
        right_walk_list = [images.player_right1, images.player_right2, images.player_right3, images.player_right4,
                           images.player_right5, images.player_right6]

        key = pygame.key.get_pressed()

        posX = 0
        speed = 5

        if key[pygame.K_d]:
            posX += speed
        elif key[pygame.K_a]:
            posX -= speed

        return posX

    def gun(self):
        pass
