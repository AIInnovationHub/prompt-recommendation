from dataclasses import dataclass


@dataclass
class User:
    user_id: str
    username: str
    password: str
    age: int
    gender: str
