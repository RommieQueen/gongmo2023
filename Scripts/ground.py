import pygame
import sys
import time

screen_width, screen_height = 1280, 720

SKY = (124,150,201)
# 땅(Ground) 클래스 정의
class Ground(pygame.sprite.Sprite):
    def __init__(self, ground_image_path):
        super().__init__()
        self.image = ground_image_path
        self.image_width = self.image.get_width()
        self.x_pos = 0

        #draw
        self.is_ground = True

    def update(self, player_is_move, player_rect_x, player_speed):            
        if player_is_move == True:
            # player 위치가 화면 끝 근처인 경우, 원래 속도(0)를 player 속도로 변경
            if player_rect_x <= 160:
                self.x_pos += player_speed
            elif player_rect_x >= 1220:
                self.x_pos -= player_speed

    def draw(self, screen, plus_x):
        screen.fill(SKY)

        for x in range (0, 1281, 128): #for문의 x를 x좌표로 그냥 사용해버림 0~1280 128씩 증가 (이미지가 128*128)
            screen.blit(self.image, (x, 620))
        if self.x_pos >= 0:
            screen.blit(self.image, (self.x_pos - self.image_width, 620))
        elif self.x_pos <= 1280:
            screen.blit(self.image, (self.x_pos + self.image_width, 620))

        if self.x_pos >= 1280:
            self.x_pos = 0
        elif self.x_pos <= - 1280:
            self.x_pos = 0

    def draw_tree(self, screen, img, x,y, plus_x):
        for i in range(1,10):
            screen.blit(img, (x,y))
            x += plus_x
