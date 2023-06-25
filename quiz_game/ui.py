from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=288,
                                                     text="Some question text",
                                                     font=("Arial", 15, "italic"),
                                                     fill="black",
                                                     justify="center")
        self.canvas.grid(row=1, column=0, columnspan=2, sticky="news", padx=20, pady=20)
        self.score_label = Label(text="Score: 0", font=("Tahoma", 10, "bold"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, justify="center", command=self.true_command)
        self.true_button.grid(row=2, column=0, pady=10, padx=10)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, justify="center", command=self.false_command)
        self.false_button.grid(row=2, column=1, pady=10, padx=10)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="White")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_command(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_command(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")

        self.window.after(1000, self.get_next_question)
        self.score_label.config(text=f"Score: {self.quiz.score}")



