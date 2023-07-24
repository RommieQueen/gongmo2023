import pygame
import sys
import random
import time
import player as p
import enemy as e

# 스크린 전체 크기 지정

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# pygame 초기화
pygame.init()

# 스크린 객체 저장
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("player ex")

# FPS를 위한 Clock 생성
clock = pygame.time.Clock()

FPS = 60

CYAN = pygame.Color('cyan')

def main():

    # 적(Enemy) 그룹 생성
    enemy_group = pygame.sprite.Group()

    # player 생성
    player = p.Player(position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 280))
    
    # 생성된 player를 그룹에 넣기
    player_sprites = pygame.sprite.Group(player)
    
    running = True
    while running:

        print(player.isMove)
        # 각 loop를 도는 시간. clock.tick()은 밀리초를 반환하므로
        # 1000을 나누어줘서 초단위로 변경한다.
        mt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                player.isAiming = True
                pygame.mouse.set_visible(False)
                if player.state == 2:
                    player.state = 4
                else:
                    player.state = 3

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    pygame.mouse.set_visible(True)
                    player.state = 0
                    player.isAiming = False
                                 
            if event.type == pygame.KEYUP:
                if not(player.state == 3 or player.state == 4):
                    if event.key == pygame.K_d or event.key == pygame.K_a or event.key == pygame.K_s:
                        player.velocity_x = 0
                        player.state = 0

        # 적 생성 및 업데이트         
        if len(enemy_group) < 10 and random.random() < 0.01:
            enemy = e.Enemy()
            enemy_group.add(enemy)
            
        enemy_group.update(player.isMove, player.rect.right, player.velocity_x)

        # all_sprites 그룹안에 든 모든 Sprite update
        player_sprites.update(mt)
        # 배경색
        SCREEN.fill(CYAN)

        # 적 그리기
        enemy_group.draw(SCREEN)
        
        # 모든 sprite 화면에 그려주기
        player_sprites.draw(SCREEN)
        pygame.display.update()

    pygame.quit()
 
if __name__ == '__main__':
    main()
