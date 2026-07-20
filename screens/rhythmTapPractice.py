import os
import pygame
import random
from save import complete_lesson, load_save, save_recent_score , save_highest_score, save_rhythm_points
from startScreen import Button, textButton
from utils.text import wrap_text
from utils.config import width, height
from screens.baseScreen import baseScreen

class practiceScreen(baseScreen):
    def __init__(self, screen, step_data, runner, icons):
        super().__init__(screen, step_data, runner, icons)
        self.completed = False
        self.state = 'start'
        self.save = load_save()
        self.points = self.save.get("rhythm_practice_points", {}).get(self.data["title"], 0)
        self.level_passed = False
        self.level_text = None
        self.bpm = 60
        self.accuracy = 0 #for percentage
        self.accuracy_text = ''
        self.accuracy_colour = (0, 0, 0)
        self.difficulty = 'Easy'
        self.is_holding = False
        self.show_count = False
        self.font_big = pygame.font.Font('fonts/Vera.ttf', 30)

        self.beginButton = pygame.image.load(os.path.join(os.getcwd(),'img', 'buttons', 'begin_btn.png')).convert_alpha()
        self.begin_button = Button(width*(0.43), height/2, self.beginButton, (width*(0.14), height*(0.1)), self.generate_notes)
        self.tryAgainButton = pygame.image.load(os.path.join(os.getcwd(),'img', 'buttons', 'try_again_btn.png')).convert_alpha()
        self.try_again_button = Button(width*(0.28), height*(0.75), self.tryAgainButton, (width*(0.14), height*(0.1)), self.generate_notes)
        self.nextLevelButton = pygame.image.load(os.path.join(os.getcwd(),'img', 'buttons', 'next_button.png')).convert_alpha()
        self.next_level_button = Button(width*(0.60), height*(0.75), self.nextLevelButton, (width*(0.14), height*(0.1)), self.next_level)
        self.count_in_example_button = textButton("Click here for count in example", (width*(0.5), height*(0.7)), self.font, (0, 0, 0), (223, 73, 67), self.play_count_in_example)

        #load note and rest images
        og_crotchet_img = pygame.image.load(os.path.join(os.getcwd(),'img', 'crotchet.png')).convert_alpha()
        og_crotchet_rest_img = pygame.image.load(os.path.join(os.getcwd(),'img', 'crotchet_rest.png')).convert_alpha()
        og_quavers_img = pygame.image.load(os.path.join(os.getcwd(),'img', 'quavers.png')).convert_alpha()
        og_minim_img = pygame.image.load(os.path.join(os.getcwd(),'img', 'minim.png')).convert_alpha()
        og_minim_rest_img = pygame.image.load(os.path.join(os.getcwd(),'img', 'minim_rest.png')).convert_alpha()
        og_semibreve_img = pygame.image.load(os.path.join(os.getcwd(),'img', 'semibreve.png')).convert_alpha()
        og_semibreve_rest_img = pygame.image.load(os.path.join(os.getcwd(),'img', 'semibreve_rest.png')).convert_alpha()

        #resize images -> original image sizes were * by 0.75
        crotchet_img = pygame.transform.smoothscale(og_crotchet_img, (75, 150))
        crotchet_rest_img = pygame.transform.smoothscale(og_crotchet_rest_img, (75, 150))
        quavers_img = pygame.transform.smoothscale(og_quavers_img, (150, 150))
        minim_img = pygame.transform.smoothscale(og_minim_img, (113, 150))
        minim_rest_img = pygame.transform.smoothscale(og_minim_rest_img, (75, 150))
        semibreve_img = pygame.transform.smoothscale(og_semibreve_img, (120, 150))
        semibreve_rest_img = pygame.transform.smoothscale(og_semibreve_rest_img, (75, 150))

        #define notes in a nested dictionary
        self.note_definitions = {
            'crotchet' : {'image': crotchet_img, 'duration': 1.0, 'beats': 1, 'width' : 75},
            'crotchet_rest' : {'image': crotchet_rest_img, 'duration': 1.0, 'beats': 1, 'width' : 75},
            'quavers' : {'image': quavers_img, 'duration': 0.5, 'beats': 1, 'width' : 150},
            'minim' : {'image': minim_img, 'duration': 2.0, 'beats': 2, 'width' : 113},
            'minim_rest' : {'image': minim_rest_img, 'duration': 2.0, 'beats': 2, 'width' : 75},
            'semibreve' : {'image': semibreve_img, 'duration': 4.0, 'beats': 4, 'width' : 120},
            'semibreve_rest' : {'image': semibreve_rest_img, 'duration': 4.0, 'beats': 4, 'width' : 75},
        }

        #note sounds
        self.note_channel = pygame.mixer.Channel(0) #the space bar notes will be in channel 0 so it won't mix with other existing sounds
        self.note_sound = pygame.mixer.Sound('soundExcerpts/spacebar_note.mp3')
        self.count_in_channel = pygame.mixer.Channel(2)

        #player's initial scores
        self.perfect_count = 0
        self.good_count = 0
        self.miss_count = 0
        self.good_hold_count = 0
        self.bad_hold_count = 0

        #chart
        self.showing_chart = False
        self.show_chart = pygame.Rect(0, 0, width*(0.2), height*(0.05)) #rect for text
        self.show_chart_image = None
        if self.data.get("chart"):
            image_path = os.path.join(os.getcwd(), 'img', self.data["chart"])
            self.show_chart_image_original = pygame.image.load(image_path).convert_alpha()
            self.show_chart_image = pygame.transform.smoothscale(self.show_chart_image_original, (544, 260))

    def handle_event(self, event):
        if self.save['completed_lessons'].get(self.data['title'], False):
            new_screen = super().handle_event(event)
            if new_screen:
                return new_screen
        
        if self.state == 'start':
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for i, hitbox in enumerate(self.icon_hitbox):
                    if hitbox.collidepoint(mouse_pos):
                        return self.runner.go_to_level(i)
            new_screen = self.begin_button.handle_event(event)
            if new_screen:
                return new_screen
            new_screen = self.back_button.handle_event(event)
            if new_screen:
                return new_screen
            new_screen = self.home_button.handle_event(event)
            if new_screen:
                return new_screen
            new_screen = self.count_in_example_button.handle_event(event)
            if new_screen:
                return new_screen
            return None

        elif self.state == 'practice':
            new_screen = self.back_button.handle_event(event)
            if new_screen:
                return new_screen
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.note_channel.play(self.note_sound, loops=-1)
                if not self.active_notes[self.current_note]['is_rest']:
                    self.check_hit_start()
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                if not self.active_notes[self.current_note]['is_rest']:
                    self.check_hit_end()
                self.note_channel.stop()
            return None  #ignore all input by mouse and only take in input by space bar so user cannot reset the notes mid practice

        elif self.state == 'finished':
            new_screen = self.back_button.handle_event(event)
            if new_screen:
                return new_screen
            new_screen = self.try_again_button.handle_event(event)
            if new_screen:
                return new_screen
            new_screen = self.next_level_button.handle_event(event)
            if new_screen:
                return new_screen
            if self.completed:
                return self.next_button.handle_event(event)
            return None
        
        return super().handle_event(event)

    def play_count_in_example(self):
        self.count_start = pygame.time.get_ticks()
        self.show_count = True
        if pygame.mixer.get_busy():
            return
        count_in = pygame.mixer.Sound("soundExcerpts/60bpm.mp3")
        count_in.play(maxtime=4000)

    def check_hit_start(self):
        now = pygame.time.get_ticks() - self.timer_start
        expected = self.active_notes[self.current_note]["hit_time"]
        difference = abs(now - expected)
        self.press_time = now
        self.is_holding = True #flag for check_hit_end

        if difference <= 200:
            self.perfect_count += 1
            self.accuracy_text = "Perfect!"
            self.accuracy_colour = (0, 150, 0)
        elif difference <= 300:
            self.good_count += 1
            self.accuracy_text = "Good!"
            self.accuracy_colour = (130, 150, 0)
        else:
            self.miss_count += 1
            self.accuracy_text = "Miss"
            self.accuracy_colour = (150, 0, 0)

    def check_hit_end(self):
        if not self.is_holding: #don't check end time if a key has not been pressed initially
            return
        
        release_time = pygame.time.get_ticks() - self.timer_start
        held_time = release_time - self.press_time
        expected_hold = self.active_notes[self.current_note]["duration"] * self.ms_per_beat

        if abs(held_time - expected_hold) <= 650:
            self.good_hold_count += 1
            self.accuracy_text = "Good hold!"
            self.accuracy_colour = (0, 150, 0)
        else:
            self.bad_hold_count += 1
            self.accuracy_text = "Bad hold"
            self.accuracy_colour = (150, 0, 0)

        self.is_holding = False
        self.current_note += 1

        if self.current_note >= len(self.active_notes):
            self.finished_practice()

    def reset_scores(self):
        self.perfect_count = 0
        self.good_count = 0
        self.miss_count = 0
        self.good_hold_count = 0
        self.bad_hold_count = 0

    def next_level(self):
        if self.level_passed:
            self.points += 2
        
        save_rhythm_points(self.data['title'], self.points)

        if self.points > 5:
            self.completed = True
            return
        
        self.generate_notes()

    def display_count_in(self):
        if not self.show_count:
            return

        if self.state == 'start': #default 60bpm
            time = (pygame.time.get_ticks() - self.count_start) // 1000
            if time < 4:
                number = str(time + 1)
                counter = self.font_big.render(number, True, (0, 0, 0))
                self.screen.blit(counter, (width/2 - counter.get_width()/2, height*(0.25)))
        elif self.state == 'practice': #accounts for other bpm
            time = pygame.time.get_ticks() - self.count_start
            beat_length = 60000 / self.bpm  #milliseconds per beat
            beat = int(time // beat_length)
            if beat < 4:
                number = str(beat + 1)
                counter = self.font_big.render(number, True, (0, 0, 0))
                self.screen.blit(counter, (width/2 - counter.get_width()/2, height * 0.25))
        else:
            self.show_count = False

    def generate_notes(self):
        self.state = 'practice'
        self.draw_layout() #cover current text
        self.reset_scores()

        start_x = width*(0.15)
        y = height*(0.41)

        if self.points <= 1:
            self.difficulty = 'Easy'
            notes = self.data["notes_easy"] 
            num_notes = int(self.data["num_notes_easy"])
            self.bpm = self.data["bpm_easy"]
        elif self.points <= 3:
            self.difficulty = 'Medium'
            notes = self.data["notes_med"]
            num_notes = int(self.data["num_notes_med"])
            self.bpm = self.data["bpm_med"]
        else:
            self.difficulty = 'Hard'
            notes = self.data["notes_hard"]
            num_notes = int(self.data["num_notes_hard"])
            self.bpm = self.data["bpm_hard"]

        #4 beat count in at x bpm
        self.count_start = pygame.time.get_ticks()
        self.show_count = True
        self.ms_per_beat = 60000/self.bpm
        self.timer_start = pygame.time.get_ticks() + (4 * self.ms_per_beat)
        
        self.count_in = pygame.mixer.Sound(f"soundExcerpts/{self.bpm}bpm.mp3")
        self.count_in_channel.play(self.count_in, loops=0)

        self.current_note = 0

        self.level_text = self.font.render(f"Difficulty: {self.difficulty}", True, (0, 0, 0))
        displayed_notes = random.sample(notes, k=num_notes) #array of random notes
        self.active_notes = [] #empty array

        current_x = 0
        current_time = 0

        for note in displayed_notes:
            x = start_x + current_x

            self.active_notes.append({
                'image' : self.note_definitions[note]['image'],
                'position' : (x, y),
                'duration' : self.note_definitions[note]["duration"],
                'hit_time' : current_time,
                'is_rest' : 'rest' in note,
                'beats' : self.note_definitions[note]['beats'],
                'width' : self.note_definitions[note]['width'],
            })
            
            current_x += self.note_definitions[note]["width"]
            current_time += self.note_definitions[note]["duration"] * self.ms_per_beat

            if note == 'quavers': #since quavers are 2 consecutive beats with one image they need special consideration (gets added twice) 
                self.active_notes.append({
                'image' : None,
                'position' : None,
                'duration' : self.note_definitions[note]["duration"],
                'hit_time' : current_time,
                'is_rest' : "rest" in note,
                'beats' : 0,
                'width' : 0,
                })

                current_time += self.note_definitions[note]["duration"] * self.ms_per_beat
    
    def show_chart_text(self):
        self.show_chart.topleft = (width/2 - width*(0.2)/2, height*(0.91)) #rect position
        pygame.draw.rect(self.screen, (90, 90, 90), self.show_chart, border_radius=8)
        chart_text = self.font.render("Hover here to show chart", True, (255, 255, 255))
        chart_rect = chart_text.get_rect(center=self.show_chart.center)
        self.screen.blit(chart_text, chart_rect)

    def show_chart_img(self):
        image_rect = self.show_chart_image.get_rect(topleft=(width/2 - 544/2, height/2 - 260/2))
        self.screen.blit(self.show_chart_image, image_rect)
        pygame.draw.rect(self.screen, (0, 0, 0), image_rect, 1)
        #self.screen.blit(self.show_chart_image, (width/2 - 544/2, height/2 - 260/2)) #display chart in centre

    def update_screen(self):
        if self.state != "practice":
            return

        if self.current_note >= len(self.active_notes):
            return

        note = self.active_notes[self.current_note]

        if note["is_rest"]:
            self.accuracy_text = ''
            now = pygame.time.get_ticks() - self.timer_start
            end_time = note["hit_time"] + note["duration"] * self.ms_per_beat

            if now >= end_time:
                self.current_note += 1

                if self.current_note >= len(self.active_notes):
                    self.finished_practice()

    def finished_practice(self):
        self.accuracy = round((self.perfect_count + self.good_count + self.good_hold_count) / (self.perfect_count + self.good_count + self.good_hold_count + self.miss_count + self.bad_hold_count)*100)
        if self.accuracy >= 75: #can only pass if user gets 75% or over
            self.level_passed = True
        else:
            self.level_passed = False

        #save scores
        save_recent_score(self.data['title'], self.difficulty, self.accuracy)
        save_highest_score(self.data['title'], self.difficulty, self.accuracy)

        if self.points >= 4 and self.level_passed:
            self.completed = True
            complete_lesson(self.data["title"])
            self.save = load_save()

        self.state = 'finished'

    def draw_stave(self): #only for the last practice level
        #one line stave
        y = height/2 + 50
        pygame.draw.line(self.screen, (0,0,0), (width*(0.08), y), (width*(0.9), y), 3)

        #percussion cleff
        pygame.draw.line(self.screen, (0,0,0), (width*(0.08), y - 20), (width*(0.08), y + 20), 5)
        pygame.draw.line(self.screen, (0,0,0), (width*(0.08) + 10, y - 20), (width*(0.08) + 10, y + 20), 5)

        #time signature
        ts_font = pygame.font.Font('fonts/new_amsterdam/NewAmsterdam.ttf', 80)
        ts_text = ts_font.render("4", True, (0, 0, 0))
        self.screen.blit(ts_text, (width*(0.1), y - 90))
        self.screen.blit(ts_text, (width*(0.1), y))

        #bar lines
        beats = 0
        for note in self.active_notes:
            beats += note["beats"]
            if beats == 4:
                if note['position'] is not None: #needed cuz 2nd quaver's position is None
                    x = note["position"][0] + note["width"]
                    pygame.draw.line(self.screen, (0,0,0), (x, y - 50), (x, y + 40), 3)
                beats = 0
        #bpm
        bpm_text = self.font.render(f"Bpm = {self.bpm}", True, (0, 0, 0))
        self.screen.blit(bpm_text, (width*(0.08), height*(0.35)))

    def draw(self):
        self.draw_layout() #draw text
        self.update_screen()

        if self.state == 'start':
            line_width = width*(97/108)
            lines = wrap_text(self.data["text"], self.font, line_width)

            y = height/3
            for line in lines:
                text = self.font.render(line, True, (0, 0, 0))
                self.screen.blit(text, (width/18, y))
                y += 40
            
            self.begin_button.draw(self.screen)  

            if self.save['completed_lessons'].get(self.data['title'], False):
                self.next_button.draw(self.screen)

            if self.data['order'] == 3:
                self.count_in_example_button.draw(self.screen)

            if self.show_count:
                self.display_count_in()

        elif self.state == 'practice':
            if self.show_count:
                self.display_count_in()

            if self.level_text:
                self.screen.blit(self.level_text, (width*(0.8), height*(0.25)))

            if self.accuracy_text:
                text = self.font.render(self.accuracy_text, True, self.accuracy_colour)
                self.screen.blit(text, (width * 0.45, height * 0.25))
            
            if self.data['order'] == 10:
                self.draw_stave()

            for i, note in enumerate(self.active_notes):
                img = note["image"]
                pos = note["position"]
               
                if img is not None:
                    self.screen.blit(img, pos)

                if i == self.current_note and pos is not None:
                    pygame.draw.circle(self.screen, (255, 0, 0), (int(pos[0] + 50), int(pos[1] - 20)), 8)

        elif self.state == 'finished':
            self.count_in_channel.stop()

            if self.level_text:
                self.screen.blit(self.level_text, (width*(0.8), height*(0.25)))
            self.try_again_button.draw(self.screen)

            if not self.completed:
                self.next_level_button.draw(self.screen)
            else:
                self.next_button.draw(self.screen)
            title_font = pygame.font.Font('fonts/new_amsterdam/NewAmsterdam.ttf', 40)
            text_font = pygame.font.Font('fonts/new_amsterdam/NewAmsterdam.ttf', 35)

            self.accuracy_text = ''

            #define all text for score screen
            perfect_text = text_font.render("Perfect", True, (0, 150, 0))
            good_text = text_font.render("Good", True, (150, 150, 0))
            miss_text = text_font.render("Miss", True, (150, 0, 0))
            
            perfect_num = text_font.render(str(self.perfect_count), True, (0, 0, 0))
            good_num = text_font.render(str(self.good_count), True, (0, 0, 0))
            miss_num = text_font.render(str(self.miss_count), True, (0, 0, 0))
           
            good_hold_text = text_font.render("Good Hold", True, (0, 150, 0))
            bad_hold_text = text_font.render("Bad Hold", True, (150, 0, 0))
            
            good_hold_num = text_font.render(str(self.good_hold_count), True, (0, 0, 0))
            bad_hold_num = text_font.render(str(self.bad_hold_count), True, (0, 0, 0))
            
            speed_text = text_font.render("Speed:", True, (0, 0, 0))
            duration_text = text_font.render("Duration:", True, (0, 0, 0))
            score_text = title_font.render("Your Score", True, (0, 0, 0))

            #display text for score screen
            self.screen.blit(score_text, (width*(0.45), height*(0.25)))

            self.screen.blit(speed_text, (width*(0.1), height*(0.38)))
            self.screen.blit(perfect_text, (width*(1/4), height*(0.38)))
            self.screen.blit(good_text, (width*(2/4), height*(0.38)))
            self.screen.blit(miss_text, (width*(3/4), height*(0.38)))
            
            self.screen.blit(perfect_num, (width*(1/4), height*(0.43)))
            self.screen.blit(good_num, (width*(2/4), height*(0.43)))
            self.screen.blit(miss_num, (width*(3/4), height*(0.43)))

            self.screen.blit(duration_text, (width*(0.1), height*(0.58)))
            self.screen.blit(good_hold_text, (width*(1/3), height*(0.58)))
            self.screen.blit(bad_hold_text, (width*(2/3), height*(0.58)))
            
            self.screen.blit(good_hold_num, (width*(1/3), height*(0.63)))
            self.screen.blit(bad_hold_num, (width*(2/3), height*(0.63)))

            accuracy_text = text_font.render(f"Overall Accuracy: {self.accuracy}%", True, (0, 0, 0))
            self.screen.blit(accuracy_text, (width*(0.41), height*(0.7)))

            #chart
            if self.data.get("chart"):
                self.show_chart_text()
            mouse_pos = pygame.mouse.get_pos()
            self.showing_chart = self.show_chart.collidepoint(mouse_pos)
            if self.showing_chart:
                self.show_chart_img()