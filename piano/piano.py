import pygame
import piano.piano_lists as pl
from pygame import mixer

fps = 60
timer = pygame.time.Clock()

class Piano:
    KEYBOARD = {
        pygame.K_s: ("white", 0),
        pygame.K_e: ("black", 0),
        pygame.K_d: ("white", 1),
        pygame.K_r: ("black", 1),
        pygame.K_f: ("white", 2),
        pygame.K_g: ("white", 3),
        pygame.K_y: ("black", 2),
        pygame.K_h: ("white", 4),
        pygame.K_u: ("black", 3),
        pygame.K_j: ("white", 5),
        pygame.K_i: ("black", 4),
        pygame.K_k: ("white", 6),
        pygame.K_l: ("white", 7),
    }
    
    def __init__(self, screen, width, height, pos : tuple):
        self.screen = screen
        self.width = width
        self.height = height
        self.pos = pos
        self.key_font = pygame.font.Font("fonts/Vera.ttf", 16)

        self.white_key_width = 60
        self.black_key_width = 40
        self.HEIGHT = 300

        self.black_notes = pl.black_notes
        self.black_notes_names = pl.black_notes_names
        self.white_notes = pl.white_notes
        self.white_notes_names = pl.white_notes_names

        self.white_sounds = []
        self.black_sounds = []

        self.active_whites = []
        self.active_blacks = []

        self.white_keys = []
        self.black_keys = []

        self.current_white = None
        self.current_black = None
        self.keys_held = set()
        
        self.current_note = None

        #add sound files to sound arrays
        for note in self.white_notes:
            self.white_sounds.append(mixer.Sound(f"piano/piano_notes/{note}.wav"))

        for note in self.black_notes:
            self.black_sounds.append(mixer.Sound(f"piano/piano_notes/{note}.wav"))
    
    def draw_piano(self):
        self.white_keys = []
        for i in range(8): #8 white notes
            rect = pygame.draw.rect(self.screen, 'white', [self.pos[0] + i * self.white_key_width, self.pos[1], self.white_key_width, 300], 0, 2)
            self.white_keys.append(rect)
            pygame.draw.rect(self.screen, 'black', [self.pos[0] + i * self.white_key_width, self.pos[1], self.white_key_width, 300], 2, 2)
            key_label = self.key_font.render(self.white_notes[i][0], True, 'black')
            self.screen.blit(key_label, (self.pos[0] + i * self.white_key_width + 3, self.pos[1] + self.height - 20))
        
        self.black_keys = []    
        black_key_positions = [0, 1, 3, 4, 5]  #5 black notes
        for i, position in enumerate(black_key_positions):
            x = ((position + 1) * self.white_key_width - self.black_key_width // 2 ) + self.pos[0] 

            rect = pygame.draw.rect(self.screen, 'black', [x, self.pos[1], self.black_key_width, 200], 0, 2)
            if i in self.active_blacks:
                pygame.draw.rect(self.screen, 'green', [x, self.pos[1], self.black_key_width, 200], 2, 2)


            self.black_keys.append(rect)

        for i in self.active_whites:
            pygame.draw.rect(self.screen, 'green', [self.pos[0] + i * self.white_key_width, self.pos[1] + self.height - 100, self.white_key_width, 100], 2, 2)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            black_key = False
            
            for i in range(len(self.black_keys)):
                if self.black_keys[i].collidepoint(event.pos):
                    self.current_black = i
                    self.current_note = self.black_notes_names[i]
                    self.black_sounds[i].play()
                    if i not in self.active_blacks:
                        self.active_blacks.append(i)
                    black_key = True
            
            if not black_key:
                for i in range(len(self.white_keys)):
                    if self.white_keys[i].collidepoint(event.pos):
                        self.current_white = i
                        self.current_note = self.white_notes_names[i]
                        self.white_sounds[i].play()
                        if i not in self.active_whites:
                            self.active_whites.append(i)

        if event.type == pygame.MOUSEBUTTONUP:
            if self.current_white is not None:
                self.white_sounds[self.current_white].stop()
                self.current_white = None
                self.active_whites.clear()
            
            if self.current_black is not None:
                self.black_sounds[self.current_black].stop()
                self.current_black = None
                self.active_blacks.clear()

        if event.type == pygame.KEYDOWN:
            if event.key in self.KEYBOARD and event.key not in self.keys_held:
                self.keys_held.add(event.key)
                colour, index = self.KEYBOARD[event.key]

                if colour == "white":
                    self.white_sounds[index].play()
                    self.active_whites.append(index)
                    self.current_note = self.white_notes_names[index]

                else:
                    self.black_sounds[index].play()
                    self.active_blacks.append(index)
                    self.current_note = self.black_notes_names[index]
        
        if event.type == pygame.KEYUP:
            if event.key in self.keys_held:
                self.keys_held.remove(event.key)

                colour, index = self.KEYBOARD[event.key]

                if colour == "white":
                    self.white_sounds[index].stop()
                    if index in self.active_whites:
                        self.active_whites.remove(index)
                else:
                    self.black_sounds[index].stop()
                    if index in self.active_blacks:
                        self.active_blacks.remove(index)
        return None
    
    def get_current_note(self):
        note = self.current_note
        self.current_note = None
        return note