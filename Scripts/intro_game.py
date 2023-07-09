import pygame

pygame.init()

def intro():
    
    from main import screen, BLACK, WIDTH_CENTER, HEIGHT_CENTER, FPS

    alpha = 0
    story = 0

    background_pos = (0, 0)
            
    dialog = pygame.image.load('./../Images/dialog.png')
        
    intro_img_1 = pygame.image.load('./../Images/intro_park.png')
    intro_img_2 = pygame.image.load('./../Images/intro_park2.png')
        
    intro_font = pygame.font.Font('./../Fonts/NeoDunggeunmoPro-Regular.ttf', 50)
    sys_font = pygame.font.Font('./../Fonts/NeoDunggeunmoPro-Regular.ttf', 15)

    system_text = sys_font.render("▼SPACE를 눌러 진행▼", True, BLACK)
    system_text_pos = system_text.get_rect(center=(WIDTH_CENTER, HEIGHT_CENTER + 320))
    
    hero_name = intro_font.render("나", True, BLACK)
    hero_name_pos = hero_name.get_rect(center = (WIDTH_CENTER - 440, HEIGHT_CENTER + 20))
    
    hero_text_1 = intro_font.render("오늘은 오랜만에 남자친구를 만나기 위해서 공원을 왔다", True, BLACK)
        
    hero_text_2 = intro_font.render("이 공원... 굉장히 오랜만에 오는 것 같다...", True, BLACK)
    hero_text_3 = intro_font.render("예전에는 많이 와서 산책도 했는데 요즘은 쓰레기를", True, BLACK)
    hero_text_4 = intro_font.render("버리는 사람들이 늘면서 호수가 많이 더러워 진 것 같다", True, BLACK)

    hero_text_5 = intro_font.render("30분이 지났는데 안 오고 있다... 무슨 일이 있는걸까?", True, BLACK)

    hero_text_6 = intro_font.render("얼마나 기다렸을까... 갑자기 짜증이 몰려오기 시작했다", True, BLACK)
    hero_text_7 = intro_font.render("얼마나 더 기다려야 할까...", True, BLACK)
    hero_text_8 = intro_font.render("방금 무슨 소리지?!", True, BLACK)
    

    alien_image = pygame.image.load('./../Images/alien.png')
    alien_image_pos = alien_image.get_rect(center=(WIDTH_CENTER + 450, HEIGHT_CENTER - 85))
    
    alien_name = intro_font.render("???", True, BLACK)
    alien_name_pos = alien_name.get_rect(center = (WIDTH_CENTER - 440, HEIGHT_CENTER + 20))

    alien_text_1 = intro_font.render("&$*%&$%*%$%&*#$@*#&#@*%&*%*$&*#$#*$&#*$&*#$&*", True, BLACK)
    
    
    character_text_pos_top = (15, 420)
    character_text_pos_middle = (15, 480)
    character_text_pos_bottom = (15, 540)
        
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
                    
            intro_img_1.set_alpha(alpha)
            screen.blit(intro_img_1, background_pos)
            
            if alpha == 255:
                screen.blit(dialog, background_pos)
                screen.blit(hero_text_1, character_text_pos_top)
                screen.blit(hero_name, hero_name_pos)
                screen.blit(system_text, system_text_pos)

        elif story == 1:
            
            alpha += 1.5
                
            if alpha > 255:
                alpha = 255
                    
            intro_img_2.set_alpha(alpha)
            screen.blit(intro_img_2, background_pos)
            
            if alpha == 255:
                screen.blit(dialog, background_pos)
                screen.blit(hero_text_2, character_text_pos_top)
                screen.blit(hero_text_3, character_text_pos_middle)
                screen.blit(hero_text_4, character_text_pos_bottom)
                screen.blit(hero_name, hero_name_pos)
                screen.blit(system_text, system_text_pos)
                    
        elif story == 2:
            
            alpha += 1.5
                
            if alpha > 255:
                alpha = 255
                    
            intro_img_2.set_alpha(alpha)
            screen.blit(intro_img_2, background_pos)
            
            if alpha == 255:
                screen.blit(dialog, background_pos)
                screen.blit(hero_text_5, character_text_pos_top)
                screen.blit(hero_name, hero_name_pos)
                screen.blit(system_text, system_text_pos)

        elif story == 3:
            
            alpha += 1.5
                
            if alpha > 255:
                alpha = 255
                    
            intro_img_2.set_alpha(alpha)
            screen.blit(intro_img_2, background_pos)
            
            if alpha == 255:
                screen.blit(dialog, background_pos)
                screen.blit(hero_text_6, character_text_pos_top)
                screen.blit(hero_text_7, character_text_pos_middle)
                screen.blit(hero_name, hero_name_pos)
                screen.blit(system_text, system_text_pos)

        elif story == 4:
            
            alpha += 1.5
                
            if alpha > 255:
                alpha = 255
                    
            intro_img_2.set_alpha(alpha)
            screen.blit(intro_img_2, background_pos)
            
            if alpha == 255:
                screen.blit(dialog, background_pos)
                screen.blit(alien_text_1, character_text_pos_top)
                screen.blit(alien_name, alien_name_pos)
                screen.blit(system_text, system_text_pos)
                
        elif story == 5:
            alpha = 255
            screen.blit(intro_img_2, background_pos)
            
            screen.blit(dialog, background_pos)
            screen.blit(hero_text_8, character_text_pos_top)
            screen.blit(hero_name, hero_name_pos)
            screen.blit(system_text, system_text_pos)

        elif story == 6:
            alpha = 255
            screen.blit(intro_img_2, background_pos)

            screen.blit(alien_image, alien_image_pos)
            screen.blit(dialog, background_pos)
            screen.blit(alien_text_1, character_text_pos_top)
            screen.blit(alien_name, alien_name_pos)
            screen.blit(system_text, system_text_pos)
                
        
                
        pygame.display.update()
                    
    pygame.quit()

