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

part2_boss = pygame.image.load('./../Images/sprites/enemy/boss/part_2_boss.png')
part2_boss_hand = pygame.image.load('./../Images/sprites/enemy/boss/part_2_boss_hand.png')
long_branch = pygame.image.load('./../Images/sprites/enemy/boss/long_branch.png')
long_branch = pygame.transform.scale(long_branch, (630,630))
short_branch = pygame.image.load('./../Images/sprites/enemy/boss/short_branch.png')
short_branch = pygame.transform.scale(short_branch, (250,250))

# ui #
dialog_box = pygame.image.load('./../Images/ui/dialog_box.png')
mark_box = pygame.image.load('./../Images/ui/ImanorBalloon.png')
scope_normal = pygame.image.load('./../Images/ui/scope_normal.png')
scope_collide = pygame.image.load('./../Images/ui/scope_collide.png')
scope_normal = pygame.transform.scale(scope_normal,(50,50))
scope_collide = pygame.transform.scale(scope_collide,(50,50))
scope_point = pygame.transform.scale(scope_normal,(5,5))
heart_full = pygame.image.load('./../Images/ui/heart_full.png')
heart_full = pygame.transform.scale(heart_full,(50,50))
heart_bin = pygame.image.load('./../Images/ui/heart_bin.png')
heart_bin = pygame.transform.scale(heart_bin, (50,50))
Restart_normal = pygame.image.load('./../Images/ui/Restart_normal.png')
Restart_normal = pygame.transform.scale(Restart_normal,(250,150))
Restart_hover = pygame.image.load('./../Images/ui/Restart_hover.png')
Restart_hover = pygame.transform.scale(Restart_hover,(250,150))
sword_ui = pygame.image.load('./../Images/ui/sword.png')
sword_ui = pygame.transform.scale(sword_ui, (100,100))
gun_ui = pygame.image.load('./../Images/ui/gun.png')
gun_ui = pygame.transform.scale(gun_ui, (100,100))
sword_charging1 = pygame.image.load('./../Images/ui/sword1.png')
sword_charging2 = pygame.image.load('./../Images/ui/sword2.png')
sword_charging3 = pygame.image.load('./../Images/ui/sword3.png')
warning = pygame.image.load('./../Images/ui/warning_mark')
warning = pygame.transform.scale(warning, (400,400))

# 배경 #
intro1_background = pygame.image.load('./../Images/background/spaceship.jpg')
intro2_background = pygame.image.load('./../Images/background/intro2_1.png')
intro3_background = pygame.image.load('./../Images/background/meeting_room.jpg')

stage1_ground = pygame.image.load('./../Images/background/ground1.jpg')
stage2_ground = pygame.image.load('./../Images/background/stage2_ground.png')
stage2_ground = pygame.transform.scale(stage2_ground,(1280,720))

# 배경 요소 #
trees1 = pygame.image.load('./../Images/background/trees1.png')
trees1 = pygame.transform.scale(trees1, (400,400))
back_tree1 = pygame.image.load('./../Images/background/shadow_trees_background1.png')
back_tree1 = pygame.transform.scale(back_tree1, (1280,720))

shadow_trees1 = pygame.image.load('./../Images/background/shadow_trees1.png')
shadow_trees1 = pygame.transform.scale(shadow_trees1, (500,500))
shadow_trees2 = pygame.image.load('./../Images/background/shadow_trees2.png')
shadow_trees2 = pygame.transform.scale(shadow_trees2,(400,400))

shadow_tree_back1 = pygame.image.load('./../Images/background/shadow_trees_background1.png')
shadow_tree_back1 = pygame.transform.scale(shadow_tree_back1, (1280, 720))
shadow_tree_back2 = pygame.image.load('./../Images/background/shadow_trees_background2.png')
shadow_tree_back2 = pygame.transform.scale(shadow_tree_back2, (1280,720))
start_button = pygame.image.load('./../Images/ui/start_button.png')

# effect #
power1 = pygame.image.load('./../Images/sprites/power1.png')
power2 = pygame.image.load('./../Images/sprites/power2.png')
power3 = pygame.image.load('./../Images/sprites/power3.png')
