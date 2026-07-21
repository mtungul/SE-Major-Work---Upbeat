rhythmlevels = [
    { # level 1
    'section' : 'rhythm',
    'order' : 1,
    'lessonType' : 'reading',
    'title' : 'What is Rhythm?',
    'text' : (
        "In music, 'rhythm' accounts for the timing and feel of a piece. It consists of the placement and duration of sounds or silences. "
        "In this section of UPBEAT you will learn about the different note values, time signatures, and tempo markings."),
    'img' : 'rhythm.png',
    'icon' : 'book',
    },

    { # level 2
    'section' : 'rhythm',
    'order' : 2,
    'lessonType' : 'lesson',
    'title' : 'Note Values',
    'text' : (
        'Note values represent how long a note lasts for and are relative to the tempo (speed) of the music. '
        'Each note has their own name and notation, as shown below. Click the play buttons to hear samples of how these notes may sound – the notes they are playing are displayed next to them.'),
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
    'text' : (
        'Now you will get to practice different rhythms! After clicking Begin, you will hear a count in of four beats, '
        'then you must hit the space bar to match the notes on the screen! '
        'While you are playing, you will hear a quiet beat to help you play in time. '),
    'icon' : 'quaver',
    'notes_easy' : ['crotchet', 'crotchet', 'crotchet', 'crotchet', 'crotchet', 'minim'],
    'notes_med' : ['crotchet', 'crotchet', 'crotchet', 'quavers', 'quavers'],
    'notes_hard' : ['crotchet', 'crotchet', 'crotchet', 'crotchet', 'quavers', 'quavers', 'minim'],
    'num_notes_easy' : '6',
    'num_notes_med' : '5',
    'num_notes_hard' : '7',
    'bpm_easy' : 60,
    'bpm_med' : 60,
    'bpm_hard' : 60,
    'chart' : 'note_value_chart.png',
    },

    { # level 4
    'section' : 'rhythm',
    'order' : 4,
    'lessonType' : 'lesson',
    'title' : 'Rest Notes',
    'text' : (
        "Music is the art of both sound AND silence. As important as it is knowing when to play, it is also important to know when to NOT play. "
        "'Rests' are notes that tell us when to NOT play. Similarly to the previous lesson, there are different note values for each rest."),
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
    'text' : (
        'Now you will get to practice playing both sound and silence! After clicking Begin, you will hear a count in of four beats. '
        'Click the space bar to match the rhythm of the notes on the screen. '
        '                                                                                                                                '
        '                                                                                                                                '
        '                                                                                                                                '
        '                                                                                                                                '
        '                                                                                                                                '
        '                                                                                                                                '
        '                                                                                                                                '
        'TIP: Make sure not to press the space bar on a rest note, instead always keep counting to make sure you get the next note on time!'),
    'icon' : 'quaver',
    'notes_easy' : ['crotchet', 'crotchet', 'crotchet', 'crotchet_rest', 'crotchet_rest', 'crotchet_rest'],
    'notes_med' : ['crotchet', 'crotchet', 'crotchet_rest', 'minim', 'minim_rest'],
    'notes_hard' : ['crotchet', 'crotchet_rest', 'minim', 'crotchet', 'quavers', 'semibreve_rest'],
    'num_notes_easy' : '6',
    'num_notes_med' : '5',
    'num_notes_hard' : '6',
    'bpm_easy' : 60,
    'bpm_med' : 60,
    'bpm_hard' : 60,
    'chart' : 'rest_value_chart.png',
    },

    { # level 6
    'section' : 'rhythm',
    'order' : 6,
    'lessonType' : 'lesson',
    'title' : 'Time Signatures',
    'text' : (
        'A time signature is the musical notation that tells us the pulse and rhythmic feel of a piece. '
        'It lets us know how to count before we start playing. Below is a diagram of the different parts of reading sheet music.'),
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
    'text' : (
        "After clicking Begin, you will be asked 6 multiple choice questions about Time Signatures. "
        "Answer them all correctly to proceed to the next level. NOTE: Don't worry if you get a question wrong, you will be able to re-answer them again!"),
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
    'text' : (
        'Tempo is the speed of a musical piece, and is measured in beats per minute (BPM). '
        'There are different Italian terms used to describe the different tempo in each piece, '
        'and they are determined by a range of BPM - however, the range of BPM may differ between musicians, '
        'thus tempo names are interpreted from its "feel".'),
    'icon' : 'lesson',
    'metronome' : True,
    'img' : 'tempo_markings.png',
    },

    { # level 9
    'section' : 'rhythm',
    'order' : 10,
    'lessonType' : 'rhythmTapPractice',
    'title' : 'Final Rhythm Practice',
    'text' : (
        'To wrap everything up, you will combine the four different lessons about notes, rests, time signature, and tempo!'
        ' After clicking Begin, you will hear a count in of four beats. Click the space bar to match the rhythm of the notes on the screen. Good Luck!'),
    'icon' : 'quaver',
    'notes_easy' : ['minim', 'minim', 'minim_rest', 'minim', 'minim_rest', 'minim'],
    'notes_med' : ['crotchet', 'crotchet', 'crotchet', 'crotchet', 'quavers', 'crotchet_rest', 'crotchet_rest', 'crotchet_rest'],
    'notes_hard' : ['crotchet', 'crotchet', 'crotchet', 'quavers', 'quavers', 'quavers', 'crotchet_rest', 'crotchet_rest'],
    'num_notes_easy' : '6',
    'num_notes_med' : '8',
    'num_notes_hard' : '8',
    'bpm_easy' : 60,
    'bpm_med' : 50,
    'bpm_hard' : 70,
    },

    { # level 10
    'section' : 'rhythm',
    'order' : 11,
    'lessonType' : 'end',
    'title' : 'Rhythm Section Complete!',
    'text' : (
        'Great work! You have fully completed the rhythm section of Upbeat! You are now able to proceed to the pitch section of the game. '
        'NOTE: Feel free to revisit any of the previous levels whenever you want.'),
    'icon' : 'star',
    }
]