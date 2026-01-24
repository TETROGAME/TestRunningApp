from typing import Dict

from TestRunner.QuestionLoader import QuestionLoader


class TestRunner:
    question_database: Dict

    def __init__(self, file_path: str):
        loader = QuestionLoader()
        self.question_database = loader.load(file_path)
