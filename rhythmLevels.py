from utils.icons import Icons
levels = [
    { # level 1
    'section' : 'rhythm',
    'lessonType' : 'reading',
    'Title' : 'What is Rhythm?',
    'Text' : 'In music, "rhythm" accounts for the timing and feel of a piece. It consists of the placement and duration of sounds or silences. In this level of UPBEAT you will learn about the different note values, time signatures, and tempo markings.',
    'icon' : 'book',
    },
    { # level 2
    'section' : 'rhythm',
    'lessonType' : 'lesson',
    'Title' : 'Subdivisions and Note Values',
    'Text' : '',
    'icon' : 'lesson',
    },
    { # level 3
    'section' : 'rhythm',
    'lessonType' : 'practice',
    'Title' : 'Note Values Practice',
    'Text' : '',
    'icon' : 'quaver',
    },
    { # level 4
    'section' : 'rhythm',
    'lessonType' : 'lesson',
    'Title' : 'Rest Notes',
    'Text' : '',
    'icon' : 'lesson',
    },
    { # level 5
    'section' : 'rhythm',
    'lessonType' : 'practice',
    'Title' : 'Rest Notes Practice',
    'Text' : '',
    'icon' : 'quaver',
    },
    { # level 6
    'section' : 'rhythm',
    'lessonType' : 'lesson',
    'Title' : 'Time Signatures',
    'Text' : '',
    'icon' : 'lesson',
    },
    { # level 7
    'section' : 'rhythm',
    'lessonType' : 'practice',
    'Title' : 'Time Signature Practice',
    'Text' : '',
    'icon' : 'quaver',
    },
    { # level 8
    'section' : 'rhythm',
    'lessonType' : 'lesson',
    'Title' : 'Tempo',
    'Text' : '',
    'icon' : 'lesson',
    },
    { # level 9
    'section' : 'rhythm',
    'lessonType' : 'practice',
    'Title' : 'Final Practice',
    'Text' : '',
    'icon' : 'quaver',
    },
    { # level 10
    'section' : 'rhythm',
    'lessonType' : 'end',
    'Title' : 'You have successfully completed the Rhythm section!',
    'Text' : '',
    'icon' : 'star',
    }
]

class levelRunner:
    def __init__(self, screen, level_data, icons):
        self.screen = screen
        self.steps = level_data 
        self.index = 0
        self.completed = [False] * len(self.steps)
        self.max_unlocked = 0
        self.icons = icons

    def get_current_screen(self):
        step = self.steps[self.index]

        if step["lessonType"] in ["reading", "lesson", "end"]: 
            from screens.lesson import lessonScreen
            return lessonScreen(self.screen, step, self, self.icons)

        elif step["lessonType"] == "practice":
            from screens.practice import practiceScreen
            return practiceScreen(self.screen, step, self)
    
    def next_step(self):
        self.completed[self.index] = True

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
    
    def go_to_step(self, index):
        if index <= self.max_unlocked:  # only allow unlocked steps
            self.index = index
            return self.get_current_screen()