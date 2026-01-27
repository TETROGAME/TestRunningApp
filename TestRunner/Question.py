from dataclasses import dataclass
from typing import List, Set

@dataclass
class Option:
    id: str
    text: str

@dataclass
class Question:
    id: int
    title: str
    options: List[Option]
    correct_option_ids: List[str]