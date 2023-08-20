import pygame

pygame.init()

def part1_story():
    from main import WIDTH_SCREEN, HEIGHT_SCREEN, screen, BLACK, WHITE, WIDTH_CENTER, HEIGHT_CENTER, FPS, running
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
            intro_load('./../Images/part1_story/part1_1.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 1:
            alpha = 255
            intro_load('./../Images/part1_story/part1_2.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 2:
            alpha = 255
            intro_load('./../Images/part1_story/part1_3.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 3:
            alpha = 255
            intro_load('./../Images/part1_story/part1_4.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 4:
            alpha = 255
            intro_load('./../Images/part1_story/part1_5.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 5:
            alpha = 255
            intro_load('./../Images/part1_story/part1_6.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 6:
            alpha = 255
            intro_load('./../Images/part1_story/part1_7.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 7:
            alpha = 255
            intro_load('./../Images/part1_story/part1_8.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 8:
            alpha = 255
            intro_load('./../Images/part1_story/part1_9.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 9:
            alpha = 255
            intro_load('./../Images/part1_story/part1_10.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 10:
            alpha = 255
            intro_load('./../Images/part1_story/part1_11.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 11:
            alpha = 255
            intro_load('./../Images/part1_story/part1_12.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 12:
            alpha = 255
            intro_load('./../Images/part1_story/part1_13.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 13:
            alpha = 255
            intro_load('./../Images/part1_story/part1_14.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 14:
            alpha = 255
            intro_load('./../Images/part1_story/part1_15.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 15:
            alpha = 255
            intro_load('./../Images/part1_story/part1_16.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 16:
            alpha = 255
            intro_load('./../Images/part1_story/part1_17.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 17:
            alpha = 255
            intro_load('./../Images/part1_story/part1_18.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 18:
            alpha = 255
            intro_load('./../Images/part1_story/part1_19.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 19:
            alpha = 255
            intro_load('./../Images/part1_story/part1_20.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 20:
            alpha = 255
            intro_load('./../Images/part1_story/part1_21.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 21:
            alpha = 255
            intro_load('./../Images/part1_story/part1_22.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 22:
            alpha = 255
            intro_load('./../Images/part1_story/part1_23.jpg')
            # input_screen, x_pos, y_pos, input_image, image_width, image_height, action = None #
            manager.Button(screen, WIDTH_CENTER - 128, HEIGHT_CENTER + 170, images.start_button, 256, 134, s.part2)
            alpha = 999        
        
        pygame.display.update()
    pygame.quit()
