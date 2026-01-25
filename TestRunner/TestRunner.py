from typing import List
from Question import Question
from TestRunner.QuestionLoader import QuestionLoader


class TestRunner:
    question_database: List[Question]

    def __init__(self, file_path: str):
        loader = QuestionLoader()
        try:
            self.question_database = loader.load(file_path)
        except ValueError as e:
            print(e)

    def validate_answer(self, question: Question, user_answer_indices: List[int]) -> bool:
        target = self.question_database.index(question)