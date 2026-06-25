import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))

box1 = pygame.Rect(100, 200, 50, 50)
box2 = pygame.Rect(300, 200, 50, 50)

color = (255, 0, 0)

event = pygame.USEREVENT + 1
pygame.time.set_timer(event, 1000)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

        if e.type == event:
            color = (0, 0, 255)

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, color, box1)
    pygame.draw.rect(screen, color, box2)

    pygame.display.update()

pygame.quit()