import os
from typing import Dict, List
from TestRunner.Question import Question
from TestRunner.QuestionReader import JsonQuestionReader


class QuestionLoader:
    file_readers: Dict
    def __init__(self) -> None:
        self.file_readers = {
            ".json": JsonQuestionReader()
        }
    def load(self, file_path: str) -> List[Question]:
        _, extension = os.path.splitext(file_path)
        if extension in self.file_readers.keys():
            file_reader = self.file_readers.get(extension)
            return file_reader.read_question(file_path)
        else:
            raise ValueError(f"{extension} is not supported")

