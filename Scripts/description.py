import pygame
from game import *

pygame.init()

def description():
    while True:
        for event in pygame.event.get():
            screen.fill(WHITE)