import pygame
pygame.init()

screen = pygame.display.set_mode ((500,400))

screen.fill((255,252,255))

green = (0,255,0)

pygame.draw.circle(screen,green,(300,300),50)

pygame.draw.circle(screen,green, (100,100),50,3)
pygame.display.update()
pygame.time.wait(10000)


running = True

while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT():
            running = False

    pygame.display.flip()
pygame.time.wait(10000)
pygame.quit()
