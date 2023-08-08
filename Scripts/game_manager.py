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
    def __init__(self,x,y, dx, dy, radius, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.color = color

    def render(self, screen):
        self.x += self.dx
        self.y += self.dy
        self.radius -= 0.1

        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

particles = []
def draw_particle():
    from main import screen
    for particle in particles:
        particle.draw(screen)
        if particle.radius <=0 :
            particles.remove(particle)