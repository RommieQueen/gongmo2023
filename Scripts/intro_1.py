import pygame
import import_image as images

pygame.init()

player = pygame.transform.scale(images.player,(256,256))
ailen = pygame.transform.scale(images.ailen,(250,250))
spaceship_background = pygame.transform.scale(images.spaceship_background, (250,250))
def intro():
    from main import WIDTH_SCREEN, HEIGHT_SCREEN, screen, BLACK, WHITE, WIDTH_CENTER, HEIGHT_CENTER, FPS
    # main 파일에서 변수, 상수, 메소드 불러오기
    
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
        character_name("eca1b0eca78020eba788eba5b4ed81acec8aa420eb8390ec98b9ec9db4")
        
    def Alien():
        character_name("???")
        
    alpha = 0
    story=0

    background_pos = (0, 0)

    #spaceship_background = pygame.transform.scale(spaceship_background, (1280, 720)) #왜 이건 load 빼면 에러?

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

                
        alpha += 1.8

        if alpha > 255:
            alpha = 255
                    
        spaceship_background.set_alpha(alpha)
        screen.blit(spaceship_background, background_pos)
            
        if alpha == 150 and story == 0:
            dialog_box()
            System()
            character_text(2,WHITE,"(외계인들은 유니코드로 대화하지만..)")
            character_text(3,WHITE,"(특별히 해석 해드리겠습니다.)")
                
        elif story == 1:
            dialog_box()
            Alien()
            character_text(2, WHITE, "사령관님 우리 이제 또 어디가야 하나요?")
            character_text(3, WHITE, "이제 들릴 데는 다 간 것 같은데요...")
            system_help()
            
        elif story == 2:
            dialog_box()
            Alien_Leader()
            character_text(2, WHITE, "대장님께서 무슨 계획인지 모르겠지만 지구를 택하셨지... 후훗")
            system_help()
        elif story == 3:
            intro2()
        pygame.display.update()
    pygame.quit()
    
def intro2():
    from main import WIDTH_SCREEN, HEIGHT_SCREEN, screen, BLACK, WHITE, WIDTH_CENTER, HEIGHT_CENTER, FPS
    def draw_dialog(portrait):
        from main import screen

        dialog_box = pygame.image.load('./../Images/ui/dialog_box.png')
        dialog_box = pygame.transform.scale(dialog_box, (1100,200))
        portrait = pygame.transform.scale(portrait, (140, 140))

        screen.blit(dialog_box,(WIDTH_CENTER-550,510))
        screen.blit(portrait, (120,540))

    def dialog_text(text):
        font = pygame.font.Font('./../Fonts/NeoDunggeunmoPro-Regular.ttf', 30)
        text = font.render(text, True, WHITE)
        screen.blit(text,(310, 580))

    intro2_background = pygame.image.load('./../Images/background/intro2_1.png')
    intro2_background = pygame.transform.scale(intro2_background, (1280,720))
    mark_box = pygame.image.load('./../Images/ui/ImanorBalloon.png')
    mark_box = pygame.transform.scale(mark_box,(90,90))

    #캐릭터 x,y 초기화 : 처음 그릴위치
    player_x = 300
    player_y = 300

    ailen_x = 700
    ailen_y = 30

    story =0
    alpha = 0
    running = True
    while running:
        
        deltaTime = FPS.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    story += 1

        screen.blit(intro2_background, (0,0))
        screen.blit(player, (player_x, player_y))
        screen.blit(ailen, (ailen_x, ailen_y))

        ailen_y += 3
        if ailen_y > 300:
            ailen_y = 300
            if story==0:
                draw_dialog(images.boy_portrait)
                dialog_text("와우! 저 흰색 고양이 엄청 크..")

            elif story==1:
                draw_dialog(images.alien_portrait)
                dialog_text("먀먐! 누구야?!")

            elif story==2:
                alpha += 8
                if alpha>255:
                    alpha = 255
                mark_box.set_alpha(alpha)
                screen.blit(mark_box,(360,220))
                draw_dialog(images.boy_portrait)
                dialog_text("으악!")

        pygame.display.update()
    pygame.quit()
            