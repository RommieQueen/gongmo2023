import pygame
import sys
import random
import time
import math
import player as p
import enemy as e
import ground as g
import scope as s
import import_image as images
import game_manager as manager

# 스크린 전체 크기 지정

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# pygame 초기화
pygame.init()

# 스크린 객체 저장
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("player ex") 

SKY = (124,150,201)
BLACK = (0,0,0)

# FPS를 위한 Clock 생성
clock = pygame.time.Clock()

FPS = 60

# 충돌 확인 함수
def collision_entity(entity_1, entity_2):
    collisions = pygame.sprite.spritecollide(entity_1, entity_2, False, pygame.sprite.collide_mask)
    if collisions:
        return True
    return False

def main():
    
    ground = g.Ground('./../Images/background/ground1.jpg')

    # 적(Enemy) 그룹 생성
    enemy_group = pygame.sprite.Group()

    # player 생성
    player = p.Player(position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 280))

    # 생성된 player를 그룹에 넣기
    player_sprites = pygame.sprite.Group(player)

    # 다른 모듈 클래스 인스턴스s
    scope = s.Scope()
    enemy = e.Enemy()

    # scope_point 생성
    scope_point = s.ScopePoint(scope)


    running = True
    while running:

        # 땅 그리기
        ground.update(player.isMove, player.rect.right, player.velocity_x)
        ground.draw(SCREEN)
        
        player.heart(SCREEN)
        # 각 loop를 도는 시간. clock.tick()은 밀리초를 반환하므로
        # 1000을 나누어줘서 초단위로 변경한다.
        mt = clock.tick(60) / 1000

        # 마우스 좌표값
        mouse_x, mouse_y = pygame.mouse.get_pos()

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
                if event.button == 1:
                    enemy.hit()
                                 
            if event.type == pygame.KEYUP:
                if not(player.state == 3 or player.state == 4):
                    if event.key == pygame.K_d or event.key == pygame.K_a or event.key == pygame.K_s:
                        player.state = 0
                        player.velocity_x = 0     

        # 적 생성 및 업데이트         
        if len(enemy_group) < 10 and random.random() < 0.01:
            enemy = e.Enemy()
            enemy_group.add(enemy)
            
        enemy_group.update(player.isMove, player.rect.right, player.velocity_x)

        # player의 위치와 마우스 포인터의 위치 사이의 라디안 각도를 계산
        angle = math.atan2(mouse_y - 0, mouse_x - player.rect.x)

        # 라디안 값을 각도로 변환
        angle = math.degrees(angle)                

        # all_sprites 그룹안에 든 모든 Sprite update
        player_sprites.update(mt)

        # 적 그리기
        enemy_group.draw(SCREEN)
        
        # 모든 sprite 화면에 그려주기
        player_sprites.draw(SCREEN)

        # player가 조준중인지 확인
        if player.isAiming == True:
            scope_collision = collision_entity(scope_point, enemy_group)
            # 충돌확인
            if scope_collision:
                scope.collide_enemy()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                    pos = pygame.mouse.get_pos()
            else:
                scope.normal()
                enemy.is_collide_scope = False
            # scope, scopepoint를 마우스 좌표로 이동
            scope.draw(SCREEN, mouse_x, mouse_y)
            scope_point.draw_point(SCREEN)

            # player를 기준으로 마우스 포인터가 오른쪽에 있는지 왼쪽에 있는지를 확인
            if -90 <= angle <= 90:
                player.direction = "right"
            else:
                player.direction = "left"

        #플레이어가 적에 닿으면 체력-
        if collision_entity(player, enemy_group):
            player.hit()

        pygame.display.update()

    pygame.quit()

def part2():
    global now_stage
    now_stage = 2
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
    pygame.quit()

def player_die(): #죽으면 뜨는 함수
    from main import screen, WIDTH_CENTER, HEIGHT_CENTER
    #현재 스테이지 번수
    global now_stage
    now_stage = 1

    die_font = pygame.font.Font('./../Fonts/NeoDunggeunmoPro-Regular.ttf', 40)
    die_msg = die_font.render("일어나 Sarah!", True, (255,255,255))
    alpha = 255

    enemy = e.Enemy()
    enemy.now_kill = enemy.need_kill #이거되나?

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        SCREEN.fill(BLACK)

        time.sleep(0.5)

        #ui update
        screen.blit(die_msg, (WIDTH_CENTER-150,HEIGHT_CENTER-200))
        manager.Button(screen, WIDTH_CENTER - 160, HEIGHT_CENTER, images.Restart_normal, 250, 180, main)

        pygame.display.update()
    pygame.quit()
if __name__ == '__main__':
    main()
