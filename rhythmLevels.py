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
    'text' : 'Now you will get to practice different rhythms! After clicking Begin, you will hear a four beat count in. Click the space bar to match the rhythm of the notes on the screen.',
    'icon' : 'quaver',
    'notes_easy' : ['crotchet', 'crotchet', 'crotchet', 'crotchet', 'minim', 'minim'],
    'notes_med' : ['crotchet', 'crotchet', 'quavers', 'quavers', 'semibreve'],
    'notes_hard' : ['crotchet', 'crotchet', 'crotchet', 'quavers', 'quavers', 'quavers', 'minim'],
    'num_notes_easy' : '6',
    'num_notes_med' : '5',
    'num_notes_hard' : '7',
    'bpm' : 60,
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
    'text' : 'Now you will get to practice playing both sound and silence. After clicking Begin, you will hear a four beat count in. Click the space bar to match the rhythm of the notes on the screen. TIP: Make sure not to press the space bar on a rest note, instead always keep counting to ensure you get the next note on time!',
    'icon' : 'quaver',
    'notes_easy' : ['crotchet', 'crotchet', 'crotchet', 'crotchet_rest', 'minim_rest', 'minim'],
    'notes_med' : ['crotchet', 'crotchet', 'crotchet_rest', 'quavers', 'minim_rest'],
    'notes_hard' : ['crotchet', 'crotchet_rest', 'minim', 'quavers', 'quavers', 'semibreve_rest'],
    'num_notes_easy' : '6',
    'num_notes_med' : '5',
    'num_notes_hard' : '6',
    'bpm' : 60,
    },

    { # level 6
    'section' : 'rhythm',
    'order' : 6,
    'lessonType' : 'lesson',
    'title' : 'Time Signatures',
    'text' : 'A time signature is the musical notation that dictates the pulse and rhythmic feel of a piece. It lets us know how to count before we start playing. Below is a diagram of the different parts of reading sheet music.',
    'img' : 'stave_chart.png',
    'icon' : 'lesson',
    },

    { # level 6.5
    'section' : 'rhythm',
    'order' : 7,
    'lessonType' : 'lesson',
    'title' : 'Time Signature cont.',
    'text' : '',
    'img' : 'time_signature.png',
    'icon' : 'lesson',
    },

    { # level 7
    'section' : 'rhythm',
    'order' : 8,
    'lessonType' : 'questionPractice',
    'title' : 'Time Signature Practice',
    'text' : "After clicking Begin, you will be asked 6 multiple choice questions about Time Signatures. Answer them all correctly to proceed to the next level. NOTE: Don't worry if you get a question wrong, you will be able to re-answer them again!",
    'icon' : 'quaver',
    'questions' : [
        {
           'image' : None,
            'question' : "What is a time signature?",
            'note' : None,
            'answers' : [
                {'text' : "A composer's signature when they write a piece", 'correct' : False},
                {'text' : "The musical notation that dictates the pulse and rhythm", 'correct' : True},
                {'text' : "How long a musical piece goes for", 'correct' : False},
                {'text' : "The written numbers that indicate the speed of a piece", 'correct' : False},
            ],
        },
        {
            'image' : 'top_num.png',
            'question' : "What does the top number indicate?",
            'note' : None,
            'answers' : [
                {'text' : "How many beats in a bar", 'correct' : True},
                {'text' : "What type of beat is used", 'correct' : False},
                {'text' : "How many bars there are", 'correct' : False},
                {'text' : "How long a bar is", 'correct' : False},
            ],
        },
        {
            'image' : 'bottom_num.png',
            'question' : "What does the bottom number indicate?",
            'note' : None,
            'answers' : [
                {'text' : "How many beats in a bar", 'correct' : False},
                {'text' : "What type of beat is used", 'correct' : True},
                {'text' : "How many bars there are", 'correct' : False},
                {'text' : "How long a bar is", 'correct' : False},
            ], 
        },
        {
            'image' : '3-4.png', # 3 4
            'question' : "How many beats per bar in this time signature?",
            'note' : None,
            'answers' : [
                {'text' : "3", 'correct' : True},
                {'text' : "4", 'correct' : False},
                {'text' : "7", 'correct' : False},
                {'text' : "2", 'correct' : False},
            ], 
        },
        {
            'image' : '4-8.png', # 4 8 
            'question' : "What note value is used to count in this time signature?",
            'note' : None,
            'answers' : [
                {'text' : "Quavers", 'correct' : True},
                {'text' : "Crotchets", 'correct' : False},
                {'text' : "Minims", 'correct' : False},
                {'text' : "Semibreves", 'correct' : False},
            ], 
        },
        {
            'image' : None,
            'question' : "What is the time signature of a piece with 3 minims per bar?",
            'note' : "Note: Top number | Bottom number",
            'answers' : [
                {'text' : "3 | 2", 'correct' : True},
                {'text' : "2 | 3", 'correct' : False},
                {'text' : "3 | 4", 'correct' : False},
                {'text' : "4 | 3", 'correct' : False},
            ] 
        },
    ],
    },

    { # level 8
    'section' : 'rhythm',
    'order' : 9,
    'lessonType' : 'lesson',
    'title' : 'Tempo',
    'text' : 'Tempo is the speed of a musical piece, and is it measured in beats per minute (BPM). There are different Italian terms used to describe the different tempo in each piece, and they are determined by a range of BPM - however, the range of BPM may differ between musicians, thus tempo names are interpreted from its "feel".',
    'icon' : 'lesson',
    'metronome' : True,
    'img' : 'tempo_markings.png',
    },

    { # level 9
    'section' : 'rhythm',
    'order' : 10,
    'lessonType' : 'rhythmTapPractice',
    'title' : 'Final Practice',
    'text' : 'To wrap everything up, you will combine the four different lesson about notes, rests, time signature, and tempo! After clicking Begin, you will hear a four beat count in. Click the space bar to match the rhythm of the notes on the screen. Good Luck!',
    'icon' : 'quaver',
    'notes_easy' : ['crotchet', 'crotchet', 'crotchet', 'crotchet_rest', 'minim_rest', 'minim'],
    'notes_med' : ['crotchet', 'crotchet', 'crotchet_rest', 'quavers', 'minim_rest'],
    'notes_hard' : ['crotchet', 'crotchet_rest', 'minim', 'quavers', 'quavers', 'semibreve_rest'],
    'num_notes_easy' : '6',
    'num_notes_med' : '5',
    'num_notes_hard' : '6',
    'bpm' : 70,
    },

    { # level 10
    'section' : 'rhythm',
    'order' : 11,
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
        self.index = 8
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