import pygame

pygame.init()

class Button:
    def __init__(self, input_screen, x_pos, y_pos, input_image, image_width, image_height, action = None):
        mouse_pos = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed()
        if x_pos + image_width > mouse_pos[0] > x_pos and y_pos + image_height > mouse_pos[1] > y_pos:
            input_screen.blit(input_image, (x_pos, y_pos))
            if mouse_press[0] and action is not None:
                action()                            
        else:
            input_screen.blit(input_image, (x_pos, y_pos))

class Particle():
    def __init__(self,x,y, radius, color,gravity=None):
        self.x = x
        self.y = y

        self.radius = radius
        self.color = color
        self.gravity = gravity

    def render(self, screen,x,y):
        self.x = x
        self.y = y

        if self.gravity is not None:
            self.y += self.gravity

        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

particles = []
def draw_particle(x, y):
    from main import screen
    for particle in particles:
        particle.render(screen,x,y)
        if particle.radius <=0 :
            particles.remove(particle)
