import random
import os
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_RIGHT, K_LEFT

pygame.init()

clock = pygame.time.Clock()
FPS = 120

HEIGHT = 600
WIDTH = 1000

FONT = pygame.font.SysFont('Verdana', 20)

COLOR_BLACK = (0, 0, 0)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.transform.scale(pygame.image.load('background.png'), (WIDTH, HEIGHT))
background_X1 = 0
background_X2 = background.get_width()
background_move = 3

IMAGE_PATH = "Goose"
PLAYER_IMAGES = os.listdir(IMAGE_PATH)

PLAYER_SIZE = (20, 20)
player = pygame.image.load('player.png').convert_alpha()
player_rect = player.get_rect()
player_rect.center = main_display.get_rect().center
MOVE_DOWN = [0, 4]
MOVE_UP = [0, -4]
MOVE_RIGHT = [4, 0]
MOVE_LEFT = [-4, 0]

enemy_surface = pygame.image.load('enemy.png').convert_alpha()
bonus_surface = pygame.image.load('bonus.png').convert_alpha()

def create_enemy():
    rect =  pygame.Rect(
        WIDTH, 
        random.randint(enemy_surface.get_width(), HEIGHT - enemy_surface.get_height()), 
        *enemy_surface.get_size()
    )
    move = [random.randint(-8, -4), 0]
    return [rect, move]

def create_bonus():
    rect = pygame.Rect(
        random.randint(bonus_surface.get_width(), WIDTH - bonus_surface.get_width()), 
        -bonus_surface.get_height(), 
        *bonus_surface.get_size()
    )
    move = [0, random.randint(4, 8)]
    return [rect, move]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 3000)

CHANGE_IMAGE = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMAGE, 200)

enemies = []

bonuses = []

score = 0

image_index = 0

playing = True

while playing:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())
        if event.type == CHANGE_IMAGE:
            player = pygame.image.load(os.path.join(IMAGE_PATH, PLAYER_IMAGES[image_index]))
            image_index += 1
            if image_index >= len(PLAYER_IMAGES):
                image_index = 0
    
    background_X1 -= background_move
    background_X2 -= background_move

    if background_X1 < -background.get_width():
        background_X1 = background.get_width()
    
    if background_X2 < -background.get_width():
        background_X2 = background.get_width()

    main_display.blit(background, (background_X1, 0))
    main_display.blit(background, (background_X2, 0))

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

        if player_rect.colliderect(enemy[0]):
            playing = False
    
    for bonus in bonuses:
        bonus[0] = bonus[0].move(bonus[1])
        main_display.blit(bonus_surface, bonus[0])

        if player_rect.colliderect(bonus[0]):
            score += 1
            bonuses.pop(bonuses.index(bonus))
    
    main_display.blit(FONT.render(str(score), True, COLOR_BLACK), (WIDTH-50, 20))
    main_display.blit(player, player_rect)

    pygame.display.flip()

    for enemy in enemies:
        if enemy[0].left < 0:
            enemies.pop(enemies.index(enemy))
    
    for bonus in bonuses:
        if bonus[0].bottom >= HEIGHT:
            bonuses.pop(bonuses.index(bonus))
