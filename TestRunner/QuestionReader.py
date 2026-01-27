from abc import ABC, abstractmethod
import json
from typing import List
from TestRunner.Question import Question, Option


class QuestionReader(ABC):
    @abstractmethod
    def read_question(self, file_path: str) -> List[Question]:
        pass

class JsonQuestionReader(QuestionReader):
    def read_question(self, file_path: str) -> List[Question]:
        file = open(file_path, 'r')
        data = json.load(file)
        result = list()

        for question in data['questions']:
            options = [Option(id=option['id'], text=option['text']) for option in question['options']]
            result.append(Question(
                id=question['id'],
                title=question['title'],
                options=options,
                correct_option_ids=question['correct_option_ids']))
        return result