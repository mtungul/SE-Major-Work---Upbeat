import pygame
from utils.icons import Icons
from utils.config import width, height, resource_path
from startScreen import mainScreen 

pygame.init()

#set screen size and title
pygame.display.set_caption("Upbeat!")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#set background (doesn't change)
background = pygame.image.load(resource_path('img/background.png')).convert_alpha()
background = pygame.transform.scale(background, (width, height))

icons = Icons()
current_screen = mainScreen(screen, icons)

#main game loop
run = True
while run:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        new_screen = current_screen.handle_event(event)
        if new_screen:
            current_screen = new_screen
    
    if hasattr(current_screen, 'update'):
        current_screen.update()

    current_screen.draw()

    pygame.display.update()
    clock.tick(60)

pygame.quit()