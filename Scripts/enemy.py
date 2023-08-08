import time
import pygame
import sys
import random
import scope as s
import stage as stage

screen_width, screen_height = 1280, 720

RED = (219,0,0)
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

        self.scope = s.Scope()
        self.scope_point = s.ScopePoint(self.scope)
        self.is_collide_scope = False
        self.hurt_image = self.image
        
        self.time = 0
        self.is_hitable = True

        self.need_kill = 100
        self.now_kill = self.need_kill
        self.kill_font = pygame.font.Font('./../Fonts/NeoDunggeunmoPro-Regular.ttf',30)
        self.now_kill_msg = self.kill_font.render(f"{self.now_kill}/{self.need_kill}",True, (255,255,255))
        
    def update(self, player_is_move, player_rect_x, player_speed):
        from main import screen

        #보내버린 적 얼마나?
        self.kill_msg(screen)

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
            
        if player_is_move:
            # player 위치가 화면 끝 근처인 경우, 원래 속도를 player 속도d로 변경
            if player_rect_x <= 160:
                self.rect.x += player_speed
            elif player_rect_x >= 1220:
                self.rect.x -= player_speed

        #체력 0이면 없애기 (작중에선 외계행성으로 이동)
        if self.health <= 0:
            self.remove()
            self.now_kill -= 1

    #내가만든 hit함수 너를위해 구웠지
    def hit(self):
        if self.is_hitable:
            self.health -= 1
            print(self.health)
            self.is_hitable = False
            
        self.time += 1
        if self.time >= 500:
            self.is_hitable = True
            self.time = 0
        
    def hurt(self, screen):
        self.hurt_image.fill(RED)
        self.hurt_image.set_alpha(127)
        screen.blit(self.hurt_image, self.rect)
        
    def kill_msg(self,screen):
        screen.blit(self.now_kill_msg, (1100,20))
        
        #체력, 맞으면 색깔은 빨간색인데 알파값이 약간 섞인 듯한 색깔, 0.3초 동안 일시정지 그 후 다시 원래 색으로 돌아오기
        #체력이 0이 되면 반짝이면서 사라지기
        #kill로 이미지 삭제.
