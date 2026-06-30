import os
import pygame
import random
from startScreen import Button
from utils.text import wrap_text
from utils.config import width, height
from utils.excerpts import excerptPlayer
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

        #note sounds
        self.note_channel = pygame.mixer.Channel(0) #the space bar notes will be in channel 0 so it won't mix with other existing sounds
        self.note_sound = pygame.mixer.Sound('soundExcerpts/spacebar_note.mp3')

    def handle_event(self, event):
        if self.show_notes == True:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.note_channel.play(self.note_sound, loops=-1)
                self.check_hit_start()
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                self.check_hit_end()
                self.note_channel.fadeout(150)
            return None  #ignore all input by mouse and only take in input by space bar so user cannot reset the notes mid practice

        new_screen = self.begin_button.handle_event(event)
        if new_screen:
            return new_screen
        
        return super().handle_event(event)

    def check_hit_start(self):
        now = pygame.time.get_ticks() - self.timer_start
        expected = self.active_notes[self.current_note]["hit_time"]
        difference = abs(now - expected)
        self.press_time = now
        self.is_holding = True #flag for check_hit_end

        if difference <= 100:
            print("Perfect!")
        elif difference <= 200:
            print("Good!")
        else:
            print("Miss")

        self.active_notes[self.current_note]["hit"] = True
   
    def check_hit_end(self):
        if not self.is_holding: #don't check end time if a key has not been pressed initially
            return
        
        release_time = pygame.time.get_ticks() - self.timer_start
        held_time = release_time - self.press_time
        expected_hold = self.active_notes[self.current_note]["duration"] * self.ms_per_beat

        if abs(held_time - expected_hold) <= 500:
            print('correct hold')
        else:
            print('bad hold')

        self.is_holding = False
        self.current_note += 1

    def show_next_button(self):
        return True
        #return self.completed

    def generate_notes(self):
        self.show_notes = True
        self.draw_layout() #cover current text
         
        #4 beat count in at 60 bpm
        count_in = pygame.mixer.Sound("soundExcerpts/60bpm.mp3")
        count_in.play()

        self.timer_start = pygame.time.get_ticks() + 4000
        self.current_note = 0

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

        current_time = 0
        self.ms_per_beat = 60000/self.data["bpm"] 

        for i, note in enumerate(displayed_notes):
            x = start_x + (i * space)
            #img = self.note_definitions[note]['image']
            #self.active_notes.append((img, (x, y)))

            self.active_notes.append({
                'image' : self.note_definitions[note]['image'],
                'position': (x, y),
                'duration' : self.note_definitions[note]["duration"],
                "hit_time": current_time,
                "hit": False,
            })

            current_time += self.note_definitions[note]["duration"] * self.ms_per_beat

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
            for i, note in enumerate(self.active_notes):
                img = note["image"]
                pos = note["position"]
                
                self.screen.blit(img, pos)

                if i == self.current_note:
                    pygame.draw.circle(self.screen, (255, 0, 0), (int(pos[0] + 50), int(pos[1] - 20)), 8)

