import os
import json
import copy

SAVE_FILE = 'gameSaves/save.json'

DEFAULT_SAVE = {
    'first_time': True,
    'completed_lessons': {},
    'most_recent_score': {},
    'highest_score': {},
}

def load_save():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, 'r') as file:
            data = json.load(file)
            
        if 'completed_lessons' not in data:
            data['completed_lessons'] = {}
        if 'most_recent_score' not in data:
            data['most_recent_score'] = {}
        if 'highest_score' not in data:
            data['highest_score'] = {}
        return data
    
    return copy.deepcopy(DEFAULT_SAVE)

def save_data(data):
    with open(SAVE_FILE, 'w') as file:
        json.dump(data, file, indent=2)

def complete_lesson(lesson_title):
    data = load_save()
    data['completed_lessons'][lesson_title] = True
    save_data(data)

def save_recent_score(lesson_title, score):
    data = load_save()
    data['most_recent_score'][lesson_title] = score
    save_data(data)

def save_highest_score(lesson_title, score):
    data = load_save()
    previous_highest = data['highest_score'].get(lesson_title, 0)
    if score > previous_highest:
        data['highest_score'][lesson_title] = score
    save_data(data)

#either make a new set of functions for rhythm tap practice that uses title, difficulty, score
#or add difficulty to the current one and questions only has 1 difficulty