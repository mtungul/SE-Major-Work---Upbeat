import os
import pygame
import random
from utils.text import wrap_text
from utils.config import width, height
from startScreen import Button
from screens.baseScreen import baseScreen

class practiceScreen(baseScreen):
    def __init__(self, screen, step_data, runner, icons):
        super().__init__(screen, step_data, runner, icons)
        self.show_notes = False
        #self.completed = False
        self.beginButton = pygame.image.load(os.path.join(os.getcwd(),'img', 'begin_btn.png')).convert_alpha()
        self.begin_button = Button(width*(31/72), height/2, self.beginButton, (width*(5/36), height*(1/10)), self.generate_notes)

        #load and resize note and rest images
        crotchet_img = pygame.image.load(os.path.join(os.getcwd(),'img', 'crotchet.png')).convert_alpha()
        crotchet_rest_img = pygame.image.load(os.path.join(os.getcwd(),'img', 'crotchet_rest.png')).convert_alpha()
        quavers_img = pygame.image.load(os.path.join(os.getcwd(),'img', 'quavers.png')).convert_alpha()
        minim_img = pygame.image.load(os.path.join(os.getcwd(),'img', 'minim.png')).convert_alpha()
        minim_rest_img = pygame.image.load(os.path.join(os.getcwd(),'img', 'minim_rest.png')).convert_alpha()
        semibreve_img = pygame.image.load(os.path.join(os.getcwd(),'img', 'semibreve.png')).convert_alpha()
        semibreve_rest_img = pygame.image.load(os.path.join(os.getcwd(),'img', 'semibreve_rest.png')).convert_alpha()
        
        #crotchet_img = pygame.transform.smoothscale(crotchet_img_original, (100, 200))
       # minim_img = pygame.transform.smoothscale(minim_img_original, (140, 200))


        #define notes in a nested dictionary
        self.note_definitions = {
            'crotchet' : {'image': crotchet_img, 'duration': 1.0},
            'crotchet_rest' : {'image': crotchet_rest_img, 'duration': 1.0},
            'quavers' : {'image': quavers_img, 'duration': 1.0},
            'minim' : {'image': minim_img, 'duration': 2.0},
            'minim_rest' : {'image': minim_rest_img, 'duration': 2.0},
            'semibreve' : {'image': semibreve_img, 'duration': 4.0},
            'semibreve_rest' : {'image': semibreve_rest_img, 'duration': 4.0},
        }
    
    def handle_event(self, event):
        new_screen = self.begin_button.handle_event(event)
        if new_screen:
            return new_screen
        
        return super().handle_event(event)
    def show_next_button(self):
        return True
        #return self.completed

    def generate_notes(self):
        self.draw_layout() #cover current text
        
        #add 4 beat count in at 80 bpm

        start_x = width/8
        space = 180
        y = height/2

        points = 0 #may need to move this later
        if points in [0, 1]:
            notes = self.data["notes_easy"] 
            num_notes = int(self.data["num_notes_easy"])
        elif points in [2, 3]:
            notes = self.data["notes_med"]
            num_notes = int(self.data["num_notes_med"])
        elif points in [4, 5]:
            start_x = width/12
            space = 170
            notes = self.data["notes_hard"]
            num_notes = int(self.data["num_notes_hard"])

        displayed_notes = random.sample(notes, k=num_notes) #array of random notes
        self.active_notes = [] #empty array

        for i, note in enumerate(displayed_notes):
            x = start_x + (i * space)
            img = self.note_definitions[note]['image']
            self.active_notes.append((img, (x, y)))
        
        self.show_notes = True

    def draw(self):
        self.draw_layout() #draw text
        
        if not self.show_notes:
            line_width = width*(97/108)
            lines = wrap_text(self.data["text"], self.font, line_width)

            y = height/3
            for line in lines:
                text = self.font.render(line, True, (0, 0, 0))
                self.screen.blit(text, (width/18, y))
                y += 40

            self.begin_button.draw(self.screen)  
        else:
            for img, position in self.active_notes:
                self.screen.blit(img, position)

