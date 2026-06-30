import math
import random
import pygame
 
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 2
ENEMY_SPEED_Y = 5
BULLET_SPEED_Y = 7
COLLISION_DISTANCE = 27

pygame.init()

screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))

background = pygame.image.load('backeground.jpg')
background = pygame.transform.scale(background,(800,500))

pygame.display.set_caption("Space Invader")
icon = pygame.image.load("Player.png")
pygame.display.set_icon(icon)

playerimage = pygame.image.load('Player.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

enemyimage = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemies = 6

for _i in range(number_of_enemies):
    enemyimage.append(pygame.image.load('enemy.jpg'))
    enemyimage = pygame.transform.scale(enemyimage,(40,40))
    enemyX.append(random.randint(0,SCREEN_WIDTH - 64))
    enemyY.append(random.randint(0,ENEMY_START_Y_MIN,ENEMY_START_Y_MAX ))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

bulletimage = pygame.image.load('bullet.webp')
bulletimage = pygame.transform.scale(bulletimage,(16,16))
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y
bulletstate = 'ready'

scorevalue = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

gameoverfont = pygame.font.Font('freesansbold.ttf',64)

def show_score(x,y) :
    score = font.render("score : " + str(scorevalue),True,(255,255,255))
    screen.blit(score,(x,y))

def gameovertext() :
    gameovertext = gameoverfont.render("Gameover ",True,(255,255,255))


