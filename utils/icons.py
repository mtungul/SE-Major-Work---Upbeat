import pygame
from utils.config import resource_path

class Icons:
    def __init__(self):
        icon_size = (80, 80)

        #rhythm icons
        self.rhythm_icons = {
            "book": pygame.transform.smoothscale(pygame.image.load(resource_path("img/r_book_icon.png")), icon_size),
            "lesson": pygame.transform.smoothscale(pygame.image.load(resource_path("img/r_lesson_icon.png")), icon_size),
            "quaver": pygame.transform.smoothscale(pygame.image.load(resource_path("img/r_quaver_icon.png")), icon_size),
            "star": pygame.transform.smoothscale(pygame.image.load(resource_path("img/r_star_icon.png")), icon_size),

        }

        #pitch icons
        self.pitch_icons = {
            "book": pygame.transform.smoothscale(pygame.image.load(resource_path("img/p_book_icon.png")), icon_size),
            "lesson": pygame.transform.smoothscale(pygame.image.load(resource_path("img/p_lesson_icon.png")), icon_size),
            "quaver": pygame.transform.smoothscale(pygame.image.load(resource_path("img/p_quaver_icon.png")), icon_size),
            "star": pygame.transform.smoothscale(pygame.image.load(resource_path("img/p_star_icon.png")), icon_size),
        }
    
def tint_icon(image, color):
    tinted = image.copy()
    tinted.fill(color, special_flags=pygame.BLEND_RGB_MULT)
    return tinted