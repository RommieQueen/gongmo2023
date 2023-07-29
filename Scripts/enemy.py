import pygame
import sys
import random
import time
import stage as stage
from scope import Scope

screen_width, screen_height = 1280, 720

# 적(Enemy) 클래스 정의
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./../Images/sprites/enemy/alien_stand.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (160, 160))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, screen_width - 50), random.randint(0, screen_height - 600))
        self.speed = random.randint(2, 3)
        self.original_speed = self.speed
        self.direction = random.choice(["right", "left"])
        self.is_on_ground = False
        self.mask = pygame.mask.from_surface(self.image)  
        self.masks = [self.mask]  # Enemy 클래스에도 masks 속성 추가
        self.health = 3

        #hit
        #self.is_mouse = False
        #self.scope = Scope()

    def update(self, player_is_move, player_rect_x, player_speed):
        if not self.is_on_ground:
            self.rect.y += self.speed
        else:
            self.speed = random.randint(1, 2)

            if random.random() < 0.01:
                self.direction = random.choice(["right", "left"])

            if self.direction == "right":
                self.rect.x += self.speed
            elif self.direction == "left":
                self.rect.x -= self.speed

        # 땅에 닿았는지 확인
        if self.rect.bottom >= screen_height - 100:
            self.is_on_ground = True
        else:
            self.is_on_ground = False
            
        if player_is_move == True:
            # player 위치가 화면 끝 근처인 경우, 원래 속도를 player 속도로 변경
            if player_rect_x <= 160:
                self.rect.x += player_speed
            elif player_rect_x >= 1220:
                self.rect.x -= player_speed

    #내가만든 hit함수 너를위해 구웠지
    def hit(self):

        print("i")
        timer = pygame.time.get_ticks()
        self.health -= 1

       #체력, 맞으면 색깔은 빨간색인데 알파값이 약간 섞인 듯한 색깔, 0.3초 동안 일시정지 그 후 다시 원래 색으로 돌아오기
        #체력이 0이 되면 반짝이면서 사라지기
        #kill로 이미지 삭제.
