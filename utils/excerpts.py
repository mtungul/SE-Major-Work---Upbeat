import pygame

class excerptPlayer:
    def __init__(self):
        self.sounds = {}

    def load(self, name, path):
        self.sounds[name] = pygame.mixer.Sound(path)

    def play(self, name):
        pygame.mixer.stop()  #ensures one excerpt at a time
        self.sounds[name].play()