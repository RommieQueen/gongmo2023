import pygame
import sys
import random
import time
import math
import player as p
import enemy as e
import ground as g
import scope as s
import boss as b
import import_image as images
import game_manager as manager
import part1_story as story
import ending_part as end

# 스크린 전체 크기 지정
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

WIDTH_CENTER = SCREEN_WIDTH // 2
HEIGHT_CENTER = SCREEN_HEIGHT // 2

# pygame 초기화
pygame.init()

# 스크린 객체 저장
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("본격! 외계인 침공은 있던적이 없던거야!") 

SKY = (124,150,201)
BLACK = (0,0,0)

# FPS를 위한 Clock 생성
clock = pygame.time.Clock()

FPS = 60

def scoreboard(screen, score):
    MAX_ENEMY = 100
    font = pygame.font.Font('./../Fonts/NeoDunggeunmoPro-Regular.ttf', 40)
    scoreboard_text = font.render(f"{score} / {MAX_ENEMY}", True, (255,255,255))
    screen.blit(scoreboard_text, (1090, 10))

def retry(now_stage): #죽으면 뜨는 함수
    pygame.mouse.set_visible(True)

    font = pygame.font.Font('./../Fonts/NeoDunggeunmoPro-Regular.ttf', 40)
    die_msg = font.render("일어나 Sarah!", True, (255,255,255))

    SCREEN.fill(BLACK)

    SCREEN.blit(die_msg, (WIDTH_CENTER - 150,HEIGHT_CENTER - 200))
    manager.Button(SCREEN, WIDTH_CENTER - 160, HEIGHT_CENTER, images.Restart_normal, 250, 180, now_stage)

def part1():
    
    ground = g.Ground(images.stage1_ground)

    # 적(Enemy) 그룹 생성
    enemy_group = pygame.sprite.Group()

    # player 생성
    player = p.Player(position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 280))

    # 생성된 player를 그룹에 넣기
    player_sprites = pygame.sprite.Group(player)

    # 다른 모듈 클래스 인스턴스
    scope = s.Scope()

    # scope_point 생성
    scope_point = s.ScopePoint(scope)

    #배경색
    SKYBLUE = (178, 235, 244)

    current_score = 0
    
    # Boss 생성
    boss = b.BossCat()
    boss_group = pygame.sprite.Group(boss)

    # Boss Attack 그룹 생성
    boss_attack_group = pygame.sprite.Group()

    running = True
    while running:

        # 땅
        SCREEN.fill(SKYBLUE)
        ground.update(player.isMove, player.rect.right, player.velocity_x)
        ground.draw(SCREEN)
        
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
                    
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and player.isAiming:
                    pos = pygame.mouse.get_pos()  #마우스 위치가 필요함
                    if enemy_collision:
                        #clicked_enemies에 enemy_group에 enemy를 enemy에 저장. 만약 마우스와 enemy가 닿았다면 밑에 코드 실행.
                        clicked_enemies = [enemy for enemy in enemy_group if enemy.rect.collidepoint(pos)]
                        #clicked_enemies 만큼 enemy에 hit 확인.
                        for enemy in clicked_enemies:
                            if not enemy.is_hit:
                                enemy.hit()
                                
                    if boss.is_awake:
                        if boss_collision:
                            clicked_boss = [boss for boss in boss_group if boss.rect.collidepoint(pos)]
                            for boss in clicked_boss:
                                if not boss.is_hit:
                                    boss.hit()

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    pygame.mouse.set_visible(True)
                    player.state = 0
                    player.isAiming = False
                                 
            if event.type == pygame.KEYUP:
                if not(player.state == 3 or player.state == 4):
                    if event.key == pygame.K_d or event.key == pygame.K_a or event.key == pygame.K_s:
                        player.state = 0
                        player.velocity_x = 0

        if e.current_die >= 5:
            for enemy in enemy_group:
                enemy.kill()
            boss.is_awake = True
            boss_group.update()
            boss_group.draw(SCREEN)
            boss.hp(SCREEN)

            # BossAttack 생성 및 업데이트         
            if len(boss_attack_group) < 15 and random.random() < 0.07:
                boss_attack = b.BossCatAttack()
                boss_attack_group.add(boss_attack)

            if boss.boss_health <= 0:
                boss.is_awake = False
                pygame.mouse.set_visible(True)
                story.part1_story()

            boss_attack_group.update()
            boss_attack_group.draw(SCREEN)
        else:

            #적 처치 관여 점수
            scoreboard(SCREEN, e.current_die)
            
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
        player.hp(SCREEN)

        # player가 조준중인지 확인
        if player.isAiming == True:
            enemy_collision = manager.collision_entity(scope_point, enemy_group)
            # 충돌확인
            if enemy_collision:
                scope.collide_enemy()
            else:
                scope.normal()

            if boss.is_awake:
                boss_collision = manager.collision_entity(scope_point, boss_group)
                # 충돌확인
                if boss_collision:
                    scope.collide_enemy()
                else:
                    scope.normal()
            
            # scope, scopepoint를 마우스 좌표로 이동
            scope.draw(SCREEN, mouse_x, mouse_y)
            scope_point.draw_point(SCREEN)

            # player를 기준으로 마우스 포인터가 오른쪽에 있는지 왼쪽에 있는지를 확인
            if -90 <= angle <= 90:
                player.direction = "right"
            else:
                player.direction = "left"

        #플레이어가 적에 닿으면 체력-
        if manager.collision_entity(player, enemy_group):
            if player.is_hit == False:
                player.hit()

        if manager.collision_entity(player, boss_attack_group):
            if player.is_hit == False:
                player.hit()

        if player.is_die == True:
            retry(part1)
            
        pygame.display.update()

    pygame.quit()

def part2():

    # 좌표, ui, 인스턴스 등 생성
    SKY = (225,128,72)
    player_y = SCREEN_HEIGHT - 340
    player = p.Player(position=(SCREEN_WIDTH // 2, player_y))
    scope_collide = False
    power_bar_pos = (SCREEN_WIDTH/2-images.power1.get_rect().right, 600)
    scope = s.Scope()
    scope_point = s.ScopePoint(scope)
    sword_group = pygame.sprite.Group()
    damage = 0

    # boss 요소 그룹이나 필요요소 선언
    boss = b.TreeBoss()
    boss.is_awake = True
    boss_group = pygame.sprite.Group(boss)

    long_branch_group = pygame.sprite.Group()
    short_branch_group = pygame.sprite.Group()

    is_attack = False
    attack_num = 0

    # 생성된 player를 그룹에 넣기
    player_sprites = pygame.sprite.Group(player)

    #main에 없는 sword 처리를 위해
    is_sword = False
    is_gun = True

    # 현재 스테이지 넘버
    global now_stage
    now_stage = 2

    running = True
    while running:

        # 땅 & 보스 & 플레이어 그리기
        SCREEN.fill(SKY)
        boss.update()
        boss_group.draw(SCREEN)
        SCREEN.blit(images.stage2_ground, (0,0))
        mt = clock.tick(60) / 1000
        player_sprites.draw(SCREEN)
        player_sprites.update(mt)
        player.hp(SCREEN)
        boss.hp(SCREEN)

        #좌표 가져오기
        mouse_x, mouse_y = pygame.mouse.get_pos()

        #sword or gun ui
        if is_gun:
            SCREEN.blit(images.gun_ui,(20,20))
        elif is_sword:
            SCREEN.blit(images.sword_ui, (20,20))

        # sword charging
        if player.is_charging:
            player.charging += 0.5
            if player.charging > 21:
                player.charging = 0

        if player.charging > 21 or player.charging == 0:
            player.power = 1
        elif player.charging > 14:
            player.power = 3
        elif player.charging > 7:
            player.power = 2
        elif player.charging > 0:
            player.power = 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            MOUSE_RIGHT = event.type == pygame.MOUSEBUTTONDOWN and event.button == 3
            MOUSE_LEFT = event.type == pygame.MOUSEBUTTONDOWN and event.button == 1

            # 대쉬, 무기변경
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.dash()
                if event.key == pygame.K_TAB:
                    if is_gun:
                        is_sword = True
                        is_gun = False
                    elif is_sword:
                        is_gun = True
                        is_sword = False

            # ** 무기는 우클릭 시 player.무기함수 호출 ** #
            # gun
            if is_gun:
                if MOUSE_RIGHT:
                    pygame.mouse.set_visible(False)
                    player.isAiming = True

                    if player.state == 2:
                        player.state = 4
                    else:
                        player.state = 3

                elif MOUSE_LEFT and scope_collide and player.isAiming:
                    if not boss.is_hit:
                        boss.hit(5)

            elif is_sword and not sword_group: # sword
                if MOUSE_RIGHT:
                    pygame.mouse.set_visible(False)
                    player.is_charging = True
                    player.sword_charging()

                if MOUSE_LEFT and player.is_charging:
                    player.is_charging = False
                    player.is_sword = False
                    player.charging = 0
                    player.sword_attack()
                    player.is_effect = True

            # 검 사용 이펙트
            if player.is_effect and not sword_group:
                sword_effect = p.SwordEffect(player.power, player)
                sword_group.add(sword_effect)
                player.is_effect_running = True

            # 마우스 떼서 무기 취소
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    pygame.mouse.set_visible(True)
                    if is_gun:
                        player.isAiming = False
                    if is_sword:
                        player.charging =0
                        player.is_charging = False
                    player.state = 0

            if event.type == pygame.KEYUP:
                if not (player.state == 3 or player.state == 4 or player.state == 5):
                    if event.key == pygame.K_d or event.key == pygame.K_a or event.key == pygame.K_s:
                        player.state = 0
                        player.velocity_x = 0

        # --!! Boss Attack !!----------------------------- #

        # player의 위치와 마우스 포인터의 위치 사이의 라디안 각도를 계산
        angle = math.atan2(mouse_y - 0, mouse_x - player.rect.x)

        # 라디안 값을 각도로 변환
        angle = math.degrees(angle)

        if player.isAiming:
            # player를 기준으로 마우스 포인터가 오른쪽에 있는지 왼쪽에 있는지를 확인
            if -90 <= angle <= 90:
                player.direction = "right"
            else:
                player.direction = "left"

        if not long_branch_group and not short_branch_group:
            attack_num = random.randint(0, 2)

        if attack_num == 1 and not long_branch_group: # long
            long_branch = b.Long_Branch()
            long_branch_group.add(long_branch)

        elif attack_num == 2 and not short_branch_group:  # short
            short_branch = b.Short_Branch()
            short_branch_group.add(short_branch)

        long_branch_group.update()
        long_branch_group.draw(SCREEN)
        short_branch_group.update()
        short_branch_group.draw(SCREEN)

        sword_group.update()
        sword_group.draw(SCREEN)

        if boss.boss_health <= 0:
                boss.is_awake = False
                pygame.mouse.set_visible(True)
                end.ending_part()

        # draw power_bar
        if player.is_charging:
            if player.power == 1:
                damage = 5
                SCREEN.blit(images.sword_charging1, power_bar_pos)
            if player.power == 2:
                damage = 12
                SCREEN.blit(images.sword_charging2, power_bar_pos)
            if player.power == 3:
                damage = 50
                SCREEN.blit(images.sword_charging3, power_bar_pos)

        # scope 그리기
        if player.isAiming and is_gun:
            scope.draw(SCREEN, mouse_x, mouse_y)
            scope_point.draw_point(SCREEN)

        # 플레이어 - 적 충돌 : - hp
        is_long_hit = manager.collision_entity(player, long_branch_group)
        is_short_hit = manager.collision_entity(player,short_branch_group)
        if is_short_hit or is_long_hit:
            player.hit()

        # 스코프 - 적 충돌
        scope_collide = manager.collision_entity(scope_point, long_branch_group)

        if scope_collide:
            scope.collide_enemy()
        else:
            scope.normal()

        # sword_effect - 적 충돌
        sword_collide = pygame.sprite.groupcollide(sword_group, long_branch_group, False, False)

        if sword_collide:
            boss.hit(damage)

        # 플레이어 사망
        if player.is_die == True:
            retry(part2)

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    part1()

