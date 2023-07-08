import pygame

pygame.init()

WIDTH_SCREEN = 1280;
HEIGHT_SCREEN = 720;

#set_color#
BLACK = (255,255,255)
WHITE = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
START_BLUE = (74,191,211)

screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
pygame.display.set_caption("pygame")

title_font = pygame.font.Font('Fonts/NeoDunggeunmoPro-Regular.ttf', 60)
title_text = title_font.render("-본격! 외계인 침공은 있던적이 없던거야-", True, BLACK)
title_text_rect = title_text.get_rect(center=(WIDTH_SCREEN // 2, HEIGHT_SCREEN // 2 - 200))

start_font = pygame.font.Font('Fonts/NeoDunggeunmoPro-Regular.ttf', 40)
start_text = start_font.render("Start",True,START_BLUE)
start_text_rect = start_text.get_rect(center=(WIDTH_SCREEN // 2, HEIGHT_SCREEN // 2))

run = True
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_text_rect.collidepoint(mouse_pos):
                intro()
    
    screen.fill(WHITE)
    screen.blit(title_text, title_text_rect)
    screen.blit(start_text, start_text_rect)
    
    def intro():
        print("게임시작")
        
    pygame.display.update()
pygame.quit()
