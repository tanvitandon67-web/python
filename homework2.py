import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("circle")

running = True
while running:
    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 255), (200, 200, 100, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()