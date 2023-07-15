import sys
import pygame
from game_manager import button
from intro_part import intro

pygame.init()

FPS = pygame.time.Clock()

WIDTH_SCREEN = 1280
HEIGHT_SCREEN = 720
screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
pygame.display.set_caption("본격! 외계인 침공은 있던적이 없던거야!")

WIDTH_CENTER = WIDTH_SCREEN // 2
HEIGHT_CENTER = HEIGHT_SCREEN // 2

# set_color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

running = True

def main_window():

    start_background = pygame.image.load('./../Images/background/start_background.png')

    title_font = pygame.font.Font('./../Fonts/NeoDunggeunmoPro-Regular.ttf', 60)
    
    title_text = title_font.render("본격! 외계인 침공은 있던적이 없던거야!", True, BLACK)
    title_text_rect = title_text.get_rect(center = (WIDTH_CENTER, HEIGHT_CENTER - 200))
    
    start_text = title_font.render("*엔터를 빠르게 두번 누르면 시작합니다*", True, BLACK)
    start_text_rect = start_text.get_rect(center = (WIDTH_CENTER, HEIGHT_CENTER))

    global running
    
    while running:
        
        deltaTime = FPS.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = intro()
                     
        screen.blit(start_background, (0, 0))
        screen.blit(title_text, title_text_rect)
        screen.blit(start_text, start_text_rect)

        if running == True:
            pygame.display.update()
        else:
            pygame.quit()
            sys.exit()
        
    pygame.quit()
    
main_window()
