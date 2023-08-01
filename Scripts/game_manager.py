import pygame

pygame.init()

class Button():
    def __init__(self, input_screen, x_pos, y_pos, input_image, image_width, image_height, is_hover, hover_image, action = None):

        self.screen = input_screen
        self.normal_image = input_image
        self.image = self.normal_image
        self.is_hover = is_hover
        self.hover_image = hover_image
        self.x = x_pos
        self.y = y_pos
        self.width = image_width
        self.height = image_height
        self.action = action

        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_press = pygame.mouse.get_pressed()

    def update(self):
        self.screen.blit(self.image,(self.x, self.y))

        if self.x + self.width > self.mouse_pos[0] > self.x and self.y + self.height > self.mouse_pos[1] > self.y:
            if self.is_hover:
                self.image = self.hover_image

            if self.mouse_press[0] and self.action is not None:
                self.action()
         else:
            self.image = self.normal_image