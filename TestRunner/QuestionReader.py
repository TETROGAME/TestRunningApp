from abc import ABC, abstractmethod
import json, csv
from typing import Dict, List
from TestRunner.Question import Question, Option


class QuestionReader(ABC):
    @abstractmethod
    def read_question(self, file_path: str) -> Dict[int, Question]:
        pass


class JSONQuestionReader(QuestionReader):
    def read_question(self, file_path: str) -> Dict[int, Question]:
        with open(file_path, 'r', encoding="utf-8") as file:
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




class CVSQuestionReader(QuestionReader):
    def __parse_answer_options(self, raw_options: str) -> List[Option]:
        id_with_answer = raw_options.split("|")

        result: List[Option] = list()
        for line in id_with_answer:
            question_id, option = line.split(":")
            result.append(Option(
                id=question_id,
                text=option
            ))
        return result
    def __parse_correct_option_ids(self, raw_correct_option_ids: str) -> List[str]:
        return raw_correct_option_ids.split("|")

    def read_question(self, file_path: str) -> Dict[int, Question]:
        with open(file_path, 'r', encoding="utf-8") as file:
            data = csv.reader(file)
            next(data)
            result: Dict[int, Question] = dict()

            for question in data:
                try:
                    question_id = int(question[0])
                except ValueError:
                    print(f"Question id {question[0]} does not seem to be an integer")
                    question_id = -1
                text = question[1]
                answer_options = self.__parse_answer_options(question[2])
                correct_option_ids = self.__parse_correct_option_ids(question[3])
                result[question_id] = Question(
                    title=text,
                    options=answer_options,
                    correct_option_ids=correct_option_ids,
                )
        return result

