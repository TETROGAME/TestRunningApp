from dataclasses import dataclass
from typing import List


@dataclass
class Question:
    id: int
    title: str
    options: List[str]
    correct_answer_id: List[int]