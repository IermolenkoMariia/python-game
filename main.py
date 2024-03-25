import random
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_RIGHT, K_LEFT

pygame.init()

clock = pygame.time.Clock()
FPS = 120

HEIGHT = 600
WIDTH = 1000
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_BLUE = (0, 0, 255)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

PLAYER_SIZE = (20, 20)
player = pygame.Surface(PLAYER_SIZE)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()
MOVE_DOWN = [0, 1]
MOVE_UP = [0, -1]
MOVE_RIGHT = [1, 0]
MOVE_LEFT = [-1, 0]

ENEMY_SIZE = (20, 20)
enemy_surface = pygame.Surface(ENEMY_SIZE)
enemy_surface.fill(COLOR_BLUE)

def create_enemy(size):
    rect = pygame.Rect(WIDTH, random.randint(0, HEIGHT), *size)
    move = [random.randint(-6, -1), 0]
    return [rect, move]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

enemies = []

playing = True

while playing:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy(ENEMY_SIZE))

    main_display.fill(COLOR_BLACK)

    keys = pygame.key.get_pressed()

    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(MOVE_DOWN)
    
    if keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(MOVE_UP)
    
    if keys[K_RIGHT] and player_rect.right < WIDTH:
        player_rect = player_rect.move(MOVE_RIGHT)
    
    if keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(MOVE_LEFT)
    
    for enemy in enemies:
        enemy[0] = enemy[0].move(enemy[1])
        main_display.blit(enemy_surface, enemy[0])
    
    main_display.blit(player, player_rect)

    pygame.display.flip()

    for enemy in enemies:
        if enemy[0].left < 0:
            enemies.pop(enemies.index(enemy))