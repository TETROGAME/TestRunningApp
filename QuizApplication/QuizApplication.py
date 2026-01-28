import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font

from TestRunner.Question import Option
from TestRunner.TestRunner import TestRunner


class QuizApplication:
    test_runner: TestRunner
    def __init__(self, root: tk.Tk, test_runner: TestRunner) -> None:
        self.current_index = 1

        self.test_runner = test_runner
        self.user_choices: list[tk.IntVar] = []
        self.current_option_ids: list[str] = []

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
            tk.Checkbutton(self.options_frame, text=option.text, font=self.font, variable=var).pack(anchor='w')
            self.user_choices.append(var)
            self.current_option_ids.append(option.id)


    def __next_question(self) -> None:
        selected_option_ids = [
            opt_id
            for opt_id, var in zip(self.current_option_ids, self.user_choices)
            if var.get() == 1
        ]
        self.test_runner.submit_answer(self.current_index, selected_option_ids)

        self.current_index += 1
        if self.current_index <= len(self.test_runner.question_database):
            self.__display_questions()
        else:
            self.__show_score()


    def __show_score(self) -> None:
        score = self.test_runner.count_score()
        number_of_questions = len(self.test_runner.question_database)
        tk.messagebox.showinfo(
            title="Результат",
            message=f"Результат: {score}/{number_of_questions}\n"
        )
        option = tk.messagebox.askyesno(
            title="Просмотр результатов",
            message="Посмотреть ошибки?"
        )
        if option:
            self.__show_mistakes()

    def __is_checked(self, question_id: int, option: Option) -> bool:
        return option.id in self.test_runner.user_answer_ids[question_id]
    def __show_mistakes(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        label_frame = tk.Frame(self.root)
        label_frame.pack()

        qdb = self.test_runner.question_database
        for question_id in self.test_runner.question_database.keys():
            if not self.test_runner.validate_answer(question_id):
                question_frame = tk.Frame(label_frame)
                question_frame.pack()

                label = tk.Label(question_frame, text=f"{question_id}. {qdb[question_id].title}", font=self.font)
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