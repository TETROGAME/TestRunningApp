from abc import ABC, abstractmethod
import json
from typing import List
from Question import Question

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
            result.append(Question(
                question['id'],
                question['title'],
                question['options'],
                question['correct_answer_id']))
        return result