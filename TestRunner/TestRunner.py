from typing import Dict, List
from TestRunner.Question import Question
from TestRunner.QuestionLoader import QuestionLoader


class TestRunner:
    def __init__(self, file_path: str) -> None:
        loader = QuestionLoader()
        self.question_database: Dict[int, Question] = loader.load(file_path)
        self.question_order: List[int] = list(self.question_database.keys())
        self.user_answers: Dict[int, List[str]] = {}

    def validate_answer(self, question_id: int) -> bool:
        question = self.question_database[question_id]
        selected = set(self.user_answers.get(question_id, []))
        correct = set(question.correct_option_ids)
        return selected == correct

    def submit_all(self, user_answers: Dict[int, List[str]]) -> None:
        self.user_answers = user_answers

    def count_score(self) -> int:
        score = 0
        for question_id in self.question_order:
            if self.validate_answer(question_id):
                score += 1
        return score