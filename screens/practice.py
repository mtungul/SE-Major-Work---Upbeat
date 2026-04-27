import os
import pygame
from utils.text import wrap_text
from utils.icons import tint_icon 
from startScreen import Button

class practiceScreen:
    def __init__(self, screen, step_data, runner, icons):
        self.screen = screen
        self.font = pygame.font.Font('fonts/Vera.ttf', 20)
        self.data = step_data
        self.runner = runner
        self.icons = icons

        self.nextButton = pygame.image.load(os.path.join(os.getcwd(),'img', 'next_button.png')).convert_alpha()
        self.nextButton = pygame.transform.scale(self.nextButton, (150, 60))

    def handle_event(self, event):
        pass

    def draw(self):
        text = self.font.render("Practice Screen", True, (0, 0, 0))
        self.screen.blit(text, (300, 250))
