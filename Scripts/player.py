import pygame
import stage as s
import enemy as e
import time
import import_image as imgs
pygame.init()

enemy = e.Enemy()

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super(Player, self).__init__()

        # 이미지를 Rect안에 넣기 위해 Rect의 크기 지정
        # 이미지의 크기와 같게 하거나, 크기를 다르게 한다면 pygame.transform.scale을 사용하여 rect 안에
        # 이미지를 맞추도록 한다.
        size = (92, 184) 

        # 여러장의 이미지를 리스트로 저장한다. 이미지 경로는 자신들의 경로를 사용한다.
        images = []

        # 서있는 상태 0 ~ 6
        images.append(pygame.image.load('./../Images/sprites/player/player_idle.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_idle.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_idle.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_idle.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_idle.png'))
        images.append(pygame.image.load('./../Images/sprites/player/player_idle.png'))

        # 걷기 7 ~ 13
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

        # 앉는 상태 14 ~ 15
        images.append(pygame.image.load('./../Images/sprites/player/player_sit.png'))

        # 서서 공격하는 상태 16 ~ 17
        images.append(pygame.image.load('./../Images/sprites/player/player_stand_attack.png'))

        # 앉아서 공격하는 상태 17 ~ 18
        images.append(pygame.image.load('./../Images/sprites/player/player_sit_attack.png'))

        # Rect 크기와 Image 크기 맞추기. pygame.transform.scale
        self.images = [pygame.transform.scale(image, size) for image in images]

        # rect 만들기
        self.rect = pygame.Rect(position, size)

        # masks 만들기
        self.masks = [pygame.mask.from_surface(image) for image in self.images]

        # 원본 캐릭터 이미지들
        self.images_right = images
        
        # 캐릭터 이미지가 오른쪽을 보고 있는데, 왼쪽으로 보도록 하기 위해서는
        # 이미지를 세로 기준으로 좌우로 뒤집이 준다. pygame.transform.flip 메서드 사용
        self.images_left = [pygame.transform.flip(image, True, False) for image in images]

        # 캐릭터의 현재 상태
        # 0 - idle 상태, 1 - 걷고 있는 상태
        self.state = 0
        
        # 방향
        self.direction = 'right'
        
        # 속도
        self.velocity_x = 0

        # 캐릭터의 첫번째 이미지
        self.index = 0
        self.image = images[self.index]

        # 1초에 보여줄 1장의 이미지 시간을 계산, 소수점 3자리까지 반올림
        self.animation_time = round(100 / len(self.images * 100), 2)

        # mt와 결합하여 animation_time을 계산할 시간 초기화
        self.current_time = 0

        # player가 움직이는 확인
        self.isMove = False

        # player가 조준중인지 확인
        self.isAiming = False

        #플레이어 체력
        self.health = 3

        #적과 닿았는지
        self.is_hitable = True

        self.time = 0

        #heart
        self.heart1_img = imgs.heart_full
        self.heart2_img = imgs.heart_full
        self.heart3_img = imgs.heart_full

        self.pos1 = (10,10)
        self.pos2 = (80,10)
        self.pos3 = (150,10)

        #die

    # update를 통해 캐릭터의 이미지가 계속 반복해서 나타나도록 한다.
    def update(self, mt):

        #키보드로 player 이동
        keys = pygame.key.get_pressed()
        if self.isAiming == False:
            # 왼쪽으로 이동가능
            if keys[pygame.K_a]:
                self.direction = "left"
                self.state = 1
                if self.rect.right > 160:
                    self.rect.x -= self.velocity_x
                    self.isMove = False
                else:
                    self.isMove = True
            # 오른쪽으로 이동가능
            if keys[pygame.K_d]:
                self.direction = "right"
                self.state = 1
                if self.rect.right < 1220:
                    self.rect.x += self.velocity_x
                    self.isMove = False
                else:
                    self.isMove = True
            # 앉기 가능
            if keys[pygame.K_s]:
                self.state = 2
        
        # 현재 상태에 따라 반복해줄 이미지의 index 설정과 속도
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

        # 방향이 오른쪽이면, 오른쪽 이미지 선택
        if self.direction == 'right':
            self.images = self.images_right
        # 방향이 왼쪽이면 왼쪽 이미지 선택
        elif self.direction == 'left':
            self.images = self.images_left

        # loop 시간 더하기
        self.current_time += mt

        # loop time 경과가 animation_time을 넘어서면 새로운 이미지 출력 
        if self.current_time >= self.animation_time:
            self.current_time = 0

            # 상태에 따라 이미지 index 범위를 다르게 설정한다.

            # idle 상태는 0 ~ 6, 걷기 상태는 7 ~ 13
            self.index = (self.index % count) + start_Index

            self.image = self.images[self.index]
            self.index += 1

            if self.index >= len(self.images):
                self.index = 0
                
    def hit(self):
        if self.is_hitable:
            self.health -= 1
            self.is_hitable = False

        self.time += 1
        if self.time > 50:
            self.time = 0
            self.is_hitable = True
        print(self.health)

    def heart(self,screen): #죽을때 나머지 하트 안바뀜 ㅜ
        
        if self.health <= 2:
            self.heart3_img = imgs.heart_bin
        if self.health <=1:
            self.heart2_img = imgs.heart_bin
        if self.health <=0:
            self.heart1_img = imgs.heart_bin
            time.sleep(1)
            s.player_die()

        screen.blit(self.heart1_img, self.pos1)
        screen.blit(self.heart2_img, self.pos2)
        screen.blit(self.heart3_img, self.pos3)


