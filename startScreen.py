import os
import pygame
from save import load_save, save_data
from levels.levelRunner import levelRunner
from utils.config import width, height
from utils.icons import tint_icon
from utils.text import wrap_text

class mainScreen:
    def __init__(self, screen, icons):
        self.screen = screen
        self.icons = icons
        current_dir = os.getcwd()
        self.font = pygame.font.Font('fonts/Vera.ttf', 20)
        self.font_big = pygame.font.Font('fonts/Vera.ttf', 30)

        save = load_save()
        self.first_time = save["first_time"]
            
        #load images
        self.pitch_btn = pygame.image.load(os.path.join(current_dir, 'img', 'buttons', 'pitch_btn.png')).convert_alpha()
        self.rhythm_btn = pygame.image.load(os.path.join(current_dir, 'img', 'buttons', 'rhythm_btn.png')).convert_alpha()
        self.select_original = pygame.image.load(os.path.join(current_dir, 'img', 'select.png')).convert_alpha()
        self.logo_original = pygame.image.load(os.path.join(current_dir, 'img', 'logo.png')).convert_alpha()
        self.icon_meaning_img_original = pygame.image.load(os.path.join(current_dir, 'img', 'icon_details.png')).convert_alpha()
        self.progress_book_btn = pygame.image.load(os.path.join(current_dir, 'img', 'buttons', 'progress_book_btn.png')).convert_alpha()

        #resize images
        self.select = pygame.transform.smoothscale(self.select_original, (width*(0.16), height*(0.08)))
        self.logo = pygame.transform.smoothscale(self.logo_original, (width*(0.43), height/4))
        self.icon_meaning_img = pygame.transform.smoothscale(self.icon_meaning_img_original, (width*(0.61), height*(0.20)))

        #define buttons
        self.pitch_button = Button(width*(5/9), height/2, self.pitch_btn, (width*(0.3), height/3), self.open_pitch_levels)
        self.rhythm_button = Button(width*(5/36), height/2, self.rhythm_btn, (width*(0.3), height/3), self.open_rhythm_levels)
        self.progress_button = Button(width*(0.94), height*(0.02), self.progress_book_btn, (width*(0.04), height*(0.07)), self.show_progress)

        self.exit_box = pygame.Rect(0, 0, 20, 20)

    #filler functions for now
    def open_pitch_levels(self):
        save = load_save()
        if save['completed_lessons'].get('Final Rhythm Practice', False):
            from levels.pitchLevels import pitchlevels
            runner = levelRunner(self.screen, pitchlevels, self.icons)
            return runner.get_current_screen()
        else:
            print("Must complete rhythm section")

    def open_rhythm_levels(self):
        from levels.rhythmLevels import levels
        runner = levelRunner(self.screen, levels, self.icons)
        return runner.get_current_screen()
    
    def handle_event(self, event):
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
            if self.first_time and self.exit_box.collidepoint(event.pos):
                self.first_time = False
                data = load_save()
                data['first_time'] = False
                save_data(data)

    def show_instructions(self):
        #black box background
        y = height/3
        box_width = width * 0.75
        black_box = pygame.Surface((box_width, height * 0.6))
        black_box.fill((255, 0, 255))
        black_box.set_colorkey((255, 0, 255)) 
        pygame.draw.rect(black_box, (0, 0, 0), (0, 0, box_width, height * 0.6), border_radius=15)
        black_box.set_alpha(220) 
        self.screen.blit(black_box, (width/2 - box_width / 2, y))
        
        #X in the corner
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
        "Note: Your progress will be saved once you fully complete each level and will be indicated by the "
        "icons at the top of your screen.")
        
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
        print('PROGESS')

    def reset_game(self):
        pass
        #reset everything in the json file and starts from the very beginning including show_instructions
        #data['first_time'] = True

    def draw(self):
            save = load_save()
            self.pitch_button.enabled = save["completed_lessons"].get("Final Rhythm Practice", False)

            self.screen.blit(self.logo, (width/2 - width*(0.43)/2, height*(0.075)))
            self.screen.blit(self.select, (width/2 - width*(0.16)/2, height*(0.39)))

            self.pitch_button.draw(self.screen)
            self.rhythm_button.draw(self.screen)
            self.progress_button.draw(self.screen)

            if self.first_time == True:
                self.show_instructions()

class Button:
    def __init__(self, x, y, image, size, action=None):
        self.original = image
        self.normal = pygame.transform.smoothscale(image, size)
        self.sfx = pygame.mixer.Sound('soundExcerpts/sfx/button_click_sfx.mp3')

        hover_size = (int(size[0]*1.1), int(size[1]*1.1))
        self.hover = pygame.transform.smoothscale(image, hover_size)

        self.rect = self.normal.get_rect(topleft=(x, y))
        self.hover_rect = self.hover.get_rect(center=self.rect.center)

        self.action = action
        self.enabled = True
        self.disabled = self.normal.copy()
    
    def draw(self, screen):
            mouse_pos = pygame.mouse.get_pos()

            if not self.enabled:
                self.disabled = tint_icon(self.normal.copy(), (120, 120, 120))
                screen.blit(self.disabled, self.rect)
            elif self.rect.collidepoint(mouse_pos):
                screen.blit(self.hover, self.hover_rect)
            else:
                screen.blit(self.normal, self.rect)

    def handle_event(self, event):
        if not self.enabled:
            return None

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.sfx.play()
                    return self.action()