import pygame
from game_manager import button
from intro_1 import intro

pygame.init()

FPS = pygame.time.Clock()

WIDTH_SCREEN = 1280
HEIGHT_SCREEN = 720
screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN), pygame.FULLSCREEN)
pygame.display.set_caption("본격! 외계인 침공은 있던적이 없던거야!")

WIDTH_CENTER = WIDTH_SCREEN // 2
HEIGHT_CENTER = HEIGHT_SCREEN // 2

# set_color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def main_window():

    start_background = pygame.image.load('./Images/background/start_background.png')
    start_background = pygame.transform.scale(start_background, (1280, 720))

    title_font = pygame.font.Font('./Fonts/NeoDunggeunmoPro-Regular.ttf', 60)
    title_text = title_font.render("본격! 외계인 침공은 있던적이 없던거야!", True, BLACK)
    title_text_rect = title_text.get_rect(center = (WIDTH_CENTER, HEIGHT_CENTER - 200))

    start_button = pygame.image.load('./Images/start_button.png')
    
    running = True

    while running:
        
        deltaTime = FPS.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(start_background,(0, 0))
        screen.blit(title_text, title_text_rect)
        button(screen, WIDTH_CENTER - 128, HEIGHT_CENTER - 67, start_button, 256, 134, intro)

        pygame.display.update()
        
    pygame.quit()

main_window()
