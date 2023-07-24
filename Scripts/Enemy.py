import pygame
import sys
import random
import time

screen_width, screen_height = 1280, 720

# 적(Enemy) 클래스 정의
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./../Images/sprites/enemy/alien_stand.png')
        self.image = pygame.transform.scale(self.image, (160, 160))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, screen_width - 50), random.randint(0, screen_height - 600))
        self.speed = random.randint(2, 3)
        self.original_speed = self.speed
        self.direction = random.choice(["right", "left"])
        self.is_on_ground = False

    def update(self, player_is_move, player_rect_x, player_speed):
        if not self.is_on_ground:
            self.rect.y += self.speed
        else:
            self.speed = random.randint(1, 3)

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
