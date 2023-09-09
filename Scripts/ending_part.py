import pygame

pygame.init()

def ending_part():
    from main import WIDTH_SCREEN, HEIGHT_SCREEN, screen, BLACK, WHITE, WIDTH_CENTER, HEIGHT_CENTER, FPS, running
    import main as m
    import stage as s
    import game_manager as manager
    import import_image as images

    def intro_load(get_intro):
        intro = pygame.image.load(get_intro)
        screen.blit(intro, (0, 0))

    story = 0
    alpha = 0
    
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return running
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and alpha == 1000:
                    alpha = 0
                    story += 1
                    print(story)

        screen.fill(BLACK)

        alpha += 1.8

        if alpha > 255:
            alpha = 255
 
        if alpha == 255 and story == 0:
            intro_load('./../Images/ending/ending_1.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 1:
            alpha = 255
            intro_load('./../Images/ending/ending_2.jpg')
            # input_screen, x_pos, y_pos, input_image, image_width, image_height, action = None #
            manager.Button(screen, WIDTH_CENTER - 128, HEIGHT_CENTER + 170, images.start_button, 256, 134, m.main)
            alpha = 999        
        
        pygame.display.update()
    pygame.quit()
