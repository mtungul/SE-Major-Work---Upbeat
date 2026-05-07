levels = [
    { # level 1
    'section' : 'rhythm',
    'order' : 1,
    'lessonType' : 'reading',
    'title' : 'What is Rhythm?',
    'text' : 'In music, "rhythm" accounts for the timing and feel of a piece. It consists of the placement and duration of sounds or silences. In this level of UPBEAT you will learn about the different note values, time signatures, and tempo markings.',
    'img' : '',
    'icon' : 'book',
    },
    { # level 2
    'section' : 'rhythm',
    'order' : 2,
    'lessonType' : 'lesson',
    'title' : 'Subdivisions and Note Values',
    'text' : 'Subdivisions are how a beat is divided into a certain number of equal notes. Note values represent the duration of that note and relative to the tempo (speed) of the music.',
    'img' : 'note_chart_value',
    'icon' : 'lesson',
    },
    { # level 3
    'section' : 'rhythm',
    'order' : 3,
    'lessonType' : 'practice',
    'title' : 'Note Values Practice',
    'text' : '',
    'icon' : 'quaver',
    },
    { # level 4
    'section' : 'rhythm',
    'order' : 4,
    'lessonType' : 'lesson',
    'title' : 'Rest Notes',
    'text' : '',
    'icon' : 'lesson',
    },
    { # level 5
    'section' : 'rhythm',
    'order' : 5,
    'lessonType' : 'practice',
    'title' : 'Rest Notes Practice',
    'text' : '',
    'icon' : 'quaver',
    },
    { # level 6
    'section' : 'rhythm',
    'order' : 6,
    'lessonType' : 'lesson',
    'title' : 'Time Signatures',
    'text' : '',
    'icon' : 'lesson',
    },
    { # level 7
    'section' : 'rhythm',
    'order' : 7,
    'lessonType' : 'practice',
    'title' : 'Time Signature Practice',
    'text' : '',
    'icon' : 'quaver',
    },
    { # level 8
    'section' : 'rhythm',
    'order' : 8,
    'lessonType' : 'lesson',
    'title' : 'Tempo',
    'text' : '',
    'icon' : 'lesson',
    },
    { # level 9
    'section' : 'rhythm',
    'order' : 9,
    'lessonType' : 'practice',
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

        elif step["lessonType"] == "practice":
            from screens.practice import practiceScreen
            return practiceScreen(self.screen, step, self, self.icons)
    
    def next_level(self):
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
    
    def go_to_level(self, index):
        if index <= self.max_unlocked:  # only allow unlocked steps
            self.index = index
            return self.get_current_screen()
        
    def back_level(self):
        self.index -= 1 #minus one to go back a level
        return self.get_current_screen()