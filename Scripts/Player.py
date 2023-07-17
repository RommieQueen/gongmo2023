import pygame
pygame.init()
import import_image as images

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super(Player, self).__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.is_left = False
        self.is_right = False
        self.is_walk = False
        self.is_sit = False
        self.is_attack = False

        self.idle = images.player_idle
        self.idle_left = images.player_idle_left

        # 0~5 걷기 / 6~8 앉기 /9 어택 / 10 앉아어택
        self.right_list = []
        self.right_list.append(images.player_right1)
        self.right_list.append(images.player_right2)
        self.right_list.append(images.player_right3)
        self.right_list.append(images.player_right4)
        self.right_list.append(images.player_right5)
        self.right_list.append(images.player_right6)
        self.right_list.append(images.player_sit1)
        self.right_list.append(images.player_sit2)
        self.right_list.append(images.player_sit3)
        self.right_list.append(images.player_attak)
        self.right_list.append(images.player_attatk_sit)

        #왼쪽 걸음 애니메이션 반전, 인덱스 같음
        self.left_list = [pygame.transform.flip(image, True, False) for image in self.right_list]

        self.walk_index = 0  # 애니인덱스

        self.image = self.right_list[self.walk_index]
        self.player_rect = self.image.get_rect()
        self.player_rect.topleft = [pos_x,pos_y]

    def move(self, event):
        if event.key == pygame.K_d:
            self.is_right = True
            self.is_left = False
            self.is_walk = True

        elif event.key == pygame.K_a:
            self.is_left = True
            self.is_right = False
            self.is_walk = True

        elif event.key == pygame.K_s:
            self.is_sit = True
    def stop_move(self, event):
        self.image = self.idle
        if event.key == pygame.K_d or event.key == pygame.K_a:
            self.is_walk = False
        if event.key == pygame.K_s:
            self.is_sit = False

    def gun(self, event):
        if event.button == 1:
            self.is_attack = True
    def stop_gun(self, event):
        if event.button == 1:
            self.is_attack = False

    def update(self):
        speed = 5

        #왼, 오 누르고 있을 때 위치이동
        if self.is_walk:
            if self.is_left:
                self.pos_x -= speed
                self.walk_index += 1
                if self.walk_index >= 5:
                    self.walk_index = 0
                self.image = self.left_list[self.walk_index]

            elif self.is_right:
                self.pos_x += speed
                self.walk_index += 1
                if self.walk_index > 5:  # 걷기 애니메이션만
                    self.walk_index = 0
                self.image = self.right_list[self.walk_index]

        #앉기 애니
        elif self.is_sit:
            for i in range(6,9): #인덱스 6~8 : 앉기
                self.walk_index = i
            if self.walk_index == 8:
                self.walk_index = 8
            if self.is_left:
                self.image = self.left_list[self.walk_index]
            elif self.is_right:
                self.image = self.right_list[self.walk_index]

         # 총쏘기
        elif self.is_attack:
            self.walk_index = 9
            if self.walk_index == 9:
                self.walk_index = 9

            if self.is_left:
                self.image = self.left_list[self.walk_index]
            elif self.is_right:
                self.image = self.right_list[self.walk_index]

        if self.is_sit and self.is_attack: #외 elif 않되>?
            self.walk_index = 10
            if self.walk_index == 10:
                walk_index = 10
            if self.is_left:
                self.image = self.left_list[self.walk_index]
            elif self.is_right:
                self.image = self.right_list[self.walk_index]
    def draw(self, screen):

        screen.blit(self.image,(self.pos_x, 300))

