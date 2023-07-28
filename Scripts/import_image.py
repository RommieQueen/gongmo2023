import pygame
pygame.init()

# 초상화 portrait  #
alien_portrait = pygame.image.load('./../Images/sprites/enemy/alien_portrait.png')
boy_portrait = pygame.image.load('./../Images/sprites/boy_portrait.jpeg')

# 생김새 기본 #
player = pygame.image.load('./../Images/sprites/player/player_idle.png')
ailen = pygame.image.load('./../Images/sprites/enemy/alien_stand.png')
boy = pygame.image.load('./../Images/sprites/infected_human.png')
tree = pygame.image.load('./../Images/background/tree1.png')

# 적 #
alien_left1 = pygame.image.load('./../Images/sprites/enemy/alien_left1.png')
alien_left2 = pygame.image.load('./../Images/sprites/enemy/alien_left2.png')
alien_left3 = pygame.image.load('./../Images/sprites/enemy/alien_left3.png')

# ui #
dialog_box = pygame.image.load('./../Images/ui/dialog_box.png')
mark_box = pygame.image.load('./../Images/ui/ImanorBalloon.png')
scope_normal = pygame.image.load('./../Images/ui/scope_normal.png')
scope_collide = pygame.image.load('./../Images/ui/scope_collide.png')
scope_normal = pygame.transform.scale(scope_normal,(50,50))
scope_collide = pygame.transform.scale(scope_collide,(50,50))

# 배경 #
intro1_background = pygame.image.load('./../Images/background/spaceship.jpg')
intro2_background = pygame.image.load('./../Images/background/intro2_1.png')
intro3_background = pygame.image.load('./../Images/background/meeting_room.jpg')
stage1_ground = pygame.image.load('./../Images/background/ground1.png')
stage1_ground = pygame.transform.scale(stage1_ground, (600,600))
stage1_tile = pygame.image.load('./../Images/background/ground2.jpeg')
stage1_tile = pygame.transform.scale(stage1_tile, (128,128))

# 배경 요소 #
trees1 = pygame.image.load('./../Images/background/trees1.png')
trees1 = pygame.transform.scale(trees1, (400,400))

shadow_trees1 = pygame.image.load('./../Images/background/shadow_trees1.png')
shadow_trees1 = pygame.transform.scale(shadow_trees1, (500,500))
shadow_trees2 = pygame.image.load('./../Images/background/shadow_trees2.png')
shadow_trees2 = pygame.transform.scale  (shadow_trees2,(400,400))

start_button = pygame.image.load('./../Images/ui/start_button.png')
