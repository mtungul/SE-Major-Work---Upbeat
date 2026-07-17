import os
import pygame
from save import load_save
from levels.levelRunner import levelRunner
from utils.config import width, height
from utils.text import wrap_text

class mainScreen:
    def __init__(self, screen, icons):
        self.screen = screen
        self.icons = icons
        current_dir = os.getcwd()
        self.font = pygame.font.Font('fonts/Vera.ttf', 20)

        #load images
        self.pitch_btn = pygame.image.load(os.path.join(current_dir, 'img', 'buttons', 'pitch_btn.png')).convert_alpha()
        self.rhythm_btn = pygame.image.load(os.path.join(current_dir, 'img', 'buttons', 'rhythm_btn.png')).convert_alpha()
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
        save = load_save()
        if save['completed_lessons'].get('Final Rhythm Practice', False):
            from levels.pitchLevels import pitchlevels
            runner = levelRunner(self.screen, pitchlevels, self.icons)
            return runner.get_current_screen()
        else:
            print("Must complete rhythm section")

    def open_rhythm_levels(self):
        from levels.rhythmLevels import levels
        runner = levelRunner(self.screen, levels, self.icons)
        return runner.get_current_screen()
    
    def handle_event(self, event):
        new_screen = self.pitch_button.handle_event(event)
        if new_screen:
            return new_screen

        new_screen = self.rhythm_button.handle_event(event)
        if new_screen:
            return new_screen

    def show_instructions(self):
        #black box background
        black_box = pygame.Surface((width * 0.6, height * 0.6))
        black_box.fill((255, 0, 255))
        black_box.set_colorkey((255, 0, 255)) 
        pygame.draw.rect(black_box, (0, 0, 0), (0, 0, width * 0.6, height * 0.6), border_radius=15)
        black_box.set_alpha(220) 
        self.screen.blit(black_box, (width/2 - width * 0.6 / 2, height/2 - height * 0.6 / 2))

        #text
        welcome_text = ("Welcome to Upbeat!                                               "
        "Upbeat is a beginner friendly educational game that will help you learn about music theory! "
        "Please ensure your sound is turned ON and that you have access to a mouse / trackpad and keyboard.")
        "Note: Your progress will be saved once you fully complete each level and will be indicated by the icons at the top of your screen."
        
        line_width = width*(0.5)
        lines = wrap_text(welcome_text, self.font, line_width)

        y = height/3
        for line in lines:
            text = self.font.render(line, True, (255, 255, 255))
            self.screen.blit(text, (width/18, y))
            y += 40

        #show meaning of icons

    def show_progress(self):
        pass
        #in the top left corner should be a small icon that when clicked shows what levels have been completed

    def reset_game(self):
        pass
        #reset everything in the json file and starts from the very beginning including show_instructions

    def draw(self):
            self.screen.blit(self.logo, (width*(7/24), height/12))
            self.screen.blit(self.select, (width*(5/12), height*(2/5)))

            self.pitch_button.draw(self.screen)
            self.rhythm_button.draw(self.screen)

            self.show_instructions()
            '''instructions = self.show_instructions()
            self.screen.blit(instructions)'''

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