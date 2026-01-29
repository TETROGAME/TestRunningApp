from typing import Dict, List
from random import sample, shuffle
from TestRunner.Question import Question
from TestRunner.QuestionLoader import QuestionLoader


class TestRunner:
    def __init__(self, file_path: str, displayed_questions_amount: int = 10) -> None:
        loader = QuestionLoader()
        self.full_question_database: Dict[int, Question] = loader.load(file_path)
        self.current_session_question_database = (
            self.__choose_random_questions(
            amount=displayed_questions_amount
            )
        )
        self.user_answers: Dict[int, List[str]] = {}

    def __choose_random_questions(self, amount: int) -> Dict[int, Question]:
        if amount > len(self.full_question_database):
            raise ValueError(f"Chosen {amount} questions to display. Available only {len(self.full_question_database)}")
        if amount < 0:
            raise ValueError(f"Chosen {amount} is negative.")
        result = dict()
        randomized_keys = sample(list(self.full_question_database.keys()), k=amount)
        for key in randomized_keys:
            current_question = self.full_question_database[key]
            shuffle(current_question.options)
            result[key] = current_question
        return result

    def validate_answer(self, question_id: int) -> bool:
        question = self.current_session_question_database[question_id]
        selected = set(self.user_answers.get(question_id, []))
        correct = set(question.correct_option_ids)
        return selected == correct

    def submit_all(self, user_answers: Dict[int, List[str]]) -> None:
        self.user_answers = user_answers

    def count_score(self) -> int:
        score = 0
        for question_id in self.current_session_question_database.keys():
            if self.validate_answer(question_id):
                score += 1
        return score

