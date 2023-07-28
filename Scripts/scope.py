import pygame
import import_image as images
import enemy as e

pygame.init()

class Scope(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./../Images/ui/scope_normal.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        
        self.rect = self.image.get_rect()
        
        self.mask = pygame.mask.from_surface(self.image)

    def collide_enemy(self):
        self.image = pygame.image.load('./../Images/ui/scope_collide.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        
        self.rect = self.image.get_rect()
        
        self.mask = pygame.mask.from_surface(self.image)

    def normal(self):
        self.image = pygame.image.load('./../Images/ui/scope_normal.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        
        self.rect = self.image.get_rect()
        
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, screen, mouse_x, mouse_y):
        self.rect.center = (mouse_x, mouse_y)
        screen.blit(self.image, self.rect)

class ScopePoint(pygame.sprite.Sprite): #실제 충돌감지하는 거, 야매
    def __init__(self, scope):
        super().__init__()
        self.img = images.scope_point.convert_alpha()
        self.scope = scope
        self.rect = self.img.get_rect()
    def draw_point(self, screen):
        self.img.set_alpha(0)
        self.rect = self.img.get_rect()
        self.mask = pygame.mask.from_surface(self.img)
        center_x = self.scope.rect.centerx - self.img.get_width() // 2
        center_y = self.scope.rect.centery - self.img.get_height() // 2
        self.rect.center = (center_x, center_y)

        screen.blit(self.img, self.rect.center)

