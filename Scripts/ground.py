import pygame
import sys
import time

screen_width, screen_height = 1280, 720


# 땅(Ground) 클래스 정의
class Ground(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.image_width = self.image.get_width()
        self.x_pos = 0

    def update(self, player_is_move, player_rect_x, player_speed):            
        if player_is_move == True:
            # player 위치가 화면 끝 근처인 경우, 원래 속도를 player 속도로 변경
            if player_rect_x <= 160:
                self.x_pos += player_speed
            elif player_rect_x >= 1220:
                self.x_pos -= player_speed

    def draw(self, screen):

        screen.blit(self.image, (self.x_pos, 0))

        screen.blit(self.image, (self.x_pos, 620))

        if self.x_pos >= 0:
            screen.blit(self.image, (self.x_pos - self.image_width, 0))
        elif self.x_pos <= 1280:
            screen.blit(self.image, (self.x_pos + self.image_width, 0))

        if self.x_pos >= 1280:
            self.x_pos = 0
        elif self.x_pos <= - 1280:
            self.x_pos = 0
