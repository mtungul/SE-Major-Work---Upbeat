import os
import pygame
import random
from save import complete_lesson
from startScreen import Button
from utils.text import wrap_text
from utils.config import width, height
from screens.baseScreen import baseScreen

class practiceScreen(baseScreen):
    def __init__(self, screen, step_data, runner, icons):
        super().__init__(screen, step_data, runner, icons)
        self.completed = False
        self.state = 'start'

        self.beginButton = pygame.image.load(os.path.join(os.getcwd(),'img', 'begin_btn.png')).convert_alpha()
        self.begin_button = Button(width*(31/72), height/2, self.beginButton, (width*(5/36), height*(1/10)), self.piano)

    def handle_event(self, event):
        if self.state == 'start':
            new_screen = self.begin_button.handle_event(event)
            if new_screen:
                return new_screen
            new_screen = self.back_button.handle_event(event)
            if new_screen:
                return new_screen
            return None

        elif self.state == 'practice':
            pass

        elif self.state == 'finished':
            new_screen = self.back_button.handle_event(event)
            if new_screen:
                return new_screen
            
            if self.completed:
                    return self.next_button.handle_event(event)
            return None
        
        return super().handle_event(event)
    
    def piano(self):
        pass