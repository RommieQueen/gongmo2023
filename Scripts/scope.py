import pygame
pygame.init()
import import_image as images
import enemy as e

class Scope(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./../Images/ui/scope_collide.png').convert_alpha()
        
        self.image = pygame.transform.scale(self.image, (40, 40))
        
        self.rect = self.image.get_rect()
        
        self.mask = pygame.mask.from_surface(self.image)  
        self.masks = [self.mask]
        
    def toMouse(self, mouse_x, mouse_y):
        self.rect.center = (mouse_x, mouse_y)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    
        
