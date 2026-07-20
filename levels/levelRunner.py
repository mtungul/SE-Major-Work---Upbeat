import pygame
from save import load_save

class levelRunner:
    def __init__(self, screen, level_data, icons):
        def get_order(level):
            return level['order']
        self.steps = sorted(level_data, key=get_order)
        self.screen = screen
        self.index = 0
        self.icons = icons

        save = load_save()
        self.completed = []
        for step in self.steps: #array of true or falses depending on completion
            self.completed.append(save['completed_lessons'].get(step['title'], False))

        self.max_unlocked = 0
        for i , completed in enumerate(self.completed):
            if completed: self.max_unlocked = i + 1

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
        
        elif step["lessonType"] == "pitchPianoPractice":
            from screens.pitchPianoPractice import practiceScreen
            return practiceScreen(self.screen, step, self, self.icons)
    
    def next_level(self):
        pygame.mixer.stop()
        self.completed[self.index] = True #current level is considered as 'completed'

        #set the max unlocked level to mark progress
        if self.index + 1 > self.max_unlocked:
            self.max_unlocked = self.index + 1

        self.index += 1 #add one to go to next level

        #after completing all the levels go back to home page
        if self.index >= len(self.steps):
            from startScreen import mainScreen
            self.index = 0
            return mainScreen(self.screen, self.icons)

        return self.get_current_screen()

    def back_level(self):
        pygame.mixer.stop()
        self.index -= 1 #minus one to go back a level
        return self.get_current_screen()
    
    def go_to_level(self, index):
        pygame.mixer.stop()
        save = load_save()
        step = self.steps[index]
        if (index <= self.max_unlocked or save["completed_lessons"].get(step["title"], False)): #only allow unlocked levels
            self.index = index
            return self.get_current_screen()

        return None