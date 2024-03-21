import pygame
from pygame.constants import QUIT

pygame.init()

clock = pygame.time.Clock()
FPS = 120

HEIGHT = 600
WIDTH = 1000
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

player_size = (20, 20)
player = pygame.Surface(player_size)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()
player_direction = [1, 1]

playing = True

while playing:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False

    main_display.fill(COLOR_BLACK)

    if player_rect.bottom >= HEIGHT:
        player_direction = [1, -1]
    
    if player_rect.top < 0:
        player_direction = [-1, 1]
    
    if player_rect.right >= WIDTH:
        player_direction = [-1, -1]
    
    if player_rect.left < 0:
        player_direction = [1, 1]
    
    main_display.blit(player, player_rect)

    player_rect = player_rect.move(player_direction)

    pygame.display.flip()
