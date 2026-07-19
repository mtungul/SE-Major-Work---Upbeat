import os
import pygame
from save import load_save
from startScreen import Button, mainScreen
from utils.icons import tint_icon 
from utils.config import width, height

class baseScreen:
    def __init__(self, screen, step_data, runner, icons):
        self.screen = screen
        self.font = pygame.font.Font('fonts/Vera.ttf', 20)
        self.data = step_data
        self.runner = runner
        self.icons = icons
        self.icon_hitbox = []
        self.save = load_save()

        #load and size buttons
        self.nextButton = pygame.image.load(os.path.join(os.getcwd(),'img', 'buttons', 'next_button.png')).convert_alpha()
        self.backButton = pygame.image.load(os.path.join(os.getcwd(),'img', 'buttons', 'back_button.png')).convert_alpha()
        self.next_button = Button(width*(0.79), height*(0.88), self.nextButton, (width*(0.14), height*(0.1)), self.go_next)
        self.back_button = Button(width*(0.06), height*(0.88), self.backButton, (width*(0.14), height*(0.1)), self.go_back)
        
        self.backHomeButton = pygame.image.load(os.path.join(os.getcwd(),'img', 'buttons', 'back_to_home.png')).convert_alpha()
        self.back_home_button = Button(width*(0.72), height*(0.89), self.backHomeButton, (width*(0.21), height*(0.085)), lambda: mainScreen(self.screen, self.icons))
        self.homeBtn = pygame.image.load(os.path.join(os.getcwd(),'img', 'buttons', 'home.png')).convert_alpha()
        self.home_button = Button(width*(0.94), height*(0.01), self.homeBtn, (width*(0.05), height*(0.09)), lambda: mainScreen(self.screen, self.icons))

        self.finish_section_sfx = pygame.mixer.Sound('soundExcerpts/sfx/section_complete_sfx.mp3')

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos #stores where player clicked

            for i, hitbox in enumerate(self.icon_hitbox):
                if hitbox.collidepoint(mouse_pos):

                    return self.runner.go_to_level(i)
        new_screen = self.next_button.handle_event(event)
        if new_screen:
            return new_screen

        if self.runner.index != 0:
            new_screen = self.back_button.handle_event(event)
            if new_screen:
                return new_screen
        
        new_screen = self.back_home_button.handle_event(event)
        if new_screen:
            return new_screen
        
        new_screen = self.home_button.handle_event(event)
        if new_screen:
            return new_screen
        
    def draw_icon_row(self): #draws the row of icons at the top of the screen
        start_x = width*(2/27)
        y = height/10
        spacing = 106
        self.icon_hitbox = []

        for i in range(len(self.runner.steps)):
            x = start_x + i * spacing

            step = self.runner.steps[i]
            icon_name = step["icon"]

            if step["section"] == "rhythm":
                icon = self.icons.rhythm_icons[icon_name]
            else:
                icon = self.icons.pitch_icons[icon_name]

            if i == self.runner.index: 
                icon = tint_icon(icon, (255, 255, 255)) #current level
            elif self.runner.completed[i]:
                icon = tint_icon(icon, (215, 215, 215)) #completed levels
            else:
                icon = tint_icon(icon, (120, 120, 120)) #haven't completed yet

            hitbox = icon.get_rect(center=(x, y))
            self.icon_hitbox.append(hitbox)
            self.screen.blit(icon, hitbox)

    def go_next(self):
        return self.runner.next_level()
    
    def go_back(self):
        return self.runner.back_level()

    def draw_layout(self):
        self.draw_icon_row()
                                    #numbers = colour (3), position (2), size(2)   
        pygame.draw.rect(self.screen, (255, 255, 255), (width/27, height*(5/24), width*(25/27), height*(2/3)), border_radius=20) 
        
        #draw title
        title_font = pygame.font.Font('fonts/new_amsterdam/NewAmsterdam.ttf', 40)
        title = title_font.render(self.data["title"], True, (0, 0, 0))
        self.screen.blit(title, (width/18, height*(7/30)))

        #next and back buttons  +  'back to home' button after last level of section + show recent and highest score
        if (self.data['order'] == 11 and self.data['section'] == 'rhythm') or (self.data['order'] == 9 and self.data['section'] == 'pitch'):
            if self.finish_section_sfx:
                self.finish_section_sfx.play()
            self.finish_section_sfx = None

            #show most recent scores
            score_title_font = pygame.font.Font('fonts/new_amsterdam/NewAmsterdam.ttf', 40)
            score_font = pygame.font.Font('fonts/new_amsterdam/NewAmsterdam.ttf', 30)

            x_left = width * 0.07
            x_centre = width * 0.28
            x_right = width * 0.65
            y = height * 0.46

            #titles (row 1)
            practice_text = score_title_font.render("Practice Level:", True, (0, 0, 0))
            recent_text = score_title_font.render("Your Recent Scores:", True, (0, 0, 0))
            highest_text = score_title_font.render("Your Highest Scores:", True, (0, 0, 0))

            self.screen.blit(practice_text, (x_left, y))
            self.screen.blit(recent_text, (x_centre, y))
            self.screen.blit(highest_text, (x_right, y))

            #left column
            y_start = y + 60
            lesson_names = ['Note Values', 'Rest Note Values', 'Time Signature', 'Final']

            for lesson in lesson_names:
                lesson_name_text = score_font.render(f'{lesson}', True, (0, 0, 0))
                self.screen.blit(lesson_name_text, (x_left, y_start))
                y_start += 50
            
            #recent scores
            y_start = y + 60
            for lesson_name, difficulties in self.save['most_recent_score'].items(): #cycle through levels - format: ('title', {'difficulty': int, x3})
                for difficulty, score in difficulties.items(): #cycle through difficulties
                    if difficulty == 'Easy': 
                        colour = (0, 150, 0)
                    elif difficulty == 'Medium':
                        colour = (200, 140, 0)
                    elif difficulty == 'Hard':
                        colour = (150, 0 ,0)
                    else:
                        colour = (20, 20, 20)
                    score_text = score_font.render(f'{difficulty}: {score}', True, colour)
                    self.screen.blit(score_text, (x_centre, y_start))
                    x_centre += 150

                y_start += 50
                x_centre = width * 0.28
            
            #highest scores
            y_start = y + 60
            for lesson_name, difficulties in self.save['highest_score'].items(): #cycle through levels - format: ('title', {'difficulty': int, x3})
                for difficulty, score in difficulties.items(): #cycle through difficulties
                    if difficulty == 'Easy': 
                        colour = (0, 150, 0)
                    elif difficulty == 'Medium':
                        colour = (200, 140, 0)
                    elif difficulty == 'Hard':
                        colour = (150, 0 ,0)
                    else:
                        colour = (20, 20, 20)
                    score_text = score_font.render(f'{difficulty}: {score}', True, colour)
                    self.screen.blit(score_text, (x_right, y_start))
                    x_right += 150

                y_start += 50
                x_right = width * 0.65

            self.back_home_button.draw(self.screen)  
        else:
            self.next_button.draw(self.screen)  

        if self.runner.index != 0:
            self.back_button.draw(self.screen)

        #home button
        self.home_button.draw(self.screen)