import pygame
from game_manager import description

pygame.init()

WIDTH_SCREEN = 1280
HEIGHT_SCREEN = 720
screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
pygame.display.set_caption("pygame")

WIDTH_CENTER = WIDTH_SCREEN // 2
HEIGHT_CENTER = HEIGHT_SCREEN // 2

# set_color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def menu():
    #변수선언
    background = pygame.image.load('Images/background/start_background.png')

    title_font = pygame.font.Font('Fonts/NeoDunggeunmoPro-Regular.ttf', 60)
    title_text = title_font.render("본격! 외계인 침공은 있던적이 없던거야!", True, BLACK)
    title_text_rect = title_text.get_rect(center=(WIDTH_CENTER, HEIGHT_CENTER - 200))

    button_font = pygame.font.Font('Fonts/NeoDunggeunmoPro-Regular.ttf', 40)

    start_text = button_font.render("시 작",True,WHITE)
    start_text_rect = start_text.get_rect(center = (WIDTH_CENTER, HEIGHT_CENTER))

    descrip_text = button_font.render("설 명",True,WHITE)
    descrip_text_rect = descrip_text.get_rect(center = (WIDTH_CENTER, (HEIGHT_CENTER + 110)))

    start_button = pygame.Rect((WIDTH_CENTER - 75), (HEIGHT_CENTER - 40), 150, 80)
    descrip_button = pygame.Rect((WIDTH_CENTER - 75), (HEIGHT_CENTER + 70), 150, 80)
    
    #실행
    run = True
    while run :                    
        screen.blit(background,(0, 0))
        screen.blit(title_text, title_text_rect)
        
        pygame.draw.rect(screen, BLUE, start_button, border_radius = 5)
        screen.blit(start_text, start_text_rect)
        
        pygame.draw.rect(screen, BLUE, descrip_button, border_radius = 5)
        screen.blit(descrip_text, descrip_text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_button.collidepoint(mouse_pos):
                    intro()
                elif descrip_button.collidepoint(mouse_pos):
                    run = description(run, screen, WHITE)                

        if run==True:
            pygame.display.update()
            
    pygame.quit()

def intro():
    
    alpha = 0
    timer = 0
    intro_img1 = pygame.image.load('Images/background/intro_park.png')
    intro_img2 = pygame.image.load('Images/background/intro_park2.png')
    intro_font = pygame.font.Font('Fonts/NeoDunggeunmoPro-Regular.ttf', 50)
    intro_text1 = intro_font.render("2023년 7월 3일", True, WHITE)
    intro_text2 = intro_font.render("공원에 오신것을 환영합니다.",True,WHITE)
    intro_text1_rect = intro_text1.get_rect(center=(WIDTH_CENTER, HEIGHT_CENTER-250))
    intro_text2_rect = intro_text2.get_rect(center=(WIDTH_CENTER, HEIGHT_CENTER-150))

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        screen.fill(BLACK)
        
        #불투명도 조절
        alpha+=1.5
        if alpha > 255:
            alpha = 255
            
        intro_img1.set_alpha(alpha)
        screen.blit(intro_img1, (0,0))
        
        if alpha == 255:
            screen.blit(intro_text1, intro_text1_rect)
            screen.blit(intro_text2, intro_text2_rect)
        timer+=1
        if timer >= 450:
            timer = 450
            screen.blit(intro_img2,(0,0))
            
        if run==True:    
            pygame.display.update()
    pygame.quit()
    return run

menu()