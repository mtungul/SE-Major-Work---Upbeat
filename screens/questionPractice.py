import os
import pygame
import random
from save import complete_lesson, load_save, save_recent_score, save_highest_score
from utils.text import wrap_text
from utils.config import width, height
from startScreen import Button
from screens.baseScreen import baseScreen

class practiceScreen(baseScreen):
    def __init__(self, screen, step_data, runner, icons):
        super().__init__(screen, step_data, runner, icons)
        self.completed = False
        self.state = 'start'
        self.total_questions = 0
        self.save = load_save()
        
        #buttons
        self.beginButton = pygame.image.load(os.path.join(os.getcwd(),'img', 'buttons', 'begin_btn.png')).convert_alpha()
        self.begin_button = Button(width*(31/72), height/2, self.beginButton, (width*(5/36), height*(1/10)), self.start_quiz)

        self.answer_buttons = []

        if self.data['section'] == 'rhythm':
            answer_key = ['A', 'B', 'C', 'D']
        elif self.data['section'] == 'pitch':
            answer_key = ['1', '2', '3', '4']        
            
        for i in range(4):
            self.answer_buttons.append(answerButton(answer_key[i], width*(0.39) + i * 80, height*(0.72), 60, 60))

        #sound
        self.answer_channel = pygame.mixer.Channel(1)
        self.correct_sound =  pygame.mixer.Sound('soundExcerpts/correctSFX.mp3')
        self.incorrect_sound = pygame.mixer.Sound('soundExcerpts/incorrectSFX.mp3')

    def handle_event(self, event):
        if self.save['completed_lessons'].get(self.data['title'], False):
            new_screen = super().handle_event(event)
            if new_screen:
                return new_screen
        
        if self.state == 'start':
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for i, hitbox in enumerate(self.icon_hitbox):
                    if hitbox.collidepoint(mouse_pos):
                        return self.runner.go_to_level(i)
            new_screen = self.begin_button.handle_event(event)
            if new_screen:
                return new_screen
            new_screen = self.back_button.handle_event(event)
            if new_screen:
                return new_screen
            return None
        
        elif self.state == "practice":
            for button in self.answer_buttons:
                if button.clicked(event): #method in answerButton class
                    if button.correct:
                        self.current_score += 1
                        self.answer_channel.play(self.correct_sound)
                    else:
                        self.answer_channel.play(self.incorrect_sound)
                        question_index = self.questions_to_ask[self.current_question]
                        self.wrong_answers.append(question_index)

                    self.current_question += 1
                    self.total_questions += 1

                    if self.current_question < len(self.questions_to_ask):
                        self.load_question()
                    else:
                        if self.wrong_answers:
                            self.questions_to_ask = self.wrong_answers[:]
                            self.wrong_answers.clear()
                            self.current_question = 0
                            self.load_question()
                        else:
                            self.state = "finished"
                    break
            return None
        
        elif self.state == 'finished':
            if self.completed:
                    return self.next_button.handle_event(event)
            return None
        
        return super().handle_event(event)

    def reset_quiz(self):
        self.current_question = 0
        self.current_score = 0
        self.wrong_answers = []
        self.questions_to_ask = list(range(len(self.data["questions"])))

    def start_quiz(self):
        self.reset_quiz()
        self.load_question()

    def load_question(self):
        self.state = 'practice'
        question_index = self.questions_to_ask[self.current_question]
        question = self.data["questions"][question_index] #get questions within the level dictionary

        self.current_answer = question['answers'][:] #get answers within the questions dictionary
        random.shuffle(self.current_answer) #randomise order of answers so it's not the same everytime

        for i in range(len(self.answer_buttons)):
            self.answer_buttons[i].correct = (self.current_answer[i]["correct"]) #button is 'correct' depending on if the answer index (i) is correct in the dictionary
        
        #load image
        self.question_image = None
        if question["image"]:
            image_path = os.path.join(os.getcwd(), "img", f'questionPracticeImg/{question["image"]}')
            image = pygame.image.load(image_path).convert_alpha()
            self.question_image = pygame.transform.smoothscale(image, (200, 200))   
         
    def draw(self):
        self.draw_layout()
        
        if self.state == 'start':
            line_width = width*(97/108)
            lines = wrap_text(self.data["text"], self.font, line_width)

            y = height/3
            for line in lines:
                text = self.font.render(line, True, (0, 0, 0))
                self.screen.blit(text, (width/18, y))
                y += 40
            
            self.begin_button.draw(self.screen)  

            save = load_save()
            if save['completed_lessons'].get(self.data['title'], False):
                self.next_button.draw(self.screen)

        elif self.state == 'practice':
            score = self.font.render("Your Score:" + str(self.current_score), True, (0, 0, 0))
            if score:
                self.screen.blit(score, (width*(0.8), height*(0.25)))

            question_num = self.current_question + 1
            question_font = pygame.font.Font('fonts/Vera.ttf', 38)
            question_index = self.questions_to_ask[self.current_question]
            question = self.data["questions"][question_index]
            answer_font = pygame.font.Font('fonts/Vera.ttf', 30)
            
            text = question_font.render(f"{question_num}. {question['question']}", True, (0, 0, 0))
            self.screen.blit(text, (width/18, height*(0.32)))

            if question["note"]:
                note_font = pygame.font.Font('fonts/Vera.ttf', 20)
                note_text = note_font.render(question['note'], True, (0, 0, 0))
                self.screen.blit(note_text, (width/18, height*(0.32) + 44))

            #image
            if self.question_image:
                self.screen.blit(self.question_image, (width*(0.7), height*(0.38)))

            if self.data['section'] == 'rhythm':
                answer_key = ['A', 'B', 'C', 'D']
            elif self.data['section'] == 'pitch':
                answer_key = ['1', '2', '3', '4']

            for i in range(4):
                answer_text = answer_font.render(f"{answer_key[i]}) {self.current_answer[i]['text']}", True, (0,0,0))
                self.screen.blit(answer_text, (width/18, height*(0.45 + i * 0.06)))
            
            for button in self.answer_buttons:
                button.draw(self.screen)

        elif self.state == 'finished':
            accuracy = round(6/self.total_questions*100)

            if self.current_score == 6:
                self.completed = True
                complete_lesson(self.data["title"])
                save_recent_score(self.data["title"], accuracy)
                save_highest_score(self.data["title"], accuracy)

            line_width = width*(97/108)
            lines = wrap_text("You have completed all 6 questions! Click NEXT to proceed to the next level.", self.font, line_width)

            y = height/3
            for line in lines:
                text = self.font.render(line, True, (0, 0, 0))
                self.screen.blit(text, (width/18, y))
                y += 40
            accuracy_text = self.font.render(f"Overall Score and Accuracy: 6/{self.total_questions} ({accuracy}%)", True, (0, 0, 0))
            self.screen.blit(accuracy_text, (width/18, y + 10))

class answerButton():
    def __init__(self, letter, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""
        self.correct = False
        self.font = pygame.font.Font('fonts/Vera.ttf', 30)
        self.letter = letter

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()
        colour = (220, 220, 220)

        if self.rect.collidepoint(mouse):
            colour = (251, 198, 198)

        pygame.draw.rect(screen, colour, self.rect, border_radius=10)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2, border_radius=10)

        text = self.font.render(self.letter, True, (0, 0, 0))
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def clicked(self, event):
        return (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos))