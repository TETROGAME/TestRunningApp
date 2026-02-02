import os
from typing import Dict
from TestRunner.Question import Question
from TestRunner.QuestionReader import JSONQuestionReader, CVSQuestionReader


class QuestionLoader:
    def __init__(self) -> None:
        self.file_readers = {
            ".json": JSONQuestionReader(),
            ".csv": CVSQuestionReader()
        }

    def load(self, file_path: str) -> Dict[int, Question]:
        _, extension = os.path.splitext(file_path)
        if extension in self.file_readers:
            return self.file_readers[extension].read_question(file_path)
        raise ValueError(f"{extension} is not supported")