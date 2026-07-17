pitchlevels = [
    { # level 1
    'section' : 'pitch',
    'order' : 1,
    'lessonType' : 'reading',
    'title' : 'What is Pitch?',
    'text' : (
        "In music, 'pitch' is how high or low a note is. With rhythm, it is what builds the melodies and harmonies of a song! "
        "In this section of UPBEAT you will learn about the notes on the piano, the C major scale and how to play a few easy melodies!"),
    'img' : 'pitch.png',
    'icon' : 'book',
    },

    { # level 2
    'section' : 'pitch',
    'order' : 2,
    'lessonType' : 'lesson',
    'title' : 'Notes on the Piano',
    'text' : (
        "Unlike our regular ABC's, the musical alphabet only consists of letters A to G, and typically starts at 'C'. "
        "These 7 letters repeat themselves in what's called an octave. For now, we will only be focusing on one octave."),
    'img' : 'piano_chart.png',
    'icon' : 'lesson',
    },

    { # level 3
    'section' : 'pitch',
    'order' : 3,
    'lessonType' : 'lesson',
    'title' : 'C Major Scale',
    'text' : (
        "A scale is an ordered sequence of notes that follows a specific pattern between a note and its octave. "
        "The two fundamental types of scales are major and minor, where major sounds 'happy', and minor sounds 'sad'. "
        "The C major scale is one of these many scales, consisting of notes C D E F G A B C. These are all the white keys on a piano."),
    'icon' : 'lesson',
    'img' : 'piano.png',
    'excerpts' : [
        'cmaj_scale.mp3',
        'cmin_scale.mp3',
    ],
    'excerptImg' : [
        'cmaj_scale_txt.png',
        'cmin_scale_txt.png',
    ]
    },

    { # level 3
    'section' : 'pitch',
    'order' : 3,
    'lessonType' : 'lesson',
    'title' : 'C Major Scale cont.',
    'text' : (
        "The pitch of a note is read by its position on a 5-line stave, and a clef. "
        "A clef is a musical symbol at the beginning of the stave that tells us which notes are being represented by stave's lines and spaces, "
        "i.e. where the notes are."),
    'icon' : 'lesson',
    'img' : 'cmaj_chart.png',
    },

    { # level 4
    'section' : 'pitch',
    'order' : 4,
    'lessonType' : 'lesson',
    'title' : 'How to Read Treble Clef',
    'text' : (
        "An easy way to read treble clef is by remembering that the gaps spell the word 'FACE', "
        "and the lines can be remembered using the mnemonic 'Every Good Boy Deserves Fruit'."),
    'img' : 'treble_clef_chart.png',
    'icon' : 'lesson',
    },

    { # level 5
    'section' : 'pitch',
    'order' : 5,
    'lessonType' : 'questionPractice',
    'title' : 'C Major Scale Practice',
    'text' : (
        "After clicking Begin, you will be asked 6 multiple choice questions about the C Major Scale. "
        "Answer them all correctly to proceed to the next level. NOTE: If you get a question wrong, you will be able to re-answer them again at the end!"),
    'img' : None,
    'icon' : 'quaver',
    'questions' : [
        {
           'image' : 'treble_clef.png',
            'question' : "What is this?",
            'note' : None,
            'answers' : [
                {'text' : "Treble clef", 'correct' : True},
                {'text' : "Bass clef", 'correct' : False},
                {'text' : "Time signature", 'correct' : False},
                {'text' : "Percussion clef", 'correct' : False},
            ],
        },
        {
            'image' : 'middleC.png',
            'question' : "What note is this?",
            'note' : None,
            'answers' : [
                {'text' : "C", 'correct' : True},
                {'text' : "A", 'correct' : False},
                {'text' : "F", 'correct' : False},
                {'text' : "E", 'correct' : False},
            ],
        },
        {
            'image' : 'b.png',
            'question' : "What note is this?",
            'note' : None,
            'answers' : [
                {'text' : "B", 'correct' : True},
                {'text' : "G", 'correct' : False},
                {'text' : "D", 'correct' : False},
                {'text' : "C", 'correct' : False},
            ], 
        },
        {
            'image' : 'e.png',
            'question' : "What note is this?",
            'note' : None,
            'answers' : [
                {'text' : "E", 'correct' : True},
                {'text' : "F", 'correct' : False},
                {'text' : "C", 'correct' : False},
                {'text' : "B", 'correct' : False},
            ], 
        },
        {
            'image' : 'c.png',
            'question' : "What note is this?",
            'note' : None,
            'answers' : [
                {'text' : "C", 'correct' : True},
                {'text' : "D", 'correct' : False},
                {'text' : "B", 'correct' : False},
                {'text' : "A", 'correct' : False},
            ], 
        },
        {
            'image' : 'f.png',
            'question' : "What note is this?",
            'note' : None,
            'answers' : [
                {'text' : "F", 'correct' : True},
                {'text' : "A", 'correct' : False},
                {'text' : "G", 'correct' : False},
                {'text' : "B", 'correct' : False},
            ] 
        },
    ],
    },

    { # level 6
    'section' : 'pitch',
    'order' : 6,
    'lessonType' : 'pitchPianoPractice',
    'title' : 'Song #1 : Mary Had a Little Lamb',
    'text' : (
        "Now you will get to practice playing a song! After clicking Begin, there will be sheet music for you to follow and an "
        "interactive piano you can play using your computer keyboard. See the image below to know where each note lies."),
    'icon' : 'quaver',
    'sheetMusic' : 'MaryHadALittleLamb_sheetmusic.png',
    'sheetMusic_assist' : 'MaryHadALittleLamb_sheetmusic_assist.png',
    'expectedKeys' : [
        'E', 'D', 'C', 'D', 
        'E', 'E', 'E', 
        'D', 'D', 'D', 
        'E', 'E', 'E', 
        'E', 'D', 'C', 'D', 
        'E', 'E', 'E', 'E', 
        'D', 'D', 'E','D', 
        'C'],
    'barLength' : [4, 3, 3, 3, 4, 4, 4, 1],
    },

    { # level 7
    'section' : 'pitch',
    'order' : 7,
    'lessonType' : 'pitchPianoPractice',
    'title' : 'Song #2 : Twinkle Twinkle Little Star',
    'text' : (
        "After clicking Begin, there will be sheet music for you to follow and an "
        "interactive piano you can play using your computer keyboard. See the image below to know where each note lies."),
    'icon' : 'quaver',
    'sheetMusic' : 'TwinkleTwinkle_sheetmusic.png',
    'sheetMusic_assist' : 'TwinkleTwinkle_sheetmusic_assist.png',
    'expectedKeys' : [
        'C', 'C', 'G', 'G', 
        'A', 'A', 'G', 
        'F', 'F', 'E', 'E',
        'D', 'D', 'C',
        'G', 'G', 'F', 'F',
        'E', 'E', 'D', 
        'G', 'G', 'F', 'F',
        'E', 'E', 'D', 
        'C', 'C', 'G', 'G', 
        'A', 'A', 'G', 
        'F', 'F', 'E', 'E',
        'D', 'D', 'C',],
    'barLength' : [4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3],
    },

    { # level 8
    'section' : 'pitch',
    'order' : 8,
    'lessonType' : 'pitchPianoPractice',
    'title' : 'Song #3 : Jingle Bells',
    'text' : (
        "This is the last Practice Level of Upbeat! In the following sheet music, you will see note heads coloured in blue towards the end. "
        "This will be what's called a harmony. A harmony is when two or more notes are played at the same time and create a pleasing sound. "
        "NOTE: Playing the harmony is optional (although is recommended). If you do, make sure to keep playing the melody as well."),
    'icon' : 'quaver',
    'sheetMusic' : 'JingleBells_sheetmusic.png',
    'sheetMusic_assist' : 'JingleBells_sheetmusic_assist.png',
    'expectedKeys' : [
        'E', 'E', 'E',
        'E', 'E', 'E',
        'E', 'G', 'C', 'D',
        'E',
        'F', 'F', 'F', 'F',
        'F', 'E', 'E', 'E', 'E',
        'E', 'D', 'D', 'E',
        'D', 'G',
        'E', 'E', 'E',
        'E', 'E', 'E',
        'E', 'G', 'C', 'D',
        'E',
        'F', 'F', 'F', 'F',
        'F', 'E', 'E', 'E', 'E',
        'G', 'G', 'F', 'D',
        'C',],
    'barLength' : [3, 3, 4, 1, 4, 5, 4, 2, 3, 3, 4, 1, 4, 5, 4, 1],
    },

    { # level 9
    'section' : 'pitch',
    'order' : 9,
    'lessonType' : 'end',
    'title' : 'You have successfully completed the Pitch Section!',
    'text' : '',
    'icon' : 'star',
    'img' : None,
    }
]