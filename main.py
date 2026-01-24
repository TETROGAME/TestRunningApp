import tkinter as tk
from TestRunner import TestRunner

def main():
    root = tk.Tk()
    runner = TestRunner.TestRunner("example_questions.json")
    root.mainloop()
if __name__ == '__main__':
    main()