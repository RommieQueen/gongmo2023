import time
import pygame
import sys
import random
import import_image as images


screen_width, screen_height = 1280, 720

RED = (219,0,0)
# 적(Boss) 클래스 정의
class BossCat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./../Images/sprites/enemy/boss/part_1_boss.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (1024, 576))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2 -29)
        self.mask = pygame.mask.from_surface(self.image)  
        self.masks = [self.mask]  # Boss 클래스에도 masks 속성 추가
        self.boss_health = 700
        self.max_health = 700
        self.is_hit = False
        self.is_die = False
        self.hit_alpha = 100
        self.hit_timer = 0
        self.is_awake = False
        
    def update(self):
        if self.is_hit:  #is_hit로 상태 감지. 현재 True인 상태를 감지.
            if pygame.time.get_ticks() - self.hit_timer > 200:  # 0.2초 동안 유지
                self.is_hit = False
                self.hit_alpha = 100
                self.image.set_alpha(255)

    def hit(self):
        if not self.is_hit:
            self.boss_health -= 2

        if self.boss_health <= 0:
            self.is_die = True
        else:
            self.is_hit = True
            self.hit_alpha = 100
            self.hit_timer = pygame.time.get_ticks()
            self.image.set_alpha(self.hit_alpha)

    def hp(self, screen):
        health_bar_width = 1280
        health_bar_height = 40
        health_bar_x = 0
        health_bar_y = 0
        pygame.draw.rect(screen, (255, 0, 0), (health_bar_x, health_bar_y, health_bar_width, health_bar_height))
        
        current_health_width = (self.boss_health / self.max_health) * health_bar_width
        pygame.draw.rect(screen, (0, 255, 0), (health_bar_x, health_bar_y, current_health_width, health_bar_height))

class BossCatAttack(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./../Images/sprites/enemy/boss/part_1_boss_attack.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 200))        
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, screen_width - 50), random.randint(0, screen_height - 600))
        self.speed = 20
        self.mask = pygame.mask.from_surface(self.image)  
        self.masks = [self.mask]  # BossAttack 클래스에도 masks 속성 추가
        self.health = 1
        self.is_hit = False
        self.is_on_ground = False
        self.is_wait_attack_drop = True
        self.wait_attack_drop_time = pygame.time.get_ticks()

        if self.rect.x < screen_width // 2:
            self.image = pygame.transform.flip(self.image, True, False)
        
    def update(self):

        if self.is_wait_attack_drop:
            self.rect.y = 0 
            if pygame.time.get_ticks() - self.wait_attack_drop_time > 1000:
                self.is_wait_attack_drop = False

        if not self.is_wait_attack_drop:
            self.rect.y += self.speed
            
        # 땅에 닿았는지 확인
        if self.rect.bottom >= screen_height - 100:
            self.kill()

 # ---------- PART 2 ------------------------------------------------ #
class TreeBoss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = images.part2_boss
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.max_health = 1000
        self.boss_health = self.max_health
        self.is_hit = False
        self.hit_alpha = 100
        self.hit_timer = pygame.time.get_ticks()

    def hp(self, screen):
        health_bar_width = 1280
        health_bar_height = 40
        health_bar_x = 0
        health_bar_y = 0
        pygame.draw.rect(screen, (255, 0, 0), (health_bar_x, health_bar_y, health_bar_width, health_bar_height))

        current_health_width = (self.boss_health / self.max_health) * health_bar_width
        pygame.draw.rect(screen, (0, 255, 0), (health_bar_x, health_bar_y, current_health_width, health_bar_height))

    def update(self):
        if self.is_hit:  #is_hit로 상태 감지. 현재 True인 상태를 감지.
            if pygame.time.get_ticks() - self.hit_timer > 200:  # 0.2초 동안 유지
                self.is_hit = False
                self.hit_alpha = 100
                self.image.set_alpha(255)

    def hit(self, damage):
        if not self.is_hit:
            self.boss_health -= damage

        if self.boss_health <= 0:
            self.is_die = True
        else:
            self.is_hit = True
            self.hit_alpha = 100
            self.hit_timer = pygame.time.get_ticks()
            self.image.set_alpha(self.hit_alpha)

class Long_Branch(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = images.long_branch
        self.right_image = images.long_branch
        self.left_image = pygame.transform.flip(self.image,True,False)
        self.rect = self.image.get_rect()
        self.rect.center = [0,0]
        self.mask = pygame.mask.from_surface(self.image)
        self.directions = ["left","right"]
        self.direction = random.choice(self.directions)
        self.speed = 40
        self.wait_time = pygame.time.get_ticks()
        self.kill_time = pygame.time.get_ticks()

        if self.direction == "right":
            self.rect.center = [1280+200, 500]
            self.image = self.right_image
        elif self.direction == "left":
            self.rect.center = [-200,500]
            self.image = self.left_image
    def update(self):
        # 드러나기 & kill
        if pygame.time.get_ticks() - self.wait_time > 500:
            if self.direction == "right":
                self.rect.x -= self.speed
                if self.rect.x <= 1280-630:
                    self.rect.x = 1280-630
                    if pygame.time.get_ticks() - self.kill_time > 4000:
                        self.kill()

            elif self.direction == "left":
                self.rect.x += self.speed
                if self.rect.x >= 0:
                    self.rect.x = 0
                    if pygame.time.get_ticks() - self.kill_time > 4000:
                        self.kill()

class Short_Branch(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = images.short_branch
        self.warning = images.warning
        self.warning_rect = self.warning.get_rect()
        self.rand_x = random.randrange(50,1220)
        self.rect = self.image.get_rect()
        self.rect.center = [self.rand_x,720]
        self.mask = pygame.mask.from_surface(self.image)
        self.is_warning = True
        self.warning_time = pygame.time.get_ticks()
    def warning(self,SCREEN):
        SCREEN.blit(self.warning, (self.rand_x,320))

        if pygame.time.get_ticks() - self.warning_time > 600:
            self.update()
            self.warning_time = pygame.time.get_ticks()

    def update(self):
        self.rect.center[1] += 20
        if self.y >= 0:
            self.y = 0