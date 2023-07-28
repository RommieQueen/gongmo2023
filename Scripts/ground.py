import pygame
import sys
import time

screen_width, screen_height = 1280, 720


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
                self.x_pos += 128
            elif player_rect_x >= 1220:
                self.x_pos -= 128

    def draw(self, screen): #d
        for x in range(0, 1281, 128): #for문의 x를 x좌표로 그냥 사용해버림 0~1280 128씩 증가 (이미지가 128*128)
            screen.blit(self.image, (x, 620))
        if self.x_pos >= 0:
            screen.blit(self.image, (self.x_pos - self.image_width, 620))
        elif self.x_pos <= 1280:
            screen.blit(self.image, (self.x_pos + self.image_width, 620))

        if self.x_pos >= 1280:
            self.x_pos = 0
        elif self.x_pos <= - 1280:
            self.x_pos = 0

    #나무, 풀 같은 배경 뒷요소를 그림. 위 update, draw 역할 모두포함
    #!!!!!!!!! 플레이어 움직임 움직이기 구현하기!!!!!!!!!!!!!!
    def draw_thing(self, screen, player_is_move, player_rect_x, img, x, y, plus_x):
        for x in range(x,1281, plus_x):
            screen.blit(img, (x,y))
        if player_is_move == True:
            # player 위치가 화면 끝 근처인 경우, 원래 속도(0)를 player 속도로 변경
            if player_rect_x <= 160:
                self.x_pos += plus_x
            elif player_rect_x >= 1220:
                self.x_pos -= plus_x
