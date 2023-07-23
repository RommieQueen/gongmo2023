import pygame
import import_image as images
import stage as stage
pygame.init()

def intro():
    # main 파일에서 변수, 상수, 메소드 불러오기
    from main import WIDTH_SCREEN, HEIGHT_SCREEN, screen, BLACK, WHITE, WIDTH_CENTER, HEIGHT_CENTER, FPS, running

    intro1_background = pygame.transform.scale(images.intro1_background, (1280,720))
    
    def dialog_box():
        pygame.draw.rect(screen, BLACK, [0, 620, 1280, 100])

    # 대화상자에서 줄을 바꿀 수 있음 1, 4번째 줄은 인물 대화용으로 사용하지 말 것.(1줄 이름, 4줄 시스템)
    def get_line_pos(text_name, get_line):
        if get_line == 1:
            text_pos = text_name.get_rect(center = (WIDTH_CENTER, HEIGHT_CENTER + 275))
        elif get_line == 2:
            text_pos = text_name.get_rect(center = (WIDTH_CENTER, HEIGHT_CENTER + 300))
        elif get_line == 3:
            text_pos = text_name.get_rect(center = (WIDTH_CENTER, HEIGHT_CENTER + 325))
        elif get_line == 4:
            text_pos = text_name.get_rect(center = (WIDTH_CENTER, HEIGHT_CENTER + 350))

        return text_pos

    #인물 이름 설정할 수 있음
    def character_name(get_text):
        character_name_font = pygame.font.Font('./../Fonts/NeoDunggeunmoPro-Regular.ttf', 20)
        character_name_line = character_name_font.render(get_text, True, WHITE)
        screen.blit(character_name_line, get_line_pos(character_name_line, 1))
        
    # 인물들의 말을 출력할 수 있도록 함
    # 대화상자에서 출력하고 싶은 라인, 원하는 색, 인물 대화 입력
    def character_text(get_line, get_color, get_text):        
        character_text_font = pygame.font.Font('./../Fonts/NeoDunggeunmoPro-Regular.ttf', 20)
        character_line = character_text_font.render(get_text, True, get_color)
        screen.blit(character_line, get_line_pos(character_line, get_line))

    # 대화상자에서 다음으로 넘기기를 알려줌
    def system_help():
        system_font = pygame.font.Font('./../Fonts/NeoDunggeunmoPro-Regular.ttf', 16)
        system_line_help = system_font.render("▼SPACE를 눌러 진행▼", True, WHITE)
        screen.blit(system_line_help, get_line_pos(system_line_help, 4))        

    def System():
        character_name("System")
        
    def Sarah():
        character_name("사라")

    def Alien_Leader():
        character_name("eca1b0eca285ec82ac20eb8c80ec9ea5")
        
    def Alien():
        character_name("eca1b0eca285ec82ac")
        
    alpha = 0
    story = 0

    background_pos = (0, 0)

    while running:
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return running
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and alpha == 255:
                    alpha = 0
                    story += 1
                    print(story)                                    
                
        alpha += 1.8

        if alpha > 255:
            alpha = 255
                    
        intro1_background.set_alpha(alpha)
        screen.blit(intro1_background, background_pos)
            
        if alpha == 255 and story == 0:
            dialog_box()
            System()
            character_text(2,WHITE,"(외계인들은 16진수로 대화하지만..)")
            character_text(3,WHITE,"(특별히 해석 해드리겠습니다.)")
            system_help()
                
        elif alpha >= 0 and story == 1:
            alpha = 255
            dialog_box()
            Alien()
            character_text(2, WHITE, "사령관님 우리 이제 또 어디가야 하나요?")
            character_text(3, WHITE, "이제 들릴 데는 다 간 것 같은데요...")
            system_help()
            
        elif alpha >= 0 and story == 2:
            alpha = 255
            dialog_box()
            Alien_Leader()
            character_text(2, WHITE, '대장님께서 무슨 계획인지 모르겠지만 [지구]라는 곳을 택하셨더군... 후훗')
            character_text(3, WHITE, "그러니 우리는 [지구]라는 곳에 간다...!!")
            system_help()
            
        elif alpha >= 0 and story == 3:
            alpha = 255
            dialog_box()
            Alien()
            character_text(2, WHITE, '넵! 그럼 바로 [지구]로 이동하겠습니다!')
            character_text(3, WHITE, "(저 씹덕같은 말은 좀 바꾸면 안 되나..?)")
            system_help()
            
        elif story == 4:            
            running = intro2()
            return running
            
        pygame.display.update()

def intro2():
    from main import WIDTH_SCREEN, HEIGHT_SCREEN, screen, BLACK, WHITE, WIDTH_CENTER, HEIGHT_CENTER, FPS, running

    ailen = pygame.transform.scale(images.ailen,(250, 250))
    dialog_box = pygame.transform.scale(images.dialog_box, (1100, 200))
    intro2_background = pygame.transform.scale(images.intro2_background, (1280, 720))
    mark_box = pygame.transform.scale(images.mark_box,(70, 70))
    boy = pygame.transform.scale(images.boy,(200, 200))
    tree = pygame.transform.scale(images.tree,(500, 500)) 
    
    def draw_dialog(portrait):    
        portrait = pygame.transform.scale(portrait, (140, 140))

        screen.blit(dialog_box,(WIDTH_CENTER - 550, 510))
        screen.blit(portrait, (120, 540))

    def get_line_pos(text_name, get_line):
        if get_line == 1:
            text_pos = text_name.get_rect(center = (WIDTH_CENTER, HEIGHT_CENTER + 190))
        elif get_line == 2:
            text_pos = text_name.get_rect(center = (WIDTH_CENTER, HEIGHT_CENTER + 215))
        elif get_line == 3:
            text_pos = text_name.get_rect(center = (WIDTH_CENTER, HEIGHT_CENTER + 240))
        elif get_line == 4:
            text_pos = text_name.get_rect(center = (WIDTH_CENTER, HEIGHT_CENTER + 265))
        elif get_line == 5:
            text_pos = text_name.get_rect(center = (WIDTH_CENTER, HEIGHT_CENTER + 290))
        elif get_line == 6:
            text_pos = text_name.get_rect(center = (WIDTH_CENTER, HEIGHT_CENTER + 315))

        return text_pos

    #인물 이름 설정할 수 있음
    def character_name(get_text):
        character_name_font = pygame.font.Font('./../Fonts/NeoDunggeunmoPro-Regular.ttf', 20)
        character_name_line = character_name_font.render(get_text, True, WHITE)
        screen.blit(character_name_line, get_line_pos(character_name_line, 1))
        
    # 인물들의 말을 출력할 수 있도록 함
    # 대화상자에서 출력하고 싶은 라인, 원하는 색, 인물 대화 입력
    def character_text(get_line, get_color, get_text):        
        character_text_font = pygame.font.Font('./../Fonts/NeoDunggeunmoPro-Regular.ttf', 20)
        character_line = character_text_font.render(get_text, True, get_color)
        screen.blit(character_line, get_line_pos(character_line, get_line))

    # 대화상자에서 다음으로 넘기기를 알려줌
    def system_help():
        system_font = pygame.font.Font('./../Fonts/NeoDunggeunmoPro-Regular.ttf', 16)
        system_line_help = system_font.render("▼SPACE를 눌러 진행▼", True, WHITE)
        screen.blit(system_line_help, get_line_pos(system_line_help, 6))

    #캐릭터 x,y 초기화 : 처음 그릴위치
    x_pos = 0
    y_pos = 0

    story = 0
    alpha = 0

    ailen_x = 700
    ailen_y = -180

    boy_x = -100
    boy_y = 300
    
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

        intro2_background.set_alpha(alpha)
        screen.blit(intro2_background, (0, 0))

        if alpha == 255:
            ailen_y += 3
            screen.blit(ailen, (ailen_x, ailen_y))
            
        if ailen_y > 230:
            ailen_y = 230

        if alpha >= 0 and story >= 1:
            alpha = 255
            boy_x += 3
            
            if story >= 5:
                screen.blit(tree, (boy_x - 100, boy_y - 250))
            else:
                screen.blit(boy, (boy_x, boy_y))
                
        if boy_x > 200:
            boy_x = 200

        if ailen_y == 230 and story == 0:
            draw_dialog(images.alien_portrait)
            character_name("eb8390ec98b9ec9db4")
            character_text(2, WHITE, "음... 여기가 지구 지면이구만... 흠...공기가 탁해서 적응하기는 쉽지 않겠는데...")                
            system_help()
            alpha = 1000

        if boy_x == 200 and story == 1:
            draw_dialog(images.boy_portrait)
            character_name("지나가던 행인")
            character_text(2, WHITE, "뭐야 뭔 고양이가 저렇게 크냐...? 호랑이인가?")
            system_help()
            alpha = 1000                
        elif alpha >= 0 and story == 2:
            alpha = 255
            draw_dialog(images.alien_portrait)
            character_name("eb8390ec98b9ec9db4")
            character_text(2, WHITE, "뭐야! 너 누구냐!")
            system_help()
            alpha = 1000
        elif alpha >= 0 and story == 3:
            alpha = 255
            draw_dialog(images.boy_portrait)
            character_name("지나가던 행인")
            character_text(2, WHITE, "뭐라는거지...? 저런 동물도 있었나? 생긴건 고양이처럼 생겼는데..?")
            system_help()
            alpha = 1000
        elif alpha >= 0 and story == 4:
            alpha = 255
            draw_dialog(images.alien_portrait)
            character_name("eb8390ec98b9ec9db4")
            character_text(2, WHITE, "멍청한 인간이군!! 너가 첫번째 희생자가 될 것이다!!")
            system_help()
            alpha = 1000
        elif alpha >= 0 and story == 5:
            alpha = 255
            draw_dialog(images.boy_portrait)
            character_name("지나가던 행인")
            character_text(2, WHITE, "으악~!!~!~")
            system_help()            
            alpha = 1000
        elif alpha >= 0 and story == 6:
            alpha = 255
            draw_dialog(images.alien_portrait)
            character_name("eb8390ec98b9ec9db4")
            character_text(2, WHITE, "그럼 이제 모든 인간을 없앤다!")
            system_help()
            alpha = 1000
        elif alpha >= 0 and story == 7:
            running = intro3()
            return running

        pygame.display.update()
    pygame.quit()

def intro3():
    from main import WIDTH_SCREEN, HEIGHT_SCREEN, screen, BLACK, WHITE, WIDTH_CENTER, HEIGHT_CENTER, FPS, running, main_window
    from game_manager import button


    intro3_background = pygame.transform.scale(images.intro3_background, (1280, 720))

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

        intro3_background.set_alpha(alpha)
        screen.blit(intro3_background, (0, 0))
 
        if alpha == 255 and story == 0:
            intro_load('./../Images/intro/intro3_1.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 1:
            alpha = 255
            intro_load('./../Images/intro/intro3_2.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 2:
            alpha = 255
            intro_load('./../Images/intro/intro3_3.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 3:
            alpha = 255
            intro_load('./../Images/intro/intro3_4.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 4:
            alpha = 255
            intro_load('./../Images/intro/intro3_5.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 5:
            alpha = 255
            intro_load('./../Images/intro/intro3_6.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 6:
            alpha = 255
            intro_load('./../Images/intro/intro3_7.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 7:
            alpha = 255
            intro_load('./../Images/intro/intro3_8.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 8:
            alpha = 255
            intro_load('./../Images/intro/intro3_9.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 9:
            alpha = 255
            intro_load('./../Images/intro/intro3_10.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 10:
            alpha = 255
            intro_load('./../Images/intro/intro3_11.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 11:
            alpha = 255
            intro_load('./../Images/intro/intro3_12.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 12:
            alpha = 255
            intro_load('./../Images/intro/intro3_13.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 13:
            alpha = 255
            intro_load('./../Images/intro/intro3_14.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 14:
            alpha = 255
            intro_load('./../Images/intro/intro3_15.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 15:
            alpha = 255
            intro_load('./../Images/intro/intro3_16.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 16:
            alpha = 255
            intro_load('./../Images/intro/intro3_17.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 17:
            alpha = 255
            intro_load('./../Images/intro/intro3_18.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 18:
            alpha = 255
            intro_load('./../Images/intro/intro3_19.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 19:
            alpha = 255
            intro_load('./../Images/intro/intro3_20.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 20:
            alpha = 255
            intro_load('./../Images/intro/intro3_21.jpg')
            alpha = 1000
        elif alpha >= 0 and story == 21:
            alpha = 255
            intro_load('./../Images/intro/intro3_22.jpg')
            # input_screen, x_pos, y_pos, input_image, image_width, image_height, action = None #
            button(screen, WIDTH_CENTER - 128, HEIGHT_CENTER + 170, images.start_button, 256, 134, stage.stage1)
            alpha = 999        
        
        pygame.display.update()
    pygame.quit()
            
