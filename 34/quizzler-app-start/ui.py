from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.question = self.quiz_brain.next_question()
        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score : {self.quiz_brain.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text=f"{self.question}", font=("Arial", 13, "italic"),
                                                     width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20)

        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, command=self.correct_button_handle)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)
        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, command=self.wrong_button_handle)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz_brain.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=self.quiz_brain.next_question())
            self.score_label.config(text=f"Score : {self.quiz_brain.get_score()}")
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def correct_button_handle(self):
        self.give_feedback(self.quiz_brain.check_answer('True'))

    def wrong_button_handle(self):
        self.give_feedback(self.quiz_brain.check_answer('False'))

    def give_feedback(self, result):
        if result:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)

    def flash(self):
        self.canvas.config(bg="white")
