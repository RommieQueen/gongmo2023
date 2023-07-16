import pygame
import import_image as images
pygame.init()


def drawBackground(image, x, y, plusX, range_last):
    from main import screen
    for i in range(1,range_last):
        screen.blit(image, (x,y))
        x += plusX
def drawPlayer():
    from main import screen
    from Player import Player
    player = Player()

    x = player.position()

    screen.blit(images.player_idle, (x,200))
def stage1():

    from main import WIDTH_SCREEN, HEIGHT_SCREEN, screen, BLACK, WHITE, WIDTH_CENTER, HEIGHT_CENTER, FPS, running
    SKYBLUE = (178,235,244)
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(SKYBLUE)
        drawBackground(images.shadow_trees1,-200,190,400,6)
        drawBackground(images.shadow_trees2,0,230,400,5)
        drawBackground(images.stage1_ground,0,160,550,4)
        drawPlayer()
        pygame.display.update()
    pygame.quit()

