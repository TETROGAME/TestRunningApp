from abc import ABC, abstractmethod
import json
class QuestionReader(ABC):
    @abstractmethod
    def read_question(self, file_path: str):
        pass

class JsonQuestionReader(QuestionReader):
    def read_question(self, file_path: str):
        file = open(file_path, 'r')
        data = json.load(file)
        return data