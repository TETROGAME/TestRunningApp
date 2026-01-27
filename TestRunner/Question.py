from dataclasses import dataclass
from typing import List

@dataclass(frozen=True, slots=True)
class Option:
    id: str
    text: str

@dataclass(frozen=True, slots=True)
class Question:
    title: str
    options: List[Option]
    correct_option_ids: List[str]