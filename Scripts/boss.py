import time
import pygame
import sys
import random



screen_width, screen_height = 1280, 720

RED = (219,0,0)
# 적(Enemy) 클래스 정의
class BossCat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./../Images/sprites/enemy/boss/part_1_boss.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect = (0, -101)
        self.mask = pygame.mask.from_surface(self.image)  
        self.masks = [self.mask]  # Boss 클래스에도 masks 속성 추가
        self.health = 1500
        self.is_hit = False
        self.hit_alpha = 100
        self.hit_timer = 0
        
    def update(self):
        if self.is_hit:  #is_hit로 상태 감지. 현재 True인 상태를 감지.
            if pygame.time.get_ticks() - self.hit_timer > 100:  # 0.5초 동안 유지
                self.is_hit = False
                self.hit_alpha = 100
                self.image.set_alpha(255)

    def hit(self):
        if not self.is_hit:     #is_hit로 상태 감지 False를 감지하는 이유는 False일 때 감지하고 True로 바꿔서 update에서 작용. 
            self.health -= 1

            if self.health <= 0:    #health가 0이하면 죽이고 아니면 is_hit를 True로 바꾸고 alpha = 100.
                self.kill()

            else:
                self.is_hit = True
                self.hit_alpha = 100
                self.hit_timer = pygame.time.get_ticks()
                self.image.set_alpha(self.hit_alpha)

