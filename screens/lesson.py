import os
import pygame
from metronome import metronome
from startScreen import Button
from utils.text import wrap_text
from utils.config import width, height
from utils.excerpts import excerptPlayer
from screens.baseScreen import baseScreen

class lessonScreen(baseScreen):
    def __init__(self, screen, step_data, runner, icons):
        super().__init__(screen, step_data, runner, icons)

        self.playButton = pygame.image.load(os.path.join(os.getcwd(),'img', 'play_button.png')).convert_alpha()

        #load level images
        self.lesson_image = None
        if self.data.get("img"):
            image_path = os.path.join(os.getcwd(), 'img', self.data["img"])
            self.lesson_image_original = pygame.image.load(image_path).convert_alpha()
            self.lesson_image = pygame.transform.smoothscale(self.lesson_image_original, (544, 260))

        #sound excerpts
        self.audio = excerptPlayer()
        self.excerpts = self.data.get("excerpts", [])
        self.excerpt_images = []
        
        for image_name in self.data.get("excerptImg", []):
            image_path = os.path.join(os.getcwd(), 'img', image_name)
            image_original = pygame.image.load(image_path).convert_alpha()
            image = pygame.transform.smoothscale(image_original, (501, 91))
            self.excerpt_images.append(image)
        
        for excerpt in self.excerpts:
            self.audio.load(excerpt, f"soundExcerpts/{excerpt}")
       
        self.excerpt_buttons = []

        self.excerpt_items = []

        for i, excerpt in enumerate(self.excerpts):

            button = Button(width*(0.52), height*(0.55) + i * 120, self.playButton, (50, 50), lambda e=excerpt: self.audio.play(e)) #lambda etc. makes sure each sound is played besides just the last one
            image = self.excerpt_images[i]
            self.excerpt_items.append({
                "button": button,
                "image": image,
            })

        self.metronome = None
        if self.data.get('metronome'):
            self.metronome = metronome((width*(0.72), height*(0.66)), (160,30), 120, 20, 200)

    def handle_event(self, event):
        for item in self.excerpt_items:
            item["button"].handle_event(event)

        if self.metronome:
            self.metronome.handle_event(event)
            
        return super().handle_event(event)
    
    def update(self):
        if self.metronome:
            self.metronome.update()

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
            if self.excerpt_items or self.metronome:
                self.screen.blit(self.lesson_image, (width/12, y + 5))
            else:
                lesson = self.data.get("order")
                if lesson == 7:
                    self.lesson_image = pygame.transform.smoothscale(self.lesson_image_original, (width*(0.8), height*(0.55)))
                    self.screen.blit(self.lesson_image, (width*(0.1), y-65))
                else:
                    self.lesson_image = pygame.transform.smoothscale(self.lesson_image_original, (width*(0.73), height*(0.40)))
                    self.screen.blit(self.lesson_image, (width/7, y + 5))

        #listening excerpts
        if self.excerpt_items:
            for item in self.excerpt_items:
                button = item["button"]
                image = item["image"]

                button.draw(self.screen)

                image_x = button.rect.x + 80
                image_y = button.rect.y - 20

                self.screen.blit(image, (image_x, image_y))

        if self.metronome:
            self.metronome.draw(self.screen)
        