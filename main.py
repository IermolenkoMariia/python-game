import pygame
from pygame.constants import QUIT

pygame.init()

HEIGHT = 600
WIDTH = 1000
COLOR_BLACK = (0, 0, 0)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

playing = True

while playing:

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False

    main_display.fill(COLOR_BLACK)

    pygame.display.flip()
