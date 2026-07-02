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
        #self.completed = False
        self.state = 'start'
        self.beginButton = pygame.image.load(os.path.join(os.getcwd(),'img', 'begin_btn.png')).convert_alpha()
        self.begin_button = Button(width*(31/72), height/2, self.beginButton, (width*(5/36), height*(1/10)), self.generate_notes)
        self.tryAgainButton = pygame.image.load(os.path.join(os.getcwd(),'img', 'try_again_btn.png')).convert_alpha()
        self.try_again_button = Button(width*(20/72), height*(4/5), self.tryAgainButton, (width*(5/36), height*(1/10)), self.generate_notes)
        self.nextLevelButton = pygame.image.load(os.path.join(os.getcwd(),'img', 'next_button.png')).convert_alpha()
        self.next_level_button = Button(width*(43/72), height*(4/5), self.nextLevelButton, (width*(5/36), height*(1/10)), self.generate_notes)

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

        #player's initial scores
        self.perfect_count = 0
        self.good_count = 0
        self.miss_count = 0
        self.good_hold_count = 0
        self.bad_hold_count = 0

    def handle_event(self, event):
        if self.state == 'start':
            new_screen = self.begin_button.handle_event(event)
            if new_screen:
                return new_screen
        
        elif self.state == 'practice':
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.note_channel.play(self.note_sound, loops=-1)
                self.check_hit_start()
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                self.check_hit_end()
                self.note_channel.fadeout(150)
            return None  #ignore all input by mouse and only take in input by space bar so user cannot reset the notes mid practice

        elif self.state == 'finished':
            new_screen = self.try_again_button.handle_event(event)
            if new_screen:
                return new_screen
            
            new_screen = self.next_level_button.handle_event(event)
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
            #write the text that displays the users accuracy
            self.perfect_count += 1
        elif difference <= 200:
            print("Good!")
            self.good_count += 1
        else:
            print("Miss")
            self.miss_count += 1

        self.active_notes[self.current_note]["hit"] = True
   
    def check_hit_end(self):
        if not self.is_holding: #don't check end time if a key has not been pressed initially
            return
        
        release_time = pygame.time.get_ticks() - self.timer_start
        held_time = release_time - self.press_time
        expected_hold = self.active_notes[self.current_note]["duration"] * self.ms_per_beat

        if abs(held_time - expected_hold) <= 500:
            print('Good hold')
            self.good_hold_count += 1
        else:
            print('Bad hold')
            self.bad_hold_count += 1

        self.is_holding = False
        self.current_note += 1

        if self.current_note >= len(self.active_notes):
            self.state = 'finished'

    def show_next_button(self):
        return True
        #return self.completed

    def generate_notes(self):
        self.state = 'practice'
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
        
        if self.state == 'start':
            line_width = width*(97/108)
            lines = wrap_text(self.data["text"], self.font, line_width)

            y = height/3
            for line in lines:
                text = self.font.render(line, True, (0, 0, 0))
                self.screen.blit(text, (width/18, y))
                y += 40

            self.begin_button.draw(self.screen)  
        elif self.state == 'practice':
            for i, note in enumerate(self.active_notes):
                img = note["image"]
                pos = note["position"]
                
                self.screen.blit(img, pos)

                if i == self.current_note:
                    pygame.draw.circle(self.screen, (255, 0, 0), (int(pos[0] + 50), int(pos[1] - 20)), 8)

        elif self.state == 'finished':
            self.try_again_button.draw(self.screen)
            self.next_level_button.draw(self.screen)

            perfect_text = self.font.render("Perfect", True, (0, 150, 0))
            good_text = self.font.render("Good", True, (0, 150, 0))
            miss_text = self.font.render("Miss", True, (0, 150, 0))
            
            perfect_num = self.font.render(str(self.perfect_count), True, (0, 150, 0))
            good_num = self.font.render(str(self.good_count), True, (0, 150, 0))
            miss_num = self.font.render(str(self.miss_count), True, (0, 150, 0))
           
            '''good_hold_text = self.font.render("Good Hold", True, (0, 150, 0))
            bad_hold_text = self.font.render("Bad Hold", True, (0, 150, 0))
            
            good_hold_num = self.font.render(str(self.good_hold_count), True, (0, 150, 0))
            bad_hold_num = self.font.renderstr(self.bad_hold_count), True, (0, 150, 0)
            
            speed_text = self.font.render("Speed:", True, (0, 0, 0))
            duration_text = self.font.render("Duration", True, (0, 0, 0))
            score_text = self.font.render("Your Score", True, (0, 0, 0))'''

            self.screen.blit(perfect_text, (width*(1/4), height/2))
            self.screen.blit(good_text, (width*(2/4), height/2))
            self.screen.blit(miss_text, (width*(3/4), height/2))
            
            self.screen.blit(perfect_num, (width*(1/4), height*(3/4)))
            self.screen.blit(good_num, (width*(2/4), height*(3/4)))
            self.screen.blit(miss_num, (width*(3/4), height*(3/4)))




