import pygame
import startScreen

pygame.init()
width = 1080
height = 600

pygame.display.set_caption("software engineering project")
screen = pygame.display.set_mode([width, height])

run = True
while run:
    screen.fill('blue')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()

pygame.quit()