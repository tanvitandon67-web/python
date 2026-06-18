import pygame


pygame.init()


screen = pygame.display.set_mode((500, 500))


pygame.display.set_caption("My Pygame Window")


background_color = (173, 216, 230)

image = pygame.image.load("picture.png")   # Make sure picture.png is in the same folder


running = True
while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill(background_color)


    screen.blit(image, (150, 150))

    pygame.display.update()


pygame.quit()