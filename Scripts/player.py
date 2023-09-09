import pygame
import stage as s
import enemy as e
import time
import import_image as imgs
import game_manager as manager
pygame.init()

enemy = e.Enemy()

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super(Player, self).__init__()

        # ?��미�??�? Rect?��?�� ?���? ?��?�� Rect?�� ?���? �??��
        # ?��미�???�� ?��기�?? 같게 ?��거나, ?��기�?? ?��르게 ?��?���? pygame.transform.scale?�� ?��?��?��?�� rect ?��?��
        # ?��미�??�? 맞추?���? ?��?��.
        size = (92, 184) 

        # ?��?��?��?�� ?��미�??�? 리스?���? ????��?��?��. ?��미�?? 경로?�� ?��?��?��?�� 경로�? ?��?��?��?��.
        images = []

        # ?��?��?�� ?��?�� 0 ~ 5
        images.append(pygame.image.load('./../Images/sprites/player/player_idle.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_idle.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_idle.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_idle.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_idle.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_idle.png'))

        # 걷기 6 ~ 17
        images.append(pygame.image.load('./../Images/sprites/player/player_walk_1.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_walk_1.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_walk_2.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_walk_2.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_walk_3.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_walk_3.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_walk_4.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_walk_4.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_walk_5.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_walk_5.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_walk_6.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_walk_6.png'))

        # ?��?�� ?��?�� 18
        images.append(pygame.image.load('./../Images/sprites/player/player_sit.png'))

        # ?��?�� 공격?��?�� ?��?�� 19
        images.append(pygame.image.load('./../Images/sprites/player/player_stand_attack.png'))

        # ?��?��?�� 공격?���? ?��?�� 20
        images.append(pygame.image.load('./../Images/sprites/player/player_sit_attack.png'))

        #stage2 _ sword attack 21~24
        images.append(pygame.image.load('./../Images/sprites/player/player_sword1.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_sword2.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_sword3.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_sword4.png'))

        # Rect ?��기�?? Image ?���? 맞추�?. pygame.transform.scale
        self.images = [pygame.transform.scale(image, size) for image in images]

        # rect 만들�?
        self.rect = pygame.Rect(position, size)

        # masks 만들�?
        self.masks = [pygame.mask.from_surface(image) for image in self.images]

        # ?���? 캐릭?�� ?��미�???��
        self.images_right = images
        
        # 캐릭?�� ?��미�??�? ?��른쪽?�� 보고 ?��?��?��, ?��쪽으�? 보도�? ?���? ?��?��?��?��
        # ?��미�??�? ?���? 기�???���? 좌우�? ?��집이 �??��. pygame.transform.flip 메서?�� ?��?��
        self.images_left = [pygame.transform.flip(image, True, False) for image in images]

        # 캐릭?��?�� ?��?�� ?��?��
        self.keys = pygame.key.get_pressed()
        # 0 - idle ?��?��, 1 - 걷고 ?��?�� ?��?��
        self.state = 0
        self.keys = pygame.key.get_pressed()
        
        # 방향
        self.direction = 'right'
        
        # ?��?��
        self.velocity_x = 0

        # 캐릭?��?�� 첫번�? ?��미�??
        self.index = 0
        self.image = images[self.index]

        # 1초에 보여�? 1?��?�� ?��미�?? ?��간을 계산, ?��?��?�� 3?��리까�? 반올�?
        self.animation_time = round(100 / len(self.images * 100), 2)

        # mt??? 결합?��?�� animation_time?�� 계산?�� ?���? 초기?��
        self.current_time = 0

        # player�? ???직이?�� ?��?��
        self.isMove = False

        # player�? 조�??중인�? ?��?��
        self.isAiming = False

        # player 체력 �?�?
        self.is_hit = False
        self.hit_timer = 0
        self.is_die = False
        self.player_health = 100
        self.max_health = 100

        #stage2 _ dash
        self.is_dash = False
        self.dash_time = 0
        self.dash_speed = 70

        #stage2 _ sword
        self.is_charging = False
        self.charging = 0
        self.is_sword = True
        self.power = 1
        self.sword_x = 0
        self.sword_y = 500
        self.is_effect = False
        self.effect_time = pygame.time.get_ticks()

    # update�? ?��?�� 캐릭?��?�� ?��미�??�? 계속 반복?��?�� ?��????��?���? ?��?��.
    def update(self, mt):
        #?��보드�? player ?��?��
        self.keys = pygame.key.get_pressed()

        if not self.isAiming and not self.is_charging:
            # ?��쪽으�? ?��?���??��
            if self.keys[pygame.K_a]:

                self.direction = "left"
                self.state = 1
                if self.rect.right > 160:
                    self.rect.x -= self.velocity_x
                    self.isMove = False
                else:
                    self.isMove = True
            # ?��른쪽?���? ?��?���??��
            if self.keys[pygame.K_d]:
                self.direction = "right"
                self.state = 1
                if self.rect.right < 1220:
                    self.rect.x += self.velocity_x
                    self.isMove = False
                else:
                    self.isMove = True
            # ?���? �??��
            if self.keys[pygame.K_s]:
                self.state = 2

        # ?��?�� ?��?��?�� ?��?�� 반복?���? ?��미�???�� index ?��?���? ?��?��
        if self.state == 0:
            count = 6
            start_Index = 0
            self.velocity_x = 0
        elif self.state == 1:
            count = 6
            start_Index = 6
            self.velocity_x = 6
        elif self.state == 2:
            count = 1
            start_Index = 18
            self.velocity_x = 0
        elif self.state == 3:
            count = 1
            start_Index = 19
            self.velocity_x = 0
        elif self.state == 4:
            count = 1
            start_Index = 20
            self.velocity_x = 0

        #sword 충전
        elif self.state ==5:
            count = 1
            start_Index = 21
            self.velocity_x = 0
        #sword ?��?��르기
        elif self.state == 6:
            count = 3
            start_Index = 22
            self.velocity_x = 0

        # 방향?�� ?��른쪽?���?, ?��른쪽 ?��미�?? ?��?��
        if self.direction == 'right':
            self.images = self.images_right
        # 방향?�� ?��쪽이�? ?���? ?��미�?? ?��?��
        elif self.direction == 'left':
            self.images = self.images_left

        # loop ?���? ?��?���?
        self.current_time += mt

        # loop time 경과�? animation_time?�� ?��?��?���? ?��로운 ?��미�?? 출력
        if self.current_time >= self.animation_time:
            self.current_time = 0

            # ?��?��?�� ?��?�� ?��미�?? index 범위�? ?��르게 ?��?��?��?��.
            self.index = (self.index % count) + start_Index

            self.image = self.images[self.index]
            self.index += 1

            if self.index >= len(self.images):
                self.index = 0

        if self.is_hit:  #is_hit�? ?��?�� 감�??. ?��?�� True?�� ?��?���? 감�??.
            if pygame.time.get_ticks() - self.hit_timer > 500:  # 0.5�? ?��?�� ?���?
                self.is_hit = False

        if self.is_effect:
            if pygame.time.get_ticks() - self.effect_time > 700:
                self.is_effect = False

    def hit(self):
        if not self.is_hit:
            self.player_health -= 20

        if self.player_health <= 0:
            self.is_die = True
        else:
            self.is_hit = True
            self.hit_timer = pygame.time.get_ticks()

    def hp(self, screen):
        health_bar_width = 80
        health_bar_height = 10
        health_bar_x = self.rect.x + 7
        health_bar_y = self.rect.y - 15
        pygame.draw.rect(screen, (255, 0, 0), (health_bar_x, health_bar_y, health_bar_width, health_bar_height))
        
        current_health_width = (self.player_health / self.max_health) * health_bar_width
        pygame.draw.rect(screen, (0, 255, 0), (health_bar_x, health_bar_y, current_health_width, health_bar_height))

    # ------- ?��기�???�� part2?�� ?��?��?��?��. ------- #
    def dash(self): # 로직 ?��?��, ?��?��메이?�� ?���?
        if not self.is_dash:
            self.is_dash = True

            if self.direction == "right":
                self.rect.x += self.dash_speed
                self.rect.x += self.dash_speed

            elif self.direction == "left":
                self.rect.x -= self.dash_speed
                self.rect.x -= self.dash_speed

        if pygame.time.get_ticks() - self.dash_time > 3000:
            self.is_dash = False
            self.dash_time = pygame.time.get_ticks()
    def sword_charging(self):
        self.state = 5
        self.is_sword = False

    def sword_attack(self):
        if not self.is_sword:
            for i in range(22,25):
                self.image = self.images[i]

# --------- SWORD EFFECT --------------------- #
class SwordEffect(pygame.sprite.Sprite):
    def __init__(self, power, player):
        super().__init__()
        self.image = imgs.power1
        self.power = power
        self.kill_time = pygame.time.get_ticks()
        self.rect = self.image.get_rect()
        self.direction = player.direction
        self.mask = pygame.mask.from_surface(self.image)
        self.is_effect = False
        self.accel_speed = 5 # �??��?��
        self.rect.y  = player.rect.y

        if self.direction == "right":
            self.rect.x = player.rect.right
        elif self.direction =="left":
            self.rect.x = player.rect.left - 50

        # animation
        self.images = []

        if self.power == 1:
            self.image = imgs.power1
        elif self.power == 2:
            self.image = imgs.power2
        elif self.power == 3:
            self.image = imgs.power3

        if self.direction == "left":
            self.image = pygame.transform.flip(self.image,True, False)
    def update(self):
        self.accel_speed += 1
        self.is_effect = True
        if self.direction == "right":
            self.rect.x += self.accel_speed
        elif self.direction =="left":
            self.rect.x -= self.accel_speed

        if pygame.time.get_ticks() - self.kill_time > 300:
           self.kill()
           self.is_effect = False
