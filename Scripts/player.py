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

        # ?ù¥ÎØ∏Ï??Î•? Rect?ïà?óê ?Ñ£Í∏? ?úÑ?ï¥ Rect?ùò ?Å¨Í∏? Ïß??†ï
        # ?ù¥ÎØ∏Ï???ùò ?Å¨Í∏∞Ï?? Í∞ôÍ≤å ?ïòÍ±∞ÎÇò, ?Å¨Í∏∞Î?? ?ã§Î•¥Í≤å ?ïú?ã§Î©? pygame.transform.scale?ùÑ ?Ç¨?ö©?ïò?ó¨ rect ?ïà?óê
        # ?ù¥ÎØ∏Ï??Î•? ÎßûÏ∂î?èÑÎ°? ?ïú?ã§.
        size = (92, 184) 

        # ?ó¨?ü¨?û•?ùò ?ù¥ÎØ∏Ï??Î•? Î¶¨Ïä§?ä∏Î°? ????û•?ïú?ã§. ?ù¥ÎØ∏Ï?? Í≤ΩÎ°ú?äî ?ûê?ã†?ì§?ùò Í≤ΩÎ°úÎ•? ?Ç¨?ö©?ïú?ã§.
        images = []

        # ?Ñú?ûà?äî ?ÉÅ?Éú 0 ~ 5
        images.append(pygame.image.load('./../Images/sprites/player/player_idle.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_idle.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_idle.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_idle.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_idle.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_idle.png'))

        # Í±∑Í∏∞ 6 ~ 17
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

        # ?ïâ?äî ?ÉÅ?Éú 18
        images.append(pygame.image.load('./../Images/sprites/player/player_sit.png'))

        # ?Ñú?Ñú Í≥µÍ≤©?ïò?äî ?ÉÅ?Éú 19
        images.append(pygame.image.load('./../Images/sprites/player/player_stand_attack.png'))

        # ?ïâ?ïÑ?Ñú Í≥µÍ≤©?ïòÍ≥? ?ÉÅ?Éú 20
        images.append(pygame.image.load('./../Images/sprites/player/player_sit_attack.png'))

        #stage2 _ sword attack 21~24
        images.append(pygame.image.load('./../Images/sprites/player/player_sword1.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_sword2.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_sword3.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_sword4.png'))

        # Rect ?Å¨Í∏∞Ï?? Image ?Å¨Í∏? ÎßûÏ∂îÍ∏?. pygame.transform.scale
        self.images = [pygame.transform.scale(image, size) for image in images]

        # rect ÎßåÎì§Í∏?
        self.rect = pygame.Rect(position, size)

        # masks ÎßåÎì§Í∏?
        self.masks = [pygame.mask.from_surface(image) for image in self.images]

        # ?õêÎ≥? Ï∫êÎ¶≠?Ñ∞ ?ù¥ÎØ∏Ï???ì§
        self.images_right = images
        
        # Ï∫êÎ¶≠?Ñ∞ ?ù¥ÎØ∏Ï??Í∞? ?ò§Î•∏Ï™Ω?ùÑ Î≥¥Í≥† ?ûà?äî?ç∞, ?ôºÏ™ΩÏúºÎ°? Î≥¥ÎèÑÎ°? ?ïòÍ∏? ?úÑ?ï¥?Ñú?äî
        # ?ù¥ÎØ∏Ï??Î•? ?Ñ∏Î°? Í∏∞Ï???úºÎ°? Ï¢åÏö∞Î°? ?í§ÏßëÏù¥ Ï§??ã§. pygame.transform.flip Î©îÏÑú?ìú ?Ç¨?ö©
        self.images_left = [pygame.transform.flip(image, True, False) for image in images]

        # Ï∫êÎ¶≠?Ñ∞?ùò ?òÑ?û¨ ?ÉÅ?Éú
        self.keys = pygame.key.get_pressed()
        # 0 - idle ?ÉÅ?Éú, 1 - Í±∑Í≥† ?ûà?äî ?ÉÅ?Éú
        self.state = 0
        self.keys = pygame.key.get_pressed()
        
        # Î∞©Ìñ•
        self.direction = 'right'
        
        # ?Üç?èÑ
        self.velocity_x = 0

        # Ï∫êÎ¶≠?Ñ∞?ùò Ï≤´Î≤àÏß? ?ù¥ÎØ∏Ï??
        self.index = 0
        self.image = images[self.index]

        # 1Ï¥àÏóê Î≥¥Ïó¨Ï§? 1?û•?ùò ?ù¥ÎØ∏Ï?? ?ãúÍ∞ÑÏùÑ Í≥ÑÏÇ∞, ?Üå?àò?†ê 3?ûêÎ¶¨ÍπåÏß? Î∞òÏò¨Î¶?
        self.animation_time = round(100 / len(self.images * 100), 2)

        # mt??? Í≤∞Ìï©?ïò?ó¨ animation_time?ùÑ Í≥ÑÏÇ∞?ï† ?ãúÍ∞? Ï¥àÍ∏∞?ôî
        self.current_time = 0

        # playerÍ∞? ???ÏßÅÏù¥?äî ?ôï?ù∏
        self.isMove = False

        # playerÍ∞? Ï°∞Ï??Ï§ëÏù∏Ïß? ?ôï?ù∏
        self.isAiming = False

        # player Ï≤¥Î†• Í¥?Î¶?
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

    # updateÎ•? ?Üµ?ï¥ Ï∫êÎ¶≠?Ñ∞?ùò ?ù¥ÎØ∏Ï??Í∞? Í≥ÑÏÜç Î∞òÎ≥µ?ï¥?Ñú ?Çò????Çò?èÑÎ°? ?ïú?ã§.
    def update(self, mt):
        #?Ç§Î≥¥ÎìúÎ°? player ?ù¥?èô
        self.keys = pygame.key.get_pressed()

        if not self.isAiming and not self.is_charging:
            # ?ôºÏ™ΩÏúºÎ°? ?ù¥?èôÍ∞??ä•
            if self.keys[pygame.K_a]:

                self.direction = "left"
                self.state = 1
                if self.rect.right > 160:
                    self.rect.x -= self.velocity_x
                    self.isMove = False
                else:
                    self.isMove = True
            # ?ò§Î•∏Ï™Ω?úºÎ°? ?ù¥?èôÍ∞??ä•
            if self.keys[pygame.K_d]:
                self.direction = "right"
                self.state = 1
                if self.rect.right < 1220:
                    self.rect.x += self.velocity_x
                    self.isMove = False
                else:
                    self.isMove = True
            # ?ïâÍ∏? Í∞??ä•
            if self.keys[pygame.K_s]:
                self.state = 2

        # ?òÑ?û¨ ?ÉÅ?Éú?óê ?î∞?ùº Î∞òÎ≥µ?ï¥Ï§? ?ù¥ÎØ∏Ï???ùò index ?Ñ§?†ïÍ≥? ?Üç?èÑ
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

        #sword Ï∂©Ï†Ñ
        elif self.state ==5:
            count = 1
            start_Index = 21
            self.velocity_x = 0
        #sword ?úò?ëêÎ•¥Í∏∞
        elif self.state == 6:
            count = 3
            start_Index = 22
            self.velocity_x = 0

        # Î∞©Ìñ•?ù¥ ?ò§Î•∏Ï™Ω?ù¥Î©?, ?ò§Î•∏Ï™Ω ?ù¥ÎØ∏Ï?? ?Ñ†?Éù
        if self.direction == 'right':
            self.images = self.images_right
        # Î∞©Ìñ•?ù¥ ?ôºÏ™ΩÏù¥Î©? ?ôºÏ™? ?ù¥ÎØ∏Ï?? ?Ñ†?Éù
        elif self.direction == 'left':
            self.images = self.images_left

        # loop ?ãúÍ∞? ?çî?ïòÍ∏?
        self.current_time += mt

        # loop time Í≤ΩÍ≥ºÍ∞? animation_time?ùÑ ?Ñò?ñ¥?ÑúÎ©? ?ÉàÎ°úÏö¥ ?ù¥ÎØ∏Ï?? Ï∂úÎ†•
        if self.current_time >= self.animation_time:
            self.current_time = 0

            # ?ÉÅ?Éú?óê ?î∞?ùº ?ù¥ÎØ∏Ï?? index Î≤îÏúÑÎ•? ?ã§Î•¥Í≤å ?Ñ§?†ï?ïú?ã§.
            self.index = (self.index % count) + start_Index

            self.image = self.images[self.index]
            self.index += 1

            if self.index >= len(self.images):
                self.index = 0

        if self.is_hit:  #is_hitÎ°? ?ÉÅ?Éú Í∞êÏ??. ?òÑ?û¨ True?ù∏ ?ÉÅ?ÉúÎ•? Í∞êÏ??.
            if pygame.time.get_ticks() - self.hit_timer > 500:  # 0.5Ï¥? ?èô?ïà ?ú†Ïß?
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

    # ------- ?ó¨Í∏∞Î???Ñ∞ part2?óê ?ì∞?ûÖ?ãà?ã§. ------- #
    def dash(self): # Î°úÏßÅ ?ôÑ?Ñ±, ?ï†?ãàÎ©îÏù¥?Öò ?Ñ£Í∏?
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
        self.accel_speed = 5 # Í∞??Üç?èÑ
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
