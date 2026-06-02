import os
import pygame
from startScreen import Button
from utils.text import wrap_text
from utils.icons import tint_icon 
from utils.config import width, height

class baseScreen:
    def __init__(self, screen, step_data, runner, icons):
        self.screen = screen
        self.font = pygame.font.Font('fonts/Vera.ttf', 20)
        self.data = step_data
        self.runner = runner
        self.icons = icons
        self.icon_hitbox = []

        #load and size buttons
        self.nextButton = pygame.image.load(os.path.join(os.getcwd(),'img', 'next_button.png')).convert_alpha()
        self.backButton = pygame.image.load(os.path.join(os.getcwd(),'img', 'back_button.png')).convert_alpha()
        self.next_button = Button(width*(85/108), height*(53/60), self.nextButton, (width*(5/36), height*(1/10)), self.go_next)
        self.back_button = Button(width*(7/108), height*(53/60), self.backButton, (width*(5/36), height*(1/10)), self.go_back)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos #stores where player clicked

            for i, hitbox in enumerate(self.icon_hitbox):
                if hitbox.collidepoint(mouse_pos):

                    return self.runner.go_to_level(i)
       
        new_screen = self.next_button.handle_event(event)
        if new_screen:
            return new_screen
        
        new_screen = self.back_button.handle_event(event)
        if new_screen:
            return new_screen

    def draw_icon_row(self): #draws the row of icons at the top of the screen
        start_x = width*(2/27)
        y = height/10
        spacing = 106
        self.icon_hitbox = []

        for i in range(len(self.runner.steps)):
            x = start_x + i * spacing

            step = self.runner.steps[i]
            icon_name = step["icon"]

            if step["section"] == "rhythm":
                icon = self.icons.rhythm_icons[icon_name]
            else:
                icon = self.icons.pitch_icons[icon_name]

            if i == self.runner.index: 
                icon = tint_icon(icon, (255, 255, 255)) #current level
            elif self.runner.completed[i]:
                icon = tint_icon(icon, (235, 235, 235)) #completed levels
            else:
                icon = tint_icon(icon, (120, 120, 120)) #haven't completed yet

            hitbox = icon.get_rect(center=(x, y))
            self.icon_hitbox.append(hitbox)
            self.screen.blit(icon, hitbox)

    def go_next(self):
        return self.runner.next_level()
    
    def go_back(self):
        return self.runner.back_level()

    def show_next_button(self):
        return True
    
    def draw_layout(self):
        self.draw_icon_row()
                                    #numbers = colour (3), position (2), size(2)   
        pygame.draw.rect(self.screen, (255, 255, 255), (width/27, height*(5/24), width*(25/27), height*(2/3)), border_radius=20) 
        
        #draw title
        title_font = pygame.font.Font('fonts/new_amsterdam/NewAmsterdam.ttf', 40)
        title = title_font.render(self.data["title"], True, (0, 0, 0))
        self.screen.blit(title, (width*(11/216), height*(7/30)))

        #next and back buttons
        if self.show_next_button(): #makes it easier to overide in practice.py
            self.next_button.draw(self.screen)  

        if self.runner.index != 0:
            self.back_button.draw(self.screen)