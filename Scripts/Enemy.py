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

rect = pygame.rect.Rect

# 적 클래스
class Enemy(pygame.sprite.Sprite):
    def __init__(self, y, health, speed, *images):
        super().__init__()
        self.images = []

        # 애니메이션 리스트에 가변인자 자동대입
        i = 0
        for i in range(0, len(self.images)):
            self.images[i] = images[i]
        self.image = images[0]

        rect = self.image.get_rect()
        rect.x = screen_width  # position
        rect.y = y

        self.speed = random.randrange(speed, speed+3)
        self.health = health
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
            rect.x -= self.speed
            if rect.right < 0:
                self.kill()
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

