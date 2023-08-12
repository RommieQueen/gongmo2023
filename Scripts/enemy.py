import time
import pygame
import sys
import random
import scope as s
import stage as stage
import game_manager as manager

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
        self.speed = random.randint(4, 6)
        self.original_speed = self.speed
        self.direction = random.choice(["right", "left"])
        self.is_on_ground = False
        self.is_jump = False
        self.jump_speed = self.speed
        self.mask = pygame.mask.from_surface(self.image)  
        self.masks = [self.mask]  # Enemy 클래스에도 masks 속성 추가
        self.health = 3
        self.is_hit = False
        self.hit_alpha = 100
        self.hit_timer = 0
        self.frame = 0
        self.blood_particles = []
        #kill_msg
        self.need_kill = 100
        self.now_kill = self.need_kill
        
    def update(self, player_is_move, player_rect_x, player_speed):
        from main import screen

        if not self.is_on_ground and not self.is_jump:
            self.rect.y += self.speed

        else:
            print(self.is_on_ground, self.is_jump)
            self.speed = random.randint(5, 7)

            if random.random() < 0.02 and not self.is_jump:
                self.direction = random.choice(["right", "left"])

            if random.random() < 0.02:
                self.is_jump = True

            if self.direction == "right":
                self.rect.x += self.speed
            elif self.direction == "left":
                self.rect.x -= self.speed

            #점프실행
        if self.is_jump:
            self.rect.y -= self.jump_speed

            if self.rect.y < screen_height - 450:
                self.jump_speed = -self.speed

                if self.rect.bottom >= screen_height - 99:
                    self.is_on_ground=False


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

        if self.is_hit:  #is_hit로 상태 감지. 현재 True인 상태를 감지.
            if pygame.time.get_ticks() - self.hit_timer > 500:  # 0.5초 동안 유지
                self.is_hit = False
                self.hit_alpha = 100
                self.image.set_alpha(255)

        #kill mesage print on screen
        font = pygame.font.Font('./../Fonts/NeoDunggeunmoPro-Regular.ttf', 30)
        kill_text = font.render("{0}/{1}".format(self.need_kill, self.now_kill), True, (255, 255, 255))
        screen.blit(kill_text, (1000,100))

    def hit(self):
        from main import screen
        hit_x, hit_y = pygame.mouse.get_pos()
        if not self.is_hit:     #is_hit로 상태 감지 False를 감지하는 이유는 False일 때 감지하고 True로 바꿔서 update에서 작용. 
            self.health -= 1

            #피 파티클

            if self.health <= 0:    #health가 0이하면 죽이고 아니면 is_hitdddd를 True로 바꾸고 alpha = 100.
                self.kill()
                self.now_kill -= 1

            else:
                self.is_hit = True
                self.hit_alpha = 100
                self.hit_timer = pygame.time.get_ticks()
                self.image.set_alpha(self.hit_alpha)

