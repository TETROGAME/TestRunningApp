from typing import List
from TestRunner.Question import Question
from TestRunner.QuestionLoader import QuestionLoader


class TestRunner:
    question_database: List[Question]

    def __init__(self, file_path: str):
        loader = QuestionLoader()
        try:
            self.question_database = loader.load(file_path)
        except ValueError as e:
            print(e)

    def validate_answer(self, question_id: int, user_answer_ids: List[int]) -> bool:
        target = self.question_database[question_id]
        if target.correct_answer_ids == user_answer_ids:
            return True
        else:
            return False