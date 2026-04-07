import pygame
import os

pygame.init()

font = pygame.font.Font('fonts/Vera.ttf', 40)
width = 1080
height = 600
clock = pygame.time.Clock()
fps = 60

screen = pygame.display.set_mode([width, height]) #sets screen size
pygame.display.set_caption("software engineering project")
current_dir = os.getcwd()

#load images
pitch_btn = pygame.image.load(os.path.join(current_dir, 'img', 'pitch_btn.png')).convert_alpha()
rhythm_btn = pygame.image.load(os.path.join(current_dir, 'img', 'rhythm_btn.png')).convert_alpha()
select = pygame.image.load(os.path.join(current_dir, 'img', 'select.png')).convert_alpha()
logo = pygame.image.load(os.path.join(current_dir, 'img', 'logo.png')).convert_alpha()

#resize images
select = pygame.transform.scale(select, (170, 50))
logo = pygame.transform.scale(logo, (460, 150))

#text_surface = font.render('Hello, Pygame!', True, (255, 255, 255)) # text, true, text colour

def open_pitch_levels():
    print("Opening pitch levels")

def open_rhythm_levels():
    print("Opening rhythm levels")

class Button:
    def __init__(self, x, y, image, size, action=None):
        self.original = image
        self.normal = pygame.transform.smoothscale(image, size)

        hover_size = (int(size[0]*1.1), int(size[1]*1.1))
        self.hover = pygame.transform.smoothscale(image, hover_size)

        self.rect = self.normal.get_rect(topleft=(x, y))
        self.hover_rect = self.hover.get_rect(center=self.rect.center)

        self.action = action
    
    def draw(self, screen):
            mouse_pos = pygame.mouse.get_pos()

            if self.rect.collidepoint(mouse_pos):
                screen.blit(self.hover, self.hover_rect)
            else:
                screen.blit(self.normal, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()

pitch_button = Button(600, 300, pitch_btn, (325, 200), open_pitch_levels)
rhythm_button = Button(150, 300, rhythm_btn, (325, 200), open_rhythm_levels)


# Main loop
run = True
while run:
    
    for event in pygame.event.get():
        screen.fill((255, 255, 255))
        screen.blit(logo, (315, 50))
        screen.blit(select, (450, 200))
        rhythm_button.draw(screen)
        rhythm_button.handle_event(event)
        pitch_button.draw(screen)
        pitch_button.handle_event(event)

        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()


pygame.quit()