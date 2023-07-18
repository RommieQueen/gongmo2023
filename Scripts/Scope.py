import pygame
pygame.init()
import import_image as images
class Scope():
    def __init__(self):
        self.scope_list = [images.scope_normal, images.scope_collide]
        self.scope = self.scope_list[0]

    def update(self):
        from main import screen
        self.mouse_pos = pygame.mouse.get_pos()
        self.scope_pos = (self.mouse_pos[0] - 50//2, self.mouse_pos[1] - 50//2)

        screen.blit(self.scope, self.scope_pos)
    def collide(self):
        pass  # enemy 와 접촉하면 이미지 변경
        