import pygame
import random
import import_image as images
import Enemy as e

pygame.init()

from Player import Player

def drawBackground(image, x, y, plusX, range_last):
    from main import screen
    for i in range(1,range_last):
        screen.blit(image, (x,y))
        x += plusX

player = Player(50, 200)

def stage1():

    from main import WIDTH_SCREEN, HEIGHT_SCREEN, screen, BLACK, WHITE, WIDTH_CENTER, HEIGHT_CENTER, FPS, running
    
    SKYBLUE = (178,235,244)
    
    
    
    running = True
    while running:
        screen.fill(SKYBLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                player.move(event)
            if event.type == pygame.KEYUP:
                player.stop_move(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.gun(event)
            if event.type == pygame.MOUSEBUTTONUP:
                player.stop_gun(event)
        drawBackground(images.shadow_trees1, -200, 190, 400, 6)
        drawBackground(images.shadow_trees2, 0, 230, 400, 5)
        drawBackground(images.stage1_ground, 0, 160, 550, 4)

        player.update()
        player.draw(screen)
        
        if random.randint(1, 400) < 5:
            enemy = e.Enemy()
            e.enemies.add(enemy)

        e.enemies.update()
        e.enemies.draw(screen)

        pygame.display.update()
        
    pygame.quit()

