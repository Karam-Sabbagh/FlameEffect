import os

import pygame
from pygame.locals import *

background_color = (0, 0, 0)
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 550
SCREEN_SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), SCREEN_SURFACE)
pygame.display.set_caption("Fire Effect")


flame_pallet = [(7, 7, 7), (30, 7, 7), (47, 15, 7), (71, 15, 7), (87, 23, 7), (103, 31, 7), (143, 39, 7), (159, 46, 7),
                (175, 63, 7), (191.0, 71, 7),               # here v
                (199, 71, 7), (223, 79, 7), (223, 87, 7), (220, 60, 7), (215, 95, 7), (215.0, 103, 15), (207, 111, 15),
                (207, 119, 15),
                (207, 127, 15), (207, 135, 23), (199, 135, 23), (199, 143, 23), (199, 151, 31), (191, 159, 31),
                (191, 162, 33), (191, 167, 39),
                (191, 170, 42), (191, 175, 47), (183, 175, 47), (183, 183, 47), (183, 183, 55), (207, 207, 111),
                (223, 223, 159),
                (239, 239, 199), (255, 255, 255)]

flame_pallet.reverse()

flame_pixels = []

flame_size = SCREEN_WIDTH, 350

flame_colors = []
for each_color in flame_pallet:
    for i in range(int(flame_size[1]/len(flame_pallet))):
        flame_colors.append(each_color)

print(flame_colors)

# def flame_setup():
#     # Set the whole screen pixels to (0, 0, 0)
#     for i in range((flame_size[0]) * (flame_size[1])):
#         flame_pixels.append((255, 255, 255))

def setup_flame():
    for x in range(flame_size[0]):
        for y in range(flame_size[1]):
            flame_pixels.append(flame_colors[y])

def draw_flame_pixels():
    p_x = 0
    p_y = SCREEN_HEIGHT-1

    i = 0
    for p in flame_pixels:
        if SCREEN_HEIGHT-p_y > flame_size[1]:
            p_x += 1
            p_y = SCREEN_HEIGHT-1

        screen.set_at((p_x, p_y), p)

        i += 1
        p_y -= 1

setup_flame()

pygame.display.flip()

FPS = 30
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(FPS)
    screen.fill(background_color)

    draw_flame_pixels()
    pygame.display.flip()
