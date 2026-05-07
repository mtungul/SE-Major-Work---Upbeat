import os
import pygame
from utils.text import wrap_text
from utils.icons import tint_icon 
from startScreen import Button
from utils.config import width, height

class lessonScreen:
    def __init__(self, screen, step_data, runner, icons):
        self.screen = screen
        self.font = pygame.font.Font('fonts/Vera.ttf', 20)
        self.data = step_data
        self.runner = runner
        self.icons = icons

        #load and size buttons
        self.nextButton = pygame.image.load(os.path.join(os.getcwd(),'img', 'next_button.png')).convert_alpha()
        self.backButton = pygame.image.load(os.path.join(os.getcwd(),'img', 'back_button.png')).convert_alpha()
        self.next_button = Button(width*(85/108), height*(53/60), self.nextButton, (width*(5/36), height*(1/10)), self.go_next)
        self.back_button = Button(width*(7/108), height*(53/60), self.backButton, (width*(5/36), height*(1/10)), self.go_back)

        #load a size level images
        self.noteChart = pygame.image.load(os.path.join(os.getcwd(),'img', 'note_value_chart.png')).convert_alpha()
        self.noteChart = pygame.transform.scale(self.noteChart, (375, 125)) #NEED TO CHANGE THIS!!!

    def handle_event(self, event):
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

            rect = icon.get_rect(center=(x, y))
            self.screen.blit(icon, rect)

    def go_next(self):
        return self.runner.next_level()
    
    def go_back(self):
        return self.runner.back_level()

    def draw(self):
        self.draw_icon_row()

        pygame.draw.rect(self.screen, (255, 255, 255), (width/27, height*(5/24), width*(25/27), height*(2/3)), border_radius=20) #numbers = colour (3), position (2), size(2)

        title_font = pygame.font.Font('fonts/new_amsterdam/NewAmsterdam.ttf', 40)
        title = title_font.render(self.data["title"], True, (0, 0, 0))
        self.screen.blit(title, (width*(11/216), height*(7/30)))

        if self.data["img"] != '':
            line_width = width*(25/54)
            #self.screen.blit(self.data["img"], (500, 200))
        else:
            line_width = width*(97/108)
        
        lines = wrap_text(self.data["text"], self.font, line_width)

        y = height/3
        for line in lines:
            text = self.font.render(line, True, (0, 0, 0))
            self.screen.blit(text, (width/18, y))
            y += 40
        
        self.next_button.draw(self.screen)
        self.back_button.draw(self.screen)

        '''step = self.steps[self.index]
        if step["lessonType"] != "reading":
            self.next_button = Button(150, 530, self.nextButton, (150, 60), self.go_next)
            self.next_button.draw(self.screen)'''


#make sure to commit after fixing the sizes of everything --> 'resized screen and images + added back button'