import pygame
import os
from startScreen import mainScreen 
from utils.icons import Icons
from utils.config import width, height

pygame.init()

#set screen size and title
pygame.display.set_caption("software engineering project")
screen = pygame.display.set_mode((width, height))

#set background (doesn't change)
background = pygame.image.load(os.path.join(os.getcwd(),'img', 'background.png')).convert_alpha()
background = pygame.transform.scale(background, (width, height))

icons = Icons()
current_screen = mainScreen(screen, icons)

run = True
while run:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        new_screen = current_screen.handle_event(event)
        if new_screen:
            current_screen = new_screen

    current_screen.draw()

    pygame.display.update()

pygame.quit()