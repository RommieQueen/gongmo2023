import pygame
import import_image as images
pygame.init()

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = images.part2_boss
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
class Long_Branch(pygame.sprite.Sprite):
    def __init__(self):
        pass
class Short_Branch(pygame.sprite.Sprite):
    pass