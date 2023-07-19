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

# 플레이어 #
player_idle = pygame.image.load('./../Images/sprites/player/player_idle.png')
player_idle_left = pygame.transform.flip(player_idle,True,False)

player_right1 = pygame.image.load('./../Images/sprites/player/player_walk_1.png')
player_right2 = pygame.image.load('./../Images/sprites/player/player_walk_2.png')
player_right3 = pygame.image.load('./../Images/sprites/player/player_walk_3.png')
player_right4 = pygame.image.load('./../Images/sprites/player/player_walk_4.png')
player_right5 = pygame.image.load('./../Images/sprites/player/player_walk_5.png')
player_right6 = pygame.image.load('./../Images/sprites/player/player_walk_6.png')

player_sit1 = pygame.image.load('./../Images/sprites/player/player_sit_1.png')
player_sit2 = pygame.image.load('./../Images/sprites/player/player_sit_2.png')
player_sit3 = pygame.image.load('./../Images/sprites/player/player_sit_3.png')

player_attak = pygame.image.load('./../Images/sprites/player/player_stand_attack.png')
player_attatk_sit = pygame.image.load('./../Images/sprites/player/player_sit_attack.png')

player_sit_attak = pygame.image.load('./../Images/sprites/player/player_sit_attack.png')
player_stand_attak = pygame.image.load('./../Images/sprites/player/player_stand_attack.png')

# 적 #
enemy_right1 = pygame.image.load('./../Images/sprites/enemy/alien_left1.png')
enemy_right2 = pygame.image.load('./../Images/sprites/enemy/alien_left2.png')
enemy_right3 = pygame.image.load('./../Images/sprites/enemy/alien_left3.png')

# ui #
dialog_box = pygame.image.load('./../Images/ui/dialog_box.png')
mark_box = pygame.image.load('./../Images/ui/ImanorBalloon.png')
scope_normal = pygame.image.load('./../Images/ui/scope_normal.png')
scope_collide = pygame.image.load('./../Images/ui/scope_collide.png')
scope_normal = pygame.transform.scale(scope_normal,(50,50))
scope_collide = pygame.transform.scale(scope_collide,(50,50))

# 배경 #
spaceship_background = pygame.image.load('./../Images/background/spaceship.jpg')
intro2_background = pygame.image.load('./../Images/background/intro2_1.png')
stage1_ground = pygame.image.load('./../Images/background/ground1.png')
stage1_ground = pygame.transform.scale(stage1_ground, (600,600))
# 배경 요소 #
trees1 = pygame.image.load('./../Images/background/trees1.png')
trees1 = pygame.transform.scale(trees1, (400,400))

shadow_trees1 = pygame.image.load('./../Images/background/shadow_trees1.png')
shadow_trees1 = pygame.transform.scale(shadow_trees1, (500,500))
shadow_trees2 = pygame.image.load('./../Images/background/shadow_trees2.png')
shadow_trees2 = pygame.transform.scale  (shadow_trees2,(400,400))
