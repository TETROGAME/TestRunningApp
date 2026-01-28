import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
from tkinter import ttk
from typing import Dict, List

from TestRunner.Question import Option
from TestRunner.TestRunner import TestRunner


class QuizApplication:
    test_runner: TestRunner
    def __init__(self, root: tk.Tk, test_runner: TestRunner) -> None:

        self.test_runner = test_runner

        self.root = root
        root.title('Программа тестирования')

        self.font = Font(
            family='Arial',
            size=13
        )
        self.__build_ui()

    def __build_ui(self) -> None:
        self.question_notebook = ttk.Notebook(self.root)
        self.question_notebook.pack(expand=True, fill='both')

        self.__load_question_tabs()

        self.submit_answers_button = tk.Button(self.root, text="Завершить тест", font=self.font, command=self.__proceed_after_questions)
        self.submit_answers_button.pack(fill="both", pady=5, padx=5)

    def __load_question_tabs(self):
        self.options_vars: Dict[int, List[tk.StringVar]] = dict()
        for question_id in self.test_runner.question_database.keys():
            current_question = self.test_runner.question_database[question_id]

            question_frame = tk.Frame()
            question_frame.pack()

            question_title = tk.Label(question_frame, text=current_question.title, font=self.font)
            question_title.pack()

            options_frame = tk.Frame(question_frame)
            options_frame.pack()

            current_question_vars = []
            for option in current_question.options:
                var = tk.StringVar(value="not_selected")
                option_checkbox = tk.Checkbutton(
                    options_frame,
                    variable=var,
                    onvalue=option.id,
                    offvalue="not_selected",
                    text=option.text,
                    font=self.font)
                option_checkbox.pack()
                current_question_vars.append(var)
            self.question_notebook.add(question_frame, text=f"{question_id}")
            self.options_vars[question_id] = current_question_vars

    def __submit_all_user_answers(self):
        user_answers: Dict[int, List[str]] = dict()
        for key in self.options_vars.keys():
            user_answers[key] = list(var.get() for var in self.options_vars[key] if var.get() != "not_selected")
        self.test_runner.submit_all(user_answers)
    def __show_score(self) -> None:
        score = self.test_runner.count_score()
        number_of_questions = len(self.test_runner.question_database)
        tk.messagebox.showinfo(
            title="Результат",
            message=f"Результат: {score}/{number_of_questions}\n"
        )
        if score == number_of_questions:
            tk.messagebox.showinfo(
                title="Успех",
                message="Тест сдан"
            )
            self.root.destroy()
            return
        option = tk.messagebox.askyesno(
            title="Просмотр результатов",
            message="Посмотреть ошибки?"
        )
        if option:
            self.__show_mistakes()

    def __proceed_after_questions(self):
        self.__submit_all_user_answers()
        self.__show_score()



    def __is_checked(self, question_id: int, option: Option) -> bool:
        return option.id in self.test_runner.user_answers[question_id]

    def __show_mistakes(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        mistakes_window_notebook = ttk.Notebook(self.root)
        mistakes_window_notebook.pack(expand=True, fill='both')

        qdb = self.test_runner.question_database
        for question_id in self.test_runner.question_database.keys():
            if not self.test_runner.validate_answer(question_id):
                question_frame = tk.Frame()
                question_frame.pack()

                label = tk.Label(question_frame, text=qdb[question_id].title, font=self.font)
                label.pack(pady=5, padx=5)

                options_frame = tk.Frame(question_frame)
                options_frame.pack()

                for option in qdb[question_id].options:
                    highlight = "black"
                    if self.__is_checked(question_id, option):
                        highlight = "green" if option.id in self.test_runner.question_database[question_id].correct_option_ids else "red"
                    label = tk.Label(
                        options_frame,
                        text=option.text,
                        font=self.font,
                        fg=highlight)
                    label.pack(pady=5, padx=5)
                mistakes_window_notebook.add(question_frame, text=f"{question_id}")



