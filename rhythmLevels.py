levels = [
    { # level 1
    'section' : 'rhythm',
    'order' : 1,
    'lessonType' : 'reading',
    'title' : 'What is Rhythm?',
    'text' : 'In music, "rhythm" accounts for the timing and feel of a piece. It consists of the placement and duration of sounds or silences. In this level of UPBEAT you will learn about the different note values, time signatures, and tempo markings.',
    'img' : None,
    'icon' : 'book',
    },

    { # level 2
    'section' : 'rhythm',
    'order' : 2,
    'lessonType' : 'lesson',
    'title' : 'Subdivisions and Note Values',
    'text' : 'Subdivisions are how a beat is divided into a certain number of equal notes. Note values represent the duration of that note and are relative to the tempo (speed) of the music. The graph below shows the most common note values used, and how many of each equate to one semibreve (has the largest duration).',
    'img' : 'note_value_chart.png',
    'icon' : 'lesson',
    'excerpts' : [
        'rhythm_lvl2_ex1.mp3',
        'rhythm_lvl2_ex2.mp3',
    ],
    'excerptImg' : [
        'rhythm_lvl2_img1.png',
        'rhythm_lvl2_img2.png',
    ]
    },

    { # level 3
    'section' : 'rhythm',
    'order' : 3,
    'lessonType' : 'rhythmTapPractice',
    'title' : 'Note Values Practice',
    'text' : 'Now you will get to practice different rhythms! After clicking start, you will hear a four beat count in. Click the space bar to match the rhythm of the notes on the screen.',
    'icon' : 'quaver',
    },

    { # level 4
    'section' : 'rhythm',
    'order' : 4,
    'lessonType' : 'lesson',
    'title' : 'Rest Notes',
    'text' : 'Music is the art of both sound AND silence. As important as it is knowing when to play, it is also important to know when NOT to play. "Rests" are notes that tell us when to not play. Similarly to the previous lesson, there are different note values for each rest.',
    'img' : 'rest_value_chart.png',
    'icon' : 'lesson',
    'excerpts' : [
        'rhythm_lvl4_ex1.mp3',
        'rhythm_lvl4_ex2.mp3',
    ],
    'excerptImg' : [
        'rhythm_lvl4_img1.png',
        'rhythm_lvl4_img2.png',
    ]
    },

    { # level 5
    'section' : 'rhythm',
    'order' : 5,
    'lessonType' : 'rhythmTapPractice',
    'title' : 'Rest Notes Practice',
    'text' : '',
    'icon' : 'quaver',
    },

    { # level 6
    'section' : 'rhythm',
    'order' : 6,
    'lessonType' : 'lesson',
    'title' : 'Time Signatures',
    'text' : 'A time signature is the musical notation that dictates the pulse and rhythmic feel of a piece. It lets us know how to count before we start playing.',
    'icon' : 'lesson',
    },

    { # level 7
    'section' : 'rhythm',
    'order' : 7,
    'lessonType' : 'questionPractice',
    'title' : 'Time Signature Practice',
    'text' : '',
    'icon' : 'quaver',
    },

    { # level 8
    'section' : 'rhythm',
    'order' : 8,
    'lessonType' : 'lesson',
    'title' : 'Tempo',
    'text' : 'Tempo is the speed of a musical piece, and is it measured in beats per minute (BPM).',
    'icon' : 'lesson',
    },

    { # level 9
    'section' : 'rhythm',
    'order' : 9,
    'lessonType' : 'rhythmTapPractice',
    'title' : 'Final Practice',
    'text' : '',
    'icon' : 'quaver',
    },

    { # level 10
    'section' : 'rhythm',
    'order' : 10,
    'lessonType' : 'end',
    'title' : 'You have successfully completed the Rhythm section!',
    'text' : '',
    'icon' : 'star',
    }
]

import pygame

class levelRunner:
    def __init__(self, screen, level_data, icons):
        def get_order(level):
            return level['order']
        self.steps = sorted(level_data, key=get_order)
        self.screen = screen
        self.index = 0
        self.completed = [False] * len(self.steps) #sets all levels to current incomplete (array of 10 Falses)
        self.max_unlocked = 0
        self.icons = icons

    def get_current_screen(self):
        step = self.steps[self.index]

        if step["lessonType"] in ["reading", "lesson", "end"]: 
            from screens.lesson import lessonScreen
            return lessonScreen(self.screen, step, self, self.icons)

        elif step["lessonType"] == "questionPractice":
            from screens.questionPractice import practiceScreen
            return practiceScreen(self.screen, step, self, self.icons)
        
        elif step["lessonType"] == "rhythmTapPractice":
            from screens.rhythmTapPractice import practiceScreen
            return practiceScreen(self.screen, step, self, self.icons)
    
    def next_level(self):
        pygame.mixer.stop()
        self.completed[self.index] = True #current level is considered as 'completed'

        #set the max unlocked level to mark progress
        if self.index + 1 > self.max_unlocked:
            self.max_unlocked = self.index + 1

        self.index += 1 #add one to go to next level

        #after completing all the levels go back to home page
        #later put a variable setting rhythm section completion to true to allow the user to acces the pitch section !!!!
        if self.index >= len(self.steps):
            from startScreen import mainScreen
            return mainScreen(self.screen)

        return self.get_current_screen()

    def back_level(self):
        pygame.mixer.stop()
        self.index -= 1 #minus one to go back a level
        return self.get_current_screen()
    
    def go_to_level(self, index):
        pygame.mixer.stop()
        if index <= self.max_unlocked: #only allow unlocked levels
            self.index = index
            return self.get_current_screen()

        return None