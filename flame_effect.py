import os

import pygame
from pygame.locals import *

# TODO: Setup pixel data structure...

background_color = (0, 0, 0)
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500
WINDOW_SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), WINDOW_SURFACE)
pygame.display.set_caption("Fire Effect")

def draw_points(points: list):

    for p in points:
        WINDOW_SURFACE.set_at((p[x], p[y]), my_color)


pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

