import tkinter as tk
from TestRunner import TestRunner
from QuizApplication import QuizApplication as QApp
import os, sys
def get_resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def main():
    relative_file_path = "source_files/csv/example_questions_ru.csv"
    resource_path = str(get_resource_path(relative_file_path))
    runner = TestRunner.TestRunner(resource_path, 5)
    root = tk.Tk()
    app = QApp.QuizApplication(root, runner)
    root.mainloop()

if __name__ == '__main__':
    main()