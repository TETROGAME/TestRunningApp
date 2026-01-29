import tkinter as tk
from TestRunner import TestRunner
from QuizApplication import QuizApplication as QApp
def main():
    runner = TestRunner.TestRunner("example_questions_ru.json", 5)
    root = tk.Tk()
    app = QApp.QuizApplication(root, runner)
    root.mainloop()

if __name__ == '__main__':
    main()