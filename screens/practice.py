import pygame
import rhythmLevels

class practiceScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font('fonts/Vera.ttf', 40)

    def handle_event(self, event):
        pass

    def draw(self):
        text = self.font.render("Practice Screen", True, (0, 0, 0))
        self.screen.blit(text, (300, 250))
