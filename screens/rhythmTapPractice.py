import os
import pygame
from utils.text import wrap_text
from startScreen import Button
from screens.baseScreen import baseScreen

class practiceScreen(baseScreen):
    def __init__(self, screen, step_data, runner, icons):
        super().__init__(screen, step_data, runner, icons)
        #self.completed = completed

    def handle_event(self, event):
        return super().handle_event(event)

    def show_next_button(self):
        return True
        #return self.completed
    
    def draw(self):
        self.draw_layout()
        
        
