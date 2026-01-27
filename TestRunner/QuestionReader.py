from abc import ABC, abstractmethod
import json
from typing import Dict
from TestRunner.Question import Question, Option


class QuestionReader(ABC):
    @abstractmethod
    def read_question(self, file_path: str) -> Dict[int, Question]:
        pass


class JsonQuestionReader(QuestionReader):
    def read_question(self, file_path: str) -> Dict[int, Question]:
        with open(file_path, 'r') as file:
            data = json.load(file)

        result: Dict[int, Question] = dict()

        for question in data["questions"]:
            question_id = question["id"]

            options = [Option(id=o["id"], text=o["text"]) for o in question["options"]]

            result[question_id] = Question(
                title=question["title"],
                options=options,
                correct_option_ids=question["correct_option_ids"],
            )

        return result