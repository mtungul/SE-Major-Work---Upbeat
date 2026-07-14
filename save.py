import os
import json

SAVE_FILE = 'gameSaves/save.json'

DEFAULT_SAVE = {
    'completed_lessons': {},
}

def load_save():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, 'r') as file:
            return json.load(file)
        
    return DEFAULT_SAVE.copy()

def save_data(data):
    with open(SAVE_FILE, 'w') as file:
        json.dump(data, file, indent=2)

def complete_lesson(lesson_title):
    data = load_save()
    data['completed_lessons'][lesson_title] = True
    save_data(data)