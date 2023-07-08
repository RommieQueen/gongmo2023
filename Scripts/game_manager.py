import pygame

pygame.init()

def description(run, screen, color):
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        screen.fill(color)
        pygame.display.update()
        
    pygame.quit()
