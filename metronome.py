import time
import pygame
from utils.config import width, height

class metronome: 
    def __init__(self, pos: tuple, size: tuple, initial_bpm: float, min: int, max: int):
        self.pos = pos
        self.size = size
        self.grabbed = False

        self.slider_left_pos = self.pos[0] - (size[0]//2)
        self.slider_right_pos = self.pos[0] + (size[0]//2)
        self.slider_top_pos = self.pos[1] - (size[1]//2)

        self.min = min
        self.max = max

        value_range = max - min
        percentage = (initial_bpm - min) / value_range
        slider_width = self.slider_right_pos - self.slider_left_pos
        self.initial_val = slider_width * percentage 

        self.bpm_average = initial_bpm
        self.is_playing = False

        self._last_update = time.time()
        self._elapsed_time = 0.0
        self._last_closeness = 1.0

        self.on_beat = 0 #time since last beat
        self.beat_num = 0 #counter of beats
        self.started_beat = 0
        self.finished_beat = 0 

        self.container_rect = pygame.Rect(self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1])
        self.button_rect = pygame.Rect(self.slider_left_pos + self.initial_val - 5, self.slider_top_pos, 10, self.size[1])
        self.rect = pygame.Rect(0, 0, self.size[0] + 200, 220)
        self.rect.center = self.pos
        self.font = pygame.font.Font('fonts/Vera.ttf', 20)
        self.small_font = pygame.font.Font('fonts/Vera.ttf', 14)
        self.click_sound = pygame.mixer.Sound('soundExcerpts/metronome_click.wav')

        #buttons
        self.btn_play = pygame.Rect(self.rect.x + (self.rect.width // 2) - 50, self.rect.y + self.rect.height - 60, 100, 35)
        self.btn_minus = pygame.Rect(self.rect.x + 30, self.slider_top_pos, 40, 40)
        self.btn_plus = pygame.Rect(self.rect.x + self.rect.width - 70, self.slider_top_pos, 40, 40)
    
    def move_slider(self, mouse_pos):
        pos = mouse_pos[0]
        if pos < self.slider_left_pos:
            pos = self.slider_left_pos
        if pos > self.slider_right_pos:
            pos = self.slider_right_pos
        self.button_rect.centerx = pos
        
        self.bpm_average = self.get_value()
    
    def get_value(self):
        val_range = self.slider_right_pos - self.slider_left_pos
        button_val = self.button_rect.centerx - self.slider_left_pos

        return (button_val/val_range)*(self.max-self.min)+self.min

    def update(self):
        the_time = time.time()
        self._elapsed_time += the_time - self._last_update
        self._last_update = the_time

        space_between_beats = 60.0 / self.bpm_average
        since_last_beat = the_time - self.on_beat

        self.finished_beat = self.on_beat and (since_last_beat > 0.1)
        if self.finished_beat:
            self.on_beat = 0

        closeness = self._elapsed_time % space_between_beats
        if closeness < self._last_closeness:
            self.on_beat = the_time
            self.finished_beat = 0
            self.beat_num += 1
            self.started_beat = 1
            self.first_beat = not (self.beat_num % 4)
            
            if self.is_playing:
                self.click_sound.play()
        else:
            self.started_beat = 0

        self._last_closeness = closeness

    def handle_event(self, event):
        mouse_pos = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse[0]:
                if self.container_rect.collidepoint(mouse_pos) or self.button_rect.collidepoint(mouse_pos):
                    self.grabbed = True
                    self.move_slider(mouse_pos)

            if self.btn_play.collidepoint(mouse_pos):
                self.is_playing = not self.is_playing
                    
            elif self.btn_minus.collidepoint(mouse_pos):
                self.bpm_average = max(20, self.bpm_average - 1)
                val_range = self.max - self.min
                percentage = (self.bpm_average - self.min) / val_range
                self.button_rect.centerx = int(self.slider_left_pos + (percentage * (self.slider_right_pos - self.slider_left_pos)))
            
            elif self.btn_plus.collidepoint(mouse_pos):
                self.bpm_average = min(200, self.bpm_average + 1)
                val_range = self.max - self.min
                percentage = (self.bpm_average - self.min) / val_range
                self.button_rect.centerx = int(self.slider_left_pos + (percentage * (self.slider_right_pos - self.slider_left_pos)))

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.grabbed = False

        elif event.type == pygame.MOUSEMOTION:
            if self.grabbed:
                self.move_slider(mouse_pos)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect, border_radius=8)
        
        if self.is_playing and (self.started_beat or (self.on_beat and not self.finished_beat)):
            border_color = (255, 0, 0) 
        else:
            border_color = (250, 177, 177) 
            
        pygame.draw.rect(surface, border_color, self.rect, width=3, border_radius=8)
        pygame.draw.rect(surface, (218, 220, 224), self.container_rect, border_radius=4) #rectangle for slider
        pygame.draw.rect(surface, (224, 114, 114), self.button_rect, border_radius=50) #slider

        pygame.draw.rect(surface, (250, 177, 177), self.btn_play, border_radius=4)
        pygame.draw.rect(surface, (60, 60, 60), self.btn_minus, border_radius=4)
        pygame.draw.rect(surface, (60, 60, 60), self.btn_plus, border_radius=4)

        text_play = self.small_font.render("STOP" if self.is_playing else "START", True, (255, 255, 255))
        text_minus = self.font.render("-", True, (255, 255, 255))
        text_plus = self.font.render("+", True, (255, 255, 255))
        text_bpm = self.font.render(f"{int(self.bpm_average)} BPM", True, (0, 0, 0))
        text_metronome = self.font.render("Metronome", True, (0, 0, 0))

        surface.blit(text_play, (self.btn_play.centerx - text_play.get_width()//2, self.btn_play.centery - text_play.get_height()//2))
        surface.blit(text_minus, (self.btn_minus.centerx - text_minus.get_width()//2, self.btn_minus.centery - text_minus.get_height()//2 - 2))
        surface.blit(text_plus, (self.btn_plus.centerx - text_plus.get_width()//2, self.btn_plus.centery - text_plus.get_height()//2 - 2))
        surface.blit(text_bpm, (self.rect.centerx - text_bpm.get_width() // 2, self.rect.y + 50))
        surface.blit(text_metronome, (self.rect.centerx - text_metronome.get_width() // 2, self.rect.y + 20))


'''def main(): #used to test metronome individually
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    active_metronome = metronome((200, 200), (100,30), 120, 20, 200)

    going = True
    while going:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                going = False
            
            active_metronome.handle_event(e)

        active_metronome.update()

        screen.fill((40, 40, 40)) 
        active_metronome.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()'''