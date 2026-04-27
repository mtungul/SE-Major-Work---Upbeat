import pygame
import os

class Icons:
    def __init__(self):
        current_dir = os.getcwd()
        icon_size = (64, 64)
        #rhythm icons
        self.rhythm_icons = {
            "book": pygame.transform.smoothscale(pygame.image.load(os.path.join(current_dir, "img/r_book_icon.png")), icon_size),
            "lesson": pygame.transform.smoothscale(pygame.image.load(os.path.join(current_dir, "img/r_lesson_icon.png")), icon_size),
            "quaver": pygame.transform.smoothscale(pygame.image.load(os.path.join(current_dir, "img/r_quaver_icon.png")), icon_size),
            "star": pygame.transform.smoothscale(pygame.image.load(os.path.join(current_dir, "img/r_star_icon.png")), icon_size),

        }

        #pitch icons
        self.pitch_icons = {
            "book": pygame.transform.smoothscale(pygame.image.load(os.path.join(current_dir, "img/p_book_icon.png")), icon_size),
            "lesson": pygame.transform.smoothscale(pygame.image.load(os.path.join(current_dir, "img/p_lesson_icon.png")), icon_size),
            "quaver": pygame.transform.smoothscale(pygame.image.load(os.path.join(current_dir, "img/p_quaver_icon.png")), icon_size),
            "star": pygame.transform.smoothscale(pygame.image.load(os.path.join(current_dir, "img/p_star_icon.png")), icon_size),
        }
    
def tint_icon(image, color):
    tinted = image.copy()
    tinted.fill(color, special_flags=pygame.BLEND_RGB_MULT)
    return tinted