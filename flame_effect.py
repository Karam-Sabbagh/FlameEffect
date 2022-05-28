import os

import pygame
from pygame.locals import *
import random

background_color = (0, 0, 0)
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 168
SCREEN_SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), SCREEN_SURFACE)
pygame.display.set_caption("Fire Effect")

FIRE_WIDTH = 320
FIRE_HEIGHT = 168

palette = []

# Palette based coordinate system origin upper - left.
fire_pixels = []

rgbs = [
    0x07, 0x07, 0x07,
    0x1F, 0x07, 0x07,
    0x2F, 0x0F, 0x07,
    0x47, 0x0F, 0x07,
    0x57, 0x17, 0x07,
    0x67, 0x1F, 0x07,
    0x77, 0x1F, 0x07,
    0x8F, 0x27, 0x07,
    0x9F, 0x2F, 0x07,
    0xAF, 0x3F, 0x07,
    0xBF, 0x47, 0x07,
    0xC7, 0x47, 0x07,
    0xDF, 0x4F, 0x07,
    0xDF, 0x57, 0x07,
    0xDF, 0x57, 0x07,
    0xD7, 0x5F, 0x07,
    0xD7, 0x5F, 0x07,
    0xD7, 0x67, 0x0F,
    0xCF, 0x6F, 0x0F,
    0xCF, 0x77, 0x0F,
    0xCF, 0x7F, 0x0F,
    0xCF, 0x87, 0x17,
    0xC7, 0x87, 0x17,
    0xC7, 0x8F, 0x17,
    0xC7, 0x97, 0x1F,
    0xBF, 0x9F, 0x1F,
    0xBF, 0x9F, 0x1F,
    0xBF, 0xA7, 0x27,
    0xBF, 0xA7, 0x27,
    0xBF, 0xAF, 0x2F,
    0xB7, 0xAF, 0x2F,
    0xB7, 0xB7, 0x2F,
    0xB7, 0xB7, 0x37,
    0xCF, 0xCF, 0x6F,
    0xDF, 0xDF, 0x9F,
    0xEF, 0xEF, 0xC7,
    0xFF, 0xFF, 0xFF]

# Populate pallete.
for i in range(int(len(rgbs) / 3)):
    palette.append({
        "r": rgbs[i * 3 + 0],
        "g": rgbs[i * 3 + 1],
        "b": rgbs[i * 3 + 2]})

y_scrolling = 440
def setup():
    # set the whole screen to 0(color: 0x07,0x07,0x07)
    for i in range(FIRE_WIDTH*FIRE_HEIGHT):
        fire_pixels.append(0)

    # Set bottom line to 36(color white: 0xFF, 0xFF, 0xFF)
    for i in range(FIRE_WIDTH):
        fire_pixels[(FIRE_HEIGHT - 1) * FIRE_WIDTH + i] = 3

    y_scrolling = 440

setup()

def spread_fire(src):
    pixel = fire_pixels[src]
    if pixel == 0:
        fire_pixels[src - FIRE_WIDTH] = 0
    else:
        rand_idx = random.randint(0, 3)
        dst = src-rand_idx+1
        fire_pixels[dst - FIRE_WIDTH] = pixel - (rand_idx & 1)

def do_fire():
    for x in range(FIRE_WIDTH):
        for y in range(FIRE_HEIGHT):
            spread_fire(y*FIRE_WIDTH+x)

setup()

def draw_fire_pixels():
    for x in range(FIRE_WIDTH):
        for y in range(FIRE_HEIGHT):
            pixel_color = palette[fire_pixels[x*y]]
            pixel_color = pixel_color["r"], pixel_color["g"], pixel_color["b"]
            screen.set_at((x, FIRE_HEIGHT-y), pixel_color)

def draw():
    do_fire()
    draw_fire_pixels()

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
    draw()
    pygame.display.flip()
