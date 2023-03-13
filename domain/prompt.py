from dataclasses import dataclass
from typing import List

from domain.tags import Tags


@dataclass
class Prompt:
    id: str
    user_id: str
    prompt: str
    favorite_count: int
    category: str
    tags: List[Tags]
