import math
import random
import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 2
ENEMY_SPEED_Y = 5
BULLET_SPEED_Y = 7
COLLISION_DISTANCE = 27


pygame.init()
clock = pygame.time.Clock()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


background = pygame.image.load('backeground.jpg')
background = pygame.transform.scale(background, (800, 500))


pygame.display.set_caption("Space Invader")
icon = pygame.image.load('Player.png')
pygame.display.set_icon(icon)


playerImg = pygame.image.load('Player.png')
playerImg = pygame.transform.scale(playerImg, (60, 60))
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0


enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 7

for _i in range(num_of_enemies):
    enemy_image = pygame.image.load('enemy.jpg')
    enemy_image = pygame.transform.scale(enemy_image, (40, 40))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64)) 
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

clock.tick(60)
pygame.quit()