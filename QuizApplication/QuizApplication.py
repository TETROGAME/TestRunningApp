import tkinter as tk
from tkinter import messagebox

from TestRunner.TestRunner import TestRunner


class QuizApplication:
    test_runner: TestRunner
    def __init__(self, root: tk.Tk, test_runner: TestRunner) -> None:
        self.test_runner = test_runner
        self.root = root
        self.__display_questions()

    def __display_questions(self):
        pass
