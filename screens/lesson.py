import pygame
from rhythmLevels import levels
from utils.text import wrap_text
from utils.icons import tint_icon 

class lessonScreen:
    def __init__(self, screen, step_data, runner, icons):
        self.screen = screen
        self.font = pygame.font.Font('fonts/Vera.ttf', 20)
        self.data = step_data
        self.runner = runner
        self.icons = icons

    def handle_event(self, event):
        pass

    def draw_level_row(self):
        start_x = 80
        y = 70
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

    def draw(self):
        self.draw_level_row()
        pygame.draw.rect(self.screen, (255, 255, 255), (40, 150, 980, 400), border_radius=20)

        title_font = pygame.font.Font('fonts/new_amsterdam/NewAmsterdam.ttf', 30)
        title = title_font.render(self.data["Title"], True, (0, 0, 0))
        self.screen.blit(title, (55, 175))

        lines = wrap_text(self.data["Text"], self.font, 970)

        y = 225
        for line in lines:
            text = self.font.render(line, True, (0, 0, 0))
            self.screen.blit(text, (60, y))
            y += 40
