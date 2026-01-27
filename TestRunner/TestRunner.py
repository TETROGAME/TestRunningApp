from typing import List, Dict
from TestRunner.Question import Question
from TestRunner.QuestionLoader import QuestionLoader


class TestRunner:
    question_database: List[Question]
    user_answer_ids: Dict[int, List[str]]
    _questions_by_id: Dict[int, Question]

    def __init__(self, file_path: str) -> None:

        loader = QuestionLoader()
        try:
            self.question_database = loader.load(file_path)
        except ValueError as e:
            print(e)

        self.user_answer_ids = {}
        self._questions_by_id = {question.id: question for question in self.question_database}

    def validate_answer(self, question_id: int) -> bool:
        question = self._questions_by_id[question_id]
        selected = set(self.user_answer_ids.get(question_id, []))
        correct = set(question.correct_option_ids)
        return selected == correct

    def submit_answer(self, question_id: int, user_answer_ids: List[str]) -> None:
        self.user_answer_ids[question_id] = user_answer_ids

    def count_score(self) -> int:
        score = 0
        for question in self.question_database:
            if self.validate_answer(question.id):
                score += 1
        return score