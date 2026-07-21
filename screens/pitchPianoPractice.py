import pygame
from piano.piano import Piano
from save import complete_lesson, load_save
from startScreen import Button
from utils.text import wrap_text
from utils.config import width, height, resource_path
from screens.baseScreen import baseScreen

class practiceScreen(baseScreen):
    def __init__(self, screen, step_data, runner, icons):
        super().__init__(screen, step_data, runner, icons)
        self.completed = False
        self.state = 'start'
        self.piano = Piano(screen, (8 * 40), 300, (width*(0.57), height*(0.4)))
        self.save = load_save()
        self.toggle_assist = False
        self.sheetMusic_display = None

        self.expected_notes = self.data["expectedKeys"]
        self.current_index = 0
        self.current_bar = 0
        self.feedback = ''
        self.feedback_colour = (0, 0, 0)
        self.feedback_time = pygame.time.get_ticks()

        #load images / buttons
        self.beginButton = pygame.image.load(resource_path('img/buttons/begin_btn.png')).convert_alpha()
        self.assistON_btn = pygame.image.load(resource_path('img/buttons/assistON_btn.png')).convert_alpha()
        self.assistOFF_btn = pygame.image.load(resource_path('img/buttons/assistOFF_btn.png')).convert_alpha()
        self.resetbtn = pygame.image.load(resource_path('img/buttons/reset_btn.png')).convert_alpha()
        self.keyboard_img_original = pygame.image.load(resource_path('img/keyboard_piano.png')).convert_alpha()

        self.begin_button = Button(width*(31/72), height/2, self.beginButton, (width*(5/36), height*(1/10)), self.set_state_practice)
        self.reset_btn = Button(width*(0.83), height*(0.07), self.resetbtn, (width*(0.1), height*(0.05)), self.reset_progress)

        self.update_assist_btn()

    def handle_event(self, event):
        if self.save['completed_lessons'].get(self.data['title'], False): #all buttons work after level is already completed
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
            new_screen = self.home_button.handle_event(event)
            if new_screen:
                return new_screen
            new_screen = self.back_button.handle_event(event)
            if new_screen:
                return new_screen
            return None

        elif self.state == 'practice':
            self.piano.handle_event(event)
            new_screen = self.assist_btn.handle_event(event)
            if new_screen:
                return new_screen
            new_screen = self.reset_btn.handle_event(event)
            if new_screen:
                return new_screen
            new_screen = self.back_button.handle_event(event)
            if new_screen:
                return new_screen
                        
        elif self.state == 'finished':
            self.piano.handle_event(event)
        
        return None
    
    def set_state_practice(self):
        self.state = 'practice'
    
    def update_assist_btn(self):
        if self.toggle_assist == False:
            assist_btn_image = self.assistOFF_btn
            assist_btn_action = self.assist_on
            image_path = resource_path(f'img/sheetMusic/{self.data["sheetMusic"]}')
        else:
            assist_btn_image = self.assistON_btn
            assist_btn_action = self.assist_off
            image_path = resource_path(f'img/sheetMusic/{self.data["sheetMusic_assist"]}')

        self.assist_btn = Button(width*(0.83), height*(0.13), assist_btn_image, (width*(0.1), height*(0.05)), assist_btn_action)
        self.sheetMusic_original = pygame.image.load(image_path).convert_alpha()
        self.sheetMusic_display = pygame.transform.smoothscale(self.sheetMusic_original, (600, 340))

    def assist_on(self):
        self.toggle_assist = True
        self.update_assist_btn()

    def assist_off(self):
        self.toggle_assist = False
        self.update_assist_btn()

    def update_feedback(self):
        played_note = self.piano.get_current_note()

        if played_note is not None and self.state == 'practice':
            expected = self.expected_notes[self.current_index]
            if played_note == expected:
                self.current_index += 1
                if self.current_index >= len(self.expected_notes):
                    self.feedback = "Finished!"
                    self.feedback_colour = (0, 150, 0)
                    self.feedback_time = pygame.time.get_ticks()
                    return
                self.feedback = "Correct!"
                self.feedback_colour = (0, 150, 0)
                self.feedback_time = pygame.time.get_ticks()
            else:
                self.feedback = "Try Again"
                self.feedback_colour = (150, 0, 0)
                self.feedback_time = pygame.time.get_ticks()
        else:
            return
    
    def show_bar_num(self): #if assist is on, it shows the user what bar they are up to in case they are struggling
        total_beats = 0
        self.bar = 1
        for beats_in_bar in self.data['barLength']:
            total_beats += beats_in_bar
            if self.current_index < total_beats:
                break
            self.bar += 1

        if self.bar > len(self.data['barLength']):
            self.bar = len(self.data['barLength'])
        return self.bar
    
    def reset_progress(self): #if user forgets where they are or want to start from the beginning they can reset
        self.current_index = 0
        self.bar = 1

        self.feedback = ""
        self.feedback_colour = (0, 0, 0)
        self.feedback_time = 0

    def draw(self):
        self.draw_layout()
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

            img_width = width * (0.5)
            self.keyboard_img = pygame.transform.smoothscale(self.keyboard_img_original, (img_width, height*(0.2)))
            self.screen.blit(self.keyboard_img, (width/2 - img_width/2, height*(0.63)))

        else: #state == practice or finished
            self.piano.draw_piano()
            self.assist_btn.draw(self.screen)
            self.reset_btn.draw(self.screen)
            self.update_feedback()

            self.screen.blit(self.sheetMusic_display, (width*(0.08), height*(0.35)))

            img_width = width * (1/3)
            self.keyboard_img = pygame.transform.smoothscale(self.keyboard_img_original, (img_width, height*(0.14)))

            self.screen.blit(self.keyboard_img, (width*(0.57), height*(0.24)))

            if self.feedback:
                if pygame.time.get_ticks() - self.feedback_time < 500: #text shows for 0.5sec
                    colour = self.feedback_colour
                    text = self.font.render(self.feedback, True, colour)
                    self.screen.blit(text, (width*(0.47), height*(0.9)))

                    if self.feedback == 'Finished!':
                        pygame.time.delay(1000)
                        self.state = 'finished'
            
            if self.toggle_assist:
                bar_font = pygame.font.Font(resource_path('fonts/Vera.ttf'), 14)
                bar_num = self.show_bar_num()
                text = bar_font.render(f"You are up to Bar:{bar_num}", True, (0, 0, 0))
                self.screen.blit(text, (width*(0.08), height*(0.33)))
        
            if self.state == 'finished': #client requested for different affirmations at the end of each practice level
                finish_font = pygame.font.Font(resource_path('fonts/Vera.ttf'), 25)
                if self.data['order'] == 7:
                    text = finish_font.render("Great Job! You're a Star!", True, (0, 0, 0))
                    pos = (width*(0.4), height*(0.91))
                if self.data['order'] == 8:
                    text = finish_font.render("Wonderful Effort! You're amazing!", True, (0, 0, 0))
                    pos = (width*(0.35), height*(0.91))
                if self.data['order'] == 9:
                    text = finish_font.render("Fantastic! You're awesome!", True, (0, 0, 0))
                    pos = (width*(0.39), height*(0.91))
                self.screen.blit(text, (pos))

                complete_lesson(self.data["title"])
                self.save = load_save()