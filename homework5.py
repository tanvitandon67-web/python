import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))

bg = pygame.image.load("background.jpg")
sound = pygame.mixer.Sound("sound.wav")
sound.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg, (0, 0))
    pygame.display.flip()
