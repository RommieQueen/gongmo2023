import pygame
pygame.init()
import import_image as images
import Enemy as enemy

class Scope():
    def __init__(self):
        self.scope_list = [images.scope_normal, images.scope_collide]
        self.scope = self.scope_list[0]
        self.mouse_pos = pygame.mouse.get_pos()
        self.scope_pos = (self.mouse_pos[0] - 50//2, self.mouse_pos[1] - 50//2)
        self.rect = self.scope_list[0].get_rect()

        self.is_onEnemy = False
    def update(self, screen):

        self.mouse_pos = pygame.mouse.get_pos()
        self.scope_pos = [self.mouse_pos[0] - 50 // 2, self.mouse_pos[1] - 50 // 2]

        if enemy.rect.topleft<self.scope_pos and enemy.rect.bottomright> self.scope_pos:
            self.is_onEnemy = True
        else:
            self.is_onEnemy = False

        if self.is_onEnemy:
            self.scope = self.scope_list[1]
        else:
            self.scope = self.scope_list[0]
        screen.blit(self.scope, self.scope_pos)
        