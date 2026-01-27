from typing import List, Dict
from TestRunner.Question import Question
from TestRunner.QuestionLoader import QuestionLoader


class TestRunner:
    question_database: List[Question]
    user_answer_ids = {}

    def __init__(self, file_path: str) -> None:
        loader = QuestionLoader()
        try:
            self.question_database = loader.load(file_path)
        except ValueError as e:
            print(e)

    def validate_answer(self, question_id: int, user_answer_ids: Dict[int, int]) -> bool:
        target = self.question_database[question_id]
        if target.correct_answer_ids == user_answer_ids[question_id]:
            return True
        else:
            return False

    def submit_answer(self, question_id: int, user_answer_ids: List[int]) -> None:
        self.user_answer_ids[question_id] = user_answer_ids

    def count_score(self) -> int:
        score = 0
        for question in self.question_database:
            if self.validate_answer(question.id, self.user_answer_ids):
                score += 1
        return score