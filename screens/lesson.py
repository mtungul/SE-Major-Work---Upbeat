import os
import pygame
from utils.text import wrap_text
from utils.icons import tint_icon 
from startScreen import Button

class lessonScreen:
    def __init__(self, screen, step_data, runner, icons):
        self.screen = screen
        self.font = pygame.font.Font('fonts/Vera.ttf', 20)
        self.data = step_data
        self.runner = runner
        self.icons = icons

        self.nextButton = pygame.image.load(os.path.join(os.getcwd(),'img', 'next_button.png')).convert_alpha()
        self.nextButton = pygame.transform.scale(self.nextButton, (150, 60))

    def handle_event(self, event):
        new_screen = self.next_button.handle_event(event)
        if new_screen:
            return new_screen

    def draw_icon_row(self): #draws the row of icons at the top of the screen
        start_x = 80
        y = 60
        spacing = 85

        for i in range(len(self.runner.steps)):
            x = start_x + i * spacing

            step = self.runner.steps[i]
            icon_name = step["icon"]

            if step["section"] == "rhythm":
                icon = self.icons.rhythm_icons[icon_name]
            else:
                icon = self.icons.pitch_icons[icon_name]

            if i == self.runner.index:
                icon = tint_icon(icon, (255, 255, 255))
            elif self.runner.completed[i]:
                icon = tint_icon(icon, (200, 200, 200))
            else:
                icon = tint_icon(icon, (120, 120, 120))  

            rect = icon.get_rect(center=(x, y))
            self.screen.blit(icon, rect)

    def go_next(self):
        return self.runner.next_level()

    def draw(self):
        self.draw_icon_row()

        pygame.draw.rect(self.screen, (255, 255, 255), (40, 125, 980, 400), border_radius=20)

        title_font = pygame.font.Font('fonts/new_amsterdam/NewAmsterdam.ttf', 40)
        title = title_font.render(self.data["title"], True, (0, 0, 0))
        self.screen.blit(title, (55, 140))

        lines = wrap_text(self.data["text"], self.font, 970)

        y = 200
        for line in lines:
            text = self.font.render(line, True, (0, 0, 0))
            self.screen.blit(text, (60, y))
            y += 40
        
        self.next_button = Button(850, 530, self.nextButton, (150, 60), self.go_next)
        self.next_button.draw(self.screen)


