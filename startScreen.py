import pygame
from save import load_save, save_data, reset_user_progress
from levels.levelRunner import levelRunner
from levels.rhythmLevels import rhythmlevels
from levels.pitchLevels import pitchlevels
from utils.config import width, height, resource_path
from utils.icons import tint_icon
from utils.text import wrap_text

class mainScreen:
    def __init__(self, screen, icons):
        self.screen = screen
        self.icons = icons
        self.font = pygame.font.Font(resource_path('fonts/Vera.ttf'), 20)
        self.font_big = pygame.font.Font(resource_path('fonts/Vera.ttf'), 30)
        self.font_small = pygame.font.Font(resource_path('fonts/Vera.ttf'), 15)

        self.save = load_save()
        self.first_time = self.save["first_time"]

        self.open_progress = False
        self.confirm_reset = False
            
        #load images
        self.pitch_btn = pygame.image.load(resource_path('img/buttons/pitch_btn.png')).convert_alpha()
        self.rhythm_btn = pygame.image.load(resource_path('img/buttons/rhythm_btn.png')).convert_alpha()
        self.select_original = pygame.image.load(resource_path('img/select.png')).convert_alpha()
        self.logo_original = pygame.image.load(resource_path('img/logo.png')).convert_alpha()
        self.icon_meaning_img_original = pygame.image.load(resource_path('img/icon_details.png')).convert_alpha()
        self.progress_book_btn = pygame.image.load(resource_path('img/buttons/progress_book_btn.png')).convert_alpha()
        self.reset_btn = pygame.image.load(resource_path('img/buttons/reset_btn.png')).convert_alpha()

        #resize images
        self.select = pygame.transform.smoothscale(self.select_original, (width*(0.16), height*(0.08)))
        self.logo = pygame.transform.smoothscale(self.logo_original, (width*(0.43), height/4))
        self.icon_meaning_img = pygame.transform.smoothscale(self.icon_meaning_img_original, (width*(0.61), height*(0.20)))

        #define buttons
        self.pitch_button = Button(width*(5/9), height/2, self.pitch_btn, (width*(0.3), height/3), self.open_pitch_levels)
        self.rhythm_button = Button(width*(5/36), height/2, self.rhythm_btn, (width*(0.3), height/3), self.open_rhythm_levels)
        self.progress_button = Button(width*(0.94), height*(0.02), self.progress_book_btn, (width*(0.04), height*(0.07)), self.show_progress)
        self.reset_button = Button((width*(0.2)) + 30, height*(0.16) + 25, self.reset_btn, (width*(0.05), height*(0.03)), self.ask_reset)
        self.yes_button = textButton("Yes, reset game", (width*(0.4), height*(0.55)), self.font_small, (255, 255, 255), (255, 0, 0), self.reset_game)
        self.no_button = textButton("No, cancel", (width*(0.6), height*(0.55)), self.font_small, (255, 255, 255), (255, 0, 0), self.cancel_reset)

        self.exit_box = pygame.Rect(0, 0, 20, 20)

    def open_pitch_levels(self): #only works if last level of rhythm has been completed
        save = load_save()
        if save['completed_lessons'].get('Final Rhythm Practice', False): 
            runner = levelRunner(self.screen, pitchlevels, self.icons)
            return runner.get_current_screen()

    def open_rhythm_levels(self):
        runner = levelRunner(self.screen, rhythmlevels, self.icons)
        return runner.get_current_screen()
    
    def handle_event(self, event):
        if self.confirm_reset: #is first so no other events can be taken in unless the confirm question is answered
            new_screen = self.yes_button.handle_event(event)
            if new_screen:
                return new_screen

            self.no_button.handle_event(event)
            return None
        
        if self.open_progress:
            new_screen = self.reset_button.handle_event(event)
            if new_screen:
                return new_screen
        
        new_screen = self.pitch_button.handle_event(event)
        if new_screen:
            return new_screen

        new_screen = self.rhythm_button.handle_event(event)
        if new_screen:
            return new_screen
        
        new_screen = self.progress_button.handle_event(event)
        if new_screen:
            return new_screen
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.first_time and self.exit_box.collidepoint(event.pos): #once the welcome popup is closed, it saves the progress as a new game start (no longer first time opening home page)
                self.first_time = False
                data = load_save()
                data['first_time'] = False
                save_data(data)

                self.pitch_button.hover_enabled = True
                self.rhythm_button.hover_enabled = True
                self.pitch_button.click_enabled = True
                self.rhythm_button.click_enabled = True

            elif self.exit_box.collidepoint(event.pos):
                self.close_progress()

    def show_instructions(self):
        #black box background
        y = height/3
        box_width = width * 0.75
        box_height = height * 0.6
        black_box = pygame.Surface((box_width, box_height))
        black_box.fill((255, 0, 255))
        black_box.set_colorkey((255, 0, 255)) #makes this colour transparent
        pygame.draw.rect(black_box, (0, 0, 0), (0, 0, box_width, box_height), border_radius=15)
        black_box.set_alpha(220) #transparency
        self.screen.blit(black_box, (width/2 - box_width / 2, y))
        
        #X in the top right corner
        y += 20
        box_x = width / 2 - box_width / 2
        self.exit_box.topleft = (box_x + box_width - 40, y)
        pygame.draw.rect(self.screen, (200, 50, 50), self.exit_box, border_radius=5)

        x_text = self.font.render("X", True, (255, 255, 255))
        x_rect = x_text.get_rect(center=self.exit_box.center)
        self.screen.blit(x_text, x_rect)

        #text
        welcome_title = self.font_big.render("Welcome to Upbeat!", True, (255, 255, 255))
        welcome_text = (
        "Upbeat is a beginner friendly educational game that will help you learn about music theory! "
        "Please ensure your sound is turned ON and that you have access to a mouse / trackpad and keyboard. "
        "Your progress will be saved once you fully complete each level and will be indicated by the "
        "icons at the top of your screen (see example below).")
        
        text_x_start = width * (0.15)
        y += 10
        self.screen.blit(welcome_title, (text_x_start, y))
        y += 60

        line_width = width*(0.7)
        lines = wrap_text(welcome_text, self.font, line_width)

        for line in lines:
            text = self.font.render(line, True, (255, 255, 255))
            self.screen.blit(text, (text_x_start, y))
            y += 40

        #icon image
        self.screen.blit(self.icon_meaning_img, (width/2 - width*(0.61)/2, height*(0.7)))

    def show_progress(self):
        self.open_progress = True

        self.pitch_button.hover_enabled = False #section buttons don't work when the progress book is opened
        self.rhythm_button.hover_enabled = False

        self.pitch_button.click_enabled = False
        self.rhythm_button.click_enabled = False
    
    def close_progress(self):
        self.open_progress = False
        self.pitch_button.hover_enabled = True
        self.rhythm_button.hover_enabled = True

        self.pitch_button.click_enabled = True
        self.rhythm_button.click_enabled = True
    
    def display_progress(self):
        #box for showing game progress
        box_width = width * 0.6
        box_height = height * 0.68
        box_x = width/2 - box_width/2
        box_y = height/2 - box_height/2
        progress_box = pygame.Surface((box_width, box_height))
        progress_box.fill((255, 0, 255))
        progress_box.set_colorkey((255, 0, 255)) 
        pygame.draw.rect(progress_box, (0, 0, 0), (0, 0, box_width, box_height), border_radius=15)
        progress_box.set_alpha(220) 
        self.screen.blit(progress_box, (box_x, box_y))

        #text
        progress_title = self.font_big.render("Your Progress", True, (255, 255, 255))
        progress_subtitle = self.font.render("Rhythm Levels                                           Pitch Levels", True, (255, 255, 255))

        y = box_y + 25
        title_rect = progress_title.get_rect(midtop=(width/2, y))
        y += 45
        subtitle_rect = progress_subtitle.get_rect(midtop=(width/2, y))

        self.screen.blit(progress_title, title_rect)
        self.screen.blit(progress_subtitle, subtitle_rect)

        start_y = y + 40

        for level in rhythmlevels: #loop through rhythm levels
            self.save = load_save()
            if self.save['completed_lessons'].get(level['title'], False):
                progress_text = self.font_small.render(f'Level {level["order"]}: {level["title"]}', True, (255, 255, 255))
            else: 
                progress_text = self.font_small.render("?", True, (255, 255, 255))

            self.screen.blit(progress_text, (box_x + 30, start_y))
            start_y += 35

        start_y = y + 40

        for level in pitchlevels: #loop through pitch levels
            self.save = load_save()
            if self.save['completed_lessons'].get(level['title'], False):
                progress_text = self.font_small.render(f'Level {level["order"]}: {level["title"]}', True, (255, 255, 255))
            else: 
                progress_text = self.font_small.render("?", True, (255, 255, 255))

            self.screen.blit(progress_text, (width/2 + 30, start_y))
            start_y += 35
        
        #X in the top right corner
        y = box_y + 25
        self.exit_box.topleft = (box_x + box_width - 40, y)
        pygame.draw.rect(self.screen, (200, 50, 50), self.exit_box, border_radius=5)

        x_text = self.font.render("X", True, (255, 255, 255))
        x_rect = x_text.get_rect(center=self.exit_box.center)
        self.screen.blit(x_text, x_rect)

        #reset in the top left corner
        self.reset_button.draw(self.screen)

    def ask_reset(self):
        self.confirm_reset = True
    
    def draw_reset_confirmation(self):
        box_width = width * 0.5
        box_height = height * 0.25
        box = pygame.Surface((box_width, box_height))
        box.fill((0, 0, 0))
        pygame.draw.rect(box, (255, 255, 255), box.get_rect(), 3, border_radius=15)
        self.screen.blit(box, (width/2 - box_width/2, height/2 - box_height/2))

        text = self.font.render("Are you sure you want to reset all your progress?", True, (255, 255, 255))
        note = self.font_small.render("NOTE: This action cannot be undone.", True, (255, 0, 0))

        self.screen.blit(text, (width/2 - text.get_width()/2, height/2 - 50))
        self.screen.blit(note, (width/2 - note.get_width()/2, height/2 - 10))
        self.yes_button.draw(self.screen)
        self.no_button.draw(self.screen)  

    def reset_game(self): #full reset of entire game progress
        reset_user_progress()
        self.confirm_reset = False

        self.save = load_save()

        self.first_time = True
        self.open_progress = False

    def cancel_reset(self):
        self.confirm_reset = False

    def draw(self):
        save = load_save()
        self.pitch_button.enabled = save["completed_lessons"].get("Final Rhythm Practice", False)

        self.screen.blit(self.logo, (width/2 - width*(0.43)/2, height*(0.075)))
        self.screen.blit(self.select, (width/2 - width*(0.16)/2, height*(0.39)))

        self.pitch_button.draw(self.screen)
        self.rhythm_button.draw(self.screen)
        self.progress_button.draw(self.screen)

        if self.first_time:
            self.show_instructions()
        else:
            if self.open_progress:
                self.display_progress()

            if self.confirm_reset:
                self.draw_reset_confirmation()

