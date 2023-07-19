import pygame
import import_image as images
import random

# 초기화
pygame.init()

# 게임 화면 설정
screen_width = 1280
screen_height = 720

# FPS 설정
clock = pygame.time.Clock()
FPS = 60

enemy_walk_1 = images.enemy_right1
enemy_walk_1 = pygame.transform.scale(enemy_walk_1, (300, 300))
enemy_walk_2 = images.enemy_right2
enemy_walk_2 = pygame.transform.scale(enemy_walk_2, (300, 300))
enemy_walk_3 = images.enemy_right3
enemy_walk_3 = pygame.transform.scale(enemy_walk_3, (300, 300))

# 적 클래스
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = []

        self.images.append(enemy_walk_1)
        self.images.append(enemy_walk_2)
        self.images.append(enemy_walk_3)
        
        self.rect = self.images[0].get_rect()
        self.rect.x = screen_width
        self.rect.y = 300
        self.speed = random.randrange(5, 6)
        self.health = 3
        self.is_hit = False
        self.hit_alpha = 100
        self.hit_timer = 0
        self.frame = 0

    def update(self):
        if self.is_hit:
            if pygame.time.get_ticks() - self.hit_timer > 500:  # 0.5초 동안 유지
                self.is_hit = False
                self.hit_alpha = 100
                self.image.set_alpha(255)
        else:
            self.rect.x -= self.speed
            if self.rect.right < 0:
                self.kill()

        self.frame += 1
        if self.frame >= len(self.images) * 10:
            self.frame = 0
        self.image = self.images[self.frame // 10]

    def hit(self):
        if not self.is_hit:
            self.health -= 1
            if self.health <= 0:
                self.kill()
            else:
                self.is_hit = True
                self.hit_alpha = 100
                self.hit_timer = pygame.time.get_ticks()
                self.image.set_alpha(self.hit_alpha)

# 적 그룹
enemies = pygame.sprite.Group()

