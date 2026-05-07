import pygame
import os
from utils.config import width, height

class mainScreen:
    def __init__(self, screen, icons):
        self.screen = screen
        self.icons = icons
        current_dir = os.getcwd()

        #load images
        self.pitch_btn = pygame.image.load(os.path.join(current_dir, 'img', 'pitch_btn.png')).convert_alpha()
        self.rhythm_btn = pygame.image.load(os.path.join(current_dir, 'img', 'rhythm_btn.png')).convert_alpha()
        self.select = pygame.image.load(os.path.join(current_dir, 'img', 'select.png')).convert_alpha()
        self.logo = pygame.image.load(os.path.join(current_dir, 'img', 'logo.png')).convert_alpha()

        #resize images
        self.select = pygame.transform.scale(self.select, (width*(17/108), height/12))
        self.logo = pygame.transform.scale(self.logo, (width*(23/54), height/4))

        #define buttons
        self.pitch_button = Button(width*(5/9), height/2, self.pitch_btn, (width*(65/216), height/3), self.open_pitch_levels)
        self.rhythm_button = Button(width*(5/36), height/2, self.rhythm_btn, (width*(65/216), height/3), self.open_rhythm_levels)

    #filler functions for now
    def open_pitch_levels(self):
        print("Opening pitch levels")

    def open_rhythm_levels(self):
        print("Opening rhythm levels")
        from rhythmLevels import levels, levelRunner
        runner = levelRunner(self.screen, levels, self.icons)
        return runner.get_current_screen()
    
    def handle_event(self, event):
        new_screen = self.pitch_button.handle_event(event)
        if new_screen:
            return new_screen

        new_screen = self.rhythm_button.handle_event(event)
        if new_screen:
            return new_screen

    def draw(self):
        self.screen.blit(self.logo, (width*(7/24), height/12))
        self.screen.blit(self.select, (width*(5/12), height*(2/5)))

        self.pitch_button.draw(self.screen)
        self.rhythm_button.draw(self.screen)

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
                    return self.action()