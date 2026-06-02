import os
import pygame
from startScreen import Button
from utils.text import wrap_text
from utils.config import width, height
from screens.baseScreen import baseScreen
from utils.excerpts import excerptPlayer

class lessonScreen(baseScreen):
    def __init__(self, screen, step_data, runner, icons):
        super().__init__(screen, step_data, runner, icons)

        self.playButton = pygame.image.load(os.path.join(os.getcwd(),'img', 'play_button.png')).convert_alpha()

        #load level images
        self.lesson_image = None
        if self.data.get("img"):
            image_path = os.path.join(os.getcwd(), 'img', self.data["img"])
            self.lesson_image = pygame.image.load(image_path).convert_alpha()
            self.lesson_image = pygame.transform.scale(self.lesson_image, (475, 250))

        #sound excerpts
        self.audio = excerptPlayer()
        self.excerpts = self.data.get("excerpts", [])
        self.excerpt_images = []
        
        for image_name in self.data.get("excerptImg", []):
            image_path = os.path.join(os.getcwd(), 'img', image_name)
            image = pygame.image.load(image_path).convert_alpha()
            image = pygame.transform.scale(image, (320, 80))
            self.excerpt_images.append(image)
        
        for excerpt in self.excerpts:
            self.audio.load(excerpt, f"soundExcerpts/{excerpt}")
       
        self.excerpt_buttons = []

        self.excerpt_items = []

        for i, excerpt in enumerate(self.excerpts):

            button = Button(width*(11/20), height*(11/20) + i * 120, self.playButton, (50, 50), lambda e=excerpt: self.audio.play(e)) #lambda etc. makes sure each sound is played besides just the last one
            image = self.excerpt_images[i]
            self.excerpt_items.append({
                "button": button,
                "image": image
            })

    def handle_event(self, event):
        
        for item in self.excerpt_items:
            item["button"].handle_event(event)
            
        return super().handle_event(event)

    def draw(self):
        self.draw_layout() #inherited from baseScreen

        #draw text
        line_width = width*(97/108)
        lines = wrap_text(self.data["text"], self.font, line_width)

        y = height/3
        for line in lines:
            text = self.font.render(line, True, (0, 0, 0))
            self.screen.blit(text, (width/18, y))
            y += 40

        #images
        if self.lesson_image:
            self.screen.blit(self.lesson_image, (width/12, y + 10))

        #listening excerpts
        for item in self.excerpt_items:
            button = item["button"]
            image = item["image"]

            button.draw(self.screen)

            image_x = button.rect.x + 100
            image_y = button.rect.y - 20

            self.screen.blit(image, (image_x, image_y))