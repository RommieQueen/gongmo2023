import pygame

pygame.init()


def intro():
    # main 파일에서 변수, 상수, 메소드 불러오기
    from main import WIDTH_SCREEN, HEIGHT_SCREEN, screen, BLACK, WHITE, WIDTH_CENTER, HEIGHT_CENTER, FPS

    # 대화상자에서 줄을 바꿀 수 있음 1, 4번째 줄은 인물 대화용으로 사용하지 말 것.(1줄 이름, 4줄 시스템)
    def get_line_pos(text_name, get_line):
        if get_line == 1:
            text_pos = text_name.get_rect(center = (WIDTH_CENTER, HEIGHT_CENTER + 375))
        elif get_line == 2:
            text_pos = text_name.get_rect(center = (WIDTH_CENTER, HEIGHT_CENTER + 400))
        elif get_line == 3:
            text_pos = text_name.get_rect(center = (WIDTH_CENTER, HEIGHT_CENTER + 425))
        elif get_line == 4:
            text_pos = text_name.get_rect(center = (WIDTH_CENTER, HEIGHT_CENTER + 445))

        return text_pos

    #인물 이름 설정할 수 있음
    def character_name(*get_text):
        character_name_font = pygame.font.Font('./../Fonts/NeoDunggeunmoPro-Regular.ttf', 20)
        character_name_line = character_name_font.render(*get_text, True, WHITE)
        screen.blit(character_name_line, get_line_pos(character_name_line, 1))
        
    # 인물들의 말을 출력할 수 있도록 함
    # 대화상자에서 출력하고 싶은 라인, 원하는 색, 인물 대화 입력
    def character_text(get_line, get_color, *get_text):
        character_text_font = pygame.font.Font('./../Fonts/NeoDunggeunmoPro-Regular.ttf', 20)
        character_line = character_text_font.render(*get_text, True, get_color)
        screen.blit(character_line, get_line_pos(character_line, get_line))

    # 대화상자에서 다음으로 넘기기를 알려줌
    def system_help():
        system_font = pygame.font.Font('./../Fonts/NeoDunggeunmoPro-Regular.ttf', 16)
        system_line_help = system_font.render("▼SPACE를 눌러 진행▼", True, WHITE)
        screen.blit(system_line_help, get_line_pos(system_line_help, 4))

    def Sarah():
        character_name("사라")

    def Alien_Leader():
        character_name("eca1b0eca78020eba788eba5b4ed81acec8aa420eb8390ec98b9ec9db4")
        
    def Alien():
        character_name("???")
        
    alpha = 0
    story = 0

    background_pos = (0, 0)

    screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN + 100))

    spaceship_background = pygame.image.load('./../Images/background/spaceship.jpg')
    spaceship_background = pygame.transform.scale(spaceship_background, (1280, 720))

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
                Alien()
                character_text(2, WHITE, "사령관님 우리 이제 또 어디가야 하나요?")
                character_text(3, WHITE, "이제 들릴 때는 다 간 것 같은데요...")
                system_help()
                
        if story == 1:
            
            alpha = 255
                    
            spaceship_background.set_alpha(alpha)
            screen.blit(spaceship_background, background_pos)
            
            if alpha == 255:
                Alien_Leader()
                character_text(2, WHITE, "ec9ab0eba6b020eca780eab5aceba19c20eab084eb8ba42e2e2e20ed9b84ed9b97")
                character_text(3, WHITE, "대장님께서 무슨 계획인지 모르겠지만 지구를 택하셨지... 후훗")
                system_help()
                
        pygame.display.update()
        
    pygame.quit()
