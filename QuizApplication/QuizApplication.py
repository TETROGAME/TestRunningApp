import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font

from TestRunner.TestRunner import TestRunner


class QuizApplication:
    test_runner: TestRunner
    def __init__(self, root: tk.Tk, test_runner: TestRunner) -> None:
        self.current_index = 0

        self.test_runner = test_runner
        self.user_choices = []

        self.root = root
        root.title('Программа тестирования "placeholder"')
        self.__build_ui()
        self.__display_questions()

    def __build_ui(self) -> None:
        self.font = Font(
            family='Arial',
            size=13
        )
        self.title_label = tk.Label(self.root, text="Текст вопроса", font=self.font)
        self.title_label.pack(pady=5, padx=5)
        self.options_frame = tk.Frame(self.root)
        self.options_frame.pack(pady=5, padx=5)
        self.next_button = tk.Button(self.root, text="Следующий вопрос", font=self.font, command=self.__next_question)
        self.next_button.pack(pady=5, padx=5)

    def __display_questions(self) -> None:
        for widget in self.options_frame.winfo_children():
            widget.destroy()

        current_question = self.test_runner.question_database[self.current_index]
        self.title_label.config(text=current_question.title)

        self.user_choices = []
        for index, option in enumerate(current_question.options):
            var = tk.IntVar()
            tk.Checkbutton(self.options_frame, text=option, variable=var).pack(anchor='w')
            self.user_choices.append(var)


    def __next_question(self) -> None:
        question = self.test_runner.question_database[self.current_index]
        selected_ids = [idx for idx, var in enumerate(self.user_choices) if var.get() == 1]
        self.test_runner.submit_answer(question.id, selected_ids)

        self.current_index += 1
        if self.current_index < len(self.test_runner.question_database):
            self.__display_questions()
        else:
            self.__finish_test()


    def __finish_test(self) -> None:
        score = self.test_runner.count_score()
        number_of_questions = len(self.test_runner.question_database)
        tk.messagebox.showinfo(
            title="Результат",
            message=f"Результат: {score}/{number_of_questions}\n"
        )
        self.root.destroy()