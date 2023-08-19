import pygame
import player as p
pygame.init()

screen = pygame.display.set_mode((500,500))
running = True

effect_group = pygame.sprite.Group()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                effect = p.SwordEffect(1, 200, 200)
                effect_group.add(effect)
                effect_group.draw(screen)

    pygame.display.update()
pygame.quit()