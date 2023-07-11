import pygame

pygame.init()


def intro():
    
    from main import WIDTH_SCREEN, HEIGHT_SCREEN, screen, BLACK, WHITE, WIDTH_CENTER, HEIGHT_CENTER, FPS

    def text_pos(text_name, get_height):
        text_pos = text_name.get_rect(center = (WIDTH_CENTER, HEIGHT_CENTER + get_height))
        return text_pos

    alpha = 0
    story = 0

    background_pos = (0, 0)

    screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN + 100))

    spaceship_background = pygame.image.load('./../Images/background/spaceship.jpg')
    spaceship_background = pygame.transform.scale(spaceship_background, (1280, 720))

    text_font = pygame.font.Font('./../Fonts/NeoDunggeunmoPro-Regular.ttf', 20)

    system_line_1 = text_font.render("ㄴ미ㅓㅣㅇ루다닝린욷지ㅓㄹ아ㅣㅓㄴㅇ린ㄴㅇ리", True, WHITE)
    system_line_2 = text_font.render("머두ㅏ나우라너아ㅟㅏㄴ어라가이낭뤼다낭무가나", True, WHITE)
    system_line_3 = text_font.render("...패치 완료...", True, WHITE)
    

    running = True

    while running:

        deltaTime = FPS.tick(60)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and alpha == 255:
                    alpha = 0
                    story += 1
                    print(story)

        screen.fill(BLACK)
            
        if story == 0:
                
            alpha += 1.5
                
            if alpha > 255:
                alpha = 255
                    
            spaceship_background.set_alpha(alpha)
            screen.blit(spaceship_background, background_pos)
            
            if alpha == 255:
                screen.blit(system_line_1, text_pos(system_line_1, 380))
                
        pygame.display.update()
        
    pygame.quit()