class Button:
    def __init__(self, x, y, image, size, action=None):
        self.original = image
        self.normal = pygame.transform.smoothscale(image, size)
        self.rect = self.normal.get_rect(topleft=(x, y))
        
        hover_size = (int(size[0]*1.1), int(size[1]*1.1)) #image gets bigger when mouse is hovering over
        self.hover = pygame.transform.smoothscale(image, hover_size)
        self.hover_rect = self.hover.get_rect(center=self.rect.center)

        self.sfx = pygame.mixer.Sound(resource_path('soundExcerpts/sfx/button_click_sfx.mp3'))

        self.action = action
        self.enabled = True
        self.disabled = self.normal.copy()
        self.hover_enabled = True
        self.click_enabled = True
    
    def draw(self, screen):
            mouse_pos = pygame.mouse.get_pos()

            if not self.enabled: #used for pitch levels when rhythm is sitll being completed
                self.disabled = tint_icon(self.normal.copy(), (120, 120, 120))
                screen.blit(self.disabled, self.rect)
            elif self.hover_enabled and self.rect.collidepoint(mouse_pos):
                screen.blit(self.hover, self.hover_rect)
            else:
                screen.blit(self.normal, self.rect)

    def handle_event(self, event):
        if not self.enabled:
            return None

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.click_enabled:
                    if self.action:
                        self.sfx.play()
                        return self.action()

class textButton:
    def __init__(self, text, position : tuple, font, normalColour, hoverColour, action=None):
        self.text = text
        self.font = font
        self.action = action

        self.normal_colour = normalColour
        self.hover_colour = hoverColour #colour of text changes when mouse is hovering

        self.rect = pygame.Rect(0, 0, 0, 0)
        self.rect.center = position

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            colour = self.hover_colour
        else:
            colour = self.normal_colour

        text_surface = self.font.render(self.text, True, colour)
        self.rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    return self.action()