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

        # ?΄λ―Έμ??λ₯? Rect?? ?£κΈ? ??΄ Rect? ?¬κΈ? μ§?? 
        # ?΄λ―Έμ??? ?¬κΈ°μ?? κ°κ² ?κ±°λ, ?¬κΈ°λ?? ?€λ₯΄κ² ??€λ©? pygame.transform.scale? ?¬?©??¬ rect ??
        # ?΄λ―Έμ??λ₯? λ§μΆ?λ‘? ??€.
        size = (92, 184) 

        # ?¬?¬?₯? ?΄λ―Έμ??λ₯? λ¦¬μ€?Έλ‘? ????₯??€. ?΄λ―Έμ?? κ²½λ‘? ?? ?€? κ²½λ‘λ₯? ?¬?©??€.
        images = []

        # ??? ?? 0 ~ 5
        images.append(pygame.image.load('./../Images/sprites/player/player_idle.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_idle.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_idle.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_idle.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_idle.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_idle.png'))

        # κ±·κΈ° 6 ~ 17
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

        # ?? ?? 18
        images.append(pygame.image.load('./../Images/sprites/player/player_sit.png'))

        # ?? κ³΅κ²©?? ?? 19
        images.append(pygame.image.load('./../Images/sprites/player/player_stand_attack.png'))

        # ??? κ³΅κ²©?κ³? ?? 20
        images.append(pygame.image.load('./../Images/sprites/player/player_sit_attack.png'))

        #stage2 _ sword attack 21~24
        images.append(pygame.image.load('./../Images/sprites/player/player_sword1.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_sword2.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_sword3.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_sword4.png'))

        # Rect ?¬κΈ°μ?? Image ?¬κΈ? λ§μΆκΈ?. pygame.transform.scale
        self.images = [pygame.transform.scale(image, size) for image in images]

        # rect λ§λ€κΈ?
        self.rect = pygame.Rect(position, size)

        # masks λ§λ€κΈ?
        self.masks = [pygame.mask.from_surface(image) for image in self.images]

        # ?λ³? μΊλ¦­?° ?΄λ―Έμ???€
        self.images_right = images
        
        # μΊλ¦­?° ?΄λ―Έμ??κ°? ?€λ₯Έμͺ½? λ³΄κ³  ???°, ?Όμͺ½μΌλ‘? λ³΄λλ‘? ?κΈ? ??΄??
        # ?΄λ―Έμ??λ₯? ?Έλ‘? κΈ°μ???Όλ‘? μ’μ°λ‘? ?€μ§μ΄ μ€??€. pygame.transform.flip λ©μ? ?¬?©
        self.images_left = [pygame.transform.flip(image, True, False) for image in images]

        # μΊλ¦­?°? ??¬ ??
        self.keys = pygame.key.get_pressed()
        # 0 - idle ??, 1 - κ±·κ³  ?? ??
        self.state = 0
        self.keys = pygame.key.get_pressed()
        
        # λ°©ν₯
        self.direction = 'right'
        
        # ??
        self.velocity_x = 0

        # μΊλ¦­?°? μ²«λ²μ§? ?΄λ―Έμ??
        self.index = 0
        self.image = images[self.index]

        # 1μ΄μ λ³΄μ¬μ€? 1?₯? ?΄λ―Έμ?? ?κ°μ κ³μ°, ???  3?λ¦¬κΉμ§? λ°μ¬λ¦?
        self.animation_time = round(100 / len(self.images * 100), 2)

        # mt??? κ²°ν©??¬ animation_time? κ³μ°?  ?κ°? μ΄κΈ°?
        self.current_time = 0

        # playerκ°? ???μ§μ΄? ??Έ
        self.isMove = False

        # playerκ°? μ‘°μ??μ€μΈμ§? ??Έ
        self.isAiming = False

        # player μ²΄λ ₯ κ΄?λ¦?
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

    # updateλ₯? ?΅?΄ μΊλ¦­?°? ?΄λ―Έμ??κ°? κ³μ λ°λ³΅?΄? ??????λ‘? ??€.
    def update(self, mt):
        #?€λ³΄λλ‘? player ?΄?
        self.keys = pygame.key.get_pressed()

        if not self.isAiming and not self.is_charging:
            # ?Όμͺ½μΌλ‘? ?΄?κ°??₯
            if self.keys[pygame.K_a]:

                self.direction = "left"
                self.state = 1
                if self.rect.right > 160:
                    self.rect.x -= self.velocity_x
                    self.isMove = False
                else:
                    self.isMove = True
            # ?€λ₯Έμͺ½?Όλ‘? ?΄?κ°??₯
            if self.keys[pygame.K_d]:
                self.direction = "right"
                self.state = 1
                if self.rect.right < 1220:
                    self.rect.x += self.velocity_x
                    self.isMove = False
                else:
                    self.isMove = True
            # ?κΈ? κ°??₯
            if self.keys[pygame.K_s]:
                self.state = 2

        # ??¬ ??? ?°?Ό λ°λ³΅?΄μ€? ?΄λ―Έμ??? index ?€? κ³? ??
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

        #sword μΆ©μ 
        elif self.state ==5:
            count = 1
            start_Index = 21
            self.velocity_x = 0
        #sword ??λ₯΄κΈ°
        elif self.state == 6:
            count = 3
            start_Index = 22
            self.velocity_x = 0

        # λ°©ν₯?΄ ?€λ₯Έμͺ½?΄λ©?, ?€λ₯Έμͺ½ ?΄λ―Έμ?? ? ?
        if self.direction == 'right':
            self.images = self.images_right
        # λ°©ν₯?΄ ?Όμͺ½μ΄λ©? ?Όμͺ? ?΄λ―Έμ?? ? ?
        elif self.direction == 'left':
            self.images = self.images_left

        # loop ?κ°? ??κΈ?
        self.current_time += mt

        # loop time κ²½κ³Όκ°? animation_time? ??΄?λ©? ?λ‘μ΄ ?΄λ―Έμ?? μΆλ ₯
        if self.current_time >= self.animation_time:
            self.current_time = 0

            # ??? ?°?Ό ?΄λ―Έμ?? index λ²μλ₯? ?€λ₯΄κ² ?€? ??€.
            self.index = (self.index % count) + start_Index

            self.image = self.images[self.index]
            self.index += 1

            if self.index >= len(self.images):
                self.index = 0

        if self.is_hit:  #is_hitλ‘? ?? κ°μ??. ??¬ True?Έ ??λ₯? κ°μ??.
            if pygame.time.get_ticks() - self.hit_timer > 500:  # 0.5μ΄? ?? ? μ§?
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

    # ------- ?¬κΈ°λ???° part2? ?°???€. ------- #
    def dash(self): # λ‘μ§ ??±, ? ?λ©μ΄? ?£κΈ?
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
        self.accel_speed = 5 # κ°???
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
