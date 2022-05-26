import os
from turtle import width
import pygame

# TODO: Setup pixel data structure...

background_color = (0, 0, 0)
(width, height) = (600, 600)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flame Effect")
screen.fill(background_color)

pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

