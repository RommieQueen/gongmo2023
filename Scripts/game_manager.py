import pygame

pygame.init()

def description(run, screen, color):
    pygame.display.init() 
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        screen.fill(color)
        pygame.display.update()
        
    pygame.quit()
    return run
