import pygame
from startScreen import mainScreen 

pygame.init()

width = 1080
height = 600
screen = pygame.display.set_mode((width, height))

#font = pygame.font.Font('fonts/Vera.ttf', 40)
#text_surface = font.render('Hello, Pygame!', True, (255, 255, 255)) # text, true, text colour

current_screen = mainScreen(screen)

run = True
while run:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        current_screen.handle_event(event)

    current_screen.draw()

    pygame.display.update()

pygame.quit()