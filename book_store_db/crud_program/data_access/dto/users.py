from dataclasses import dataclass


@dataclass
class UsersDTO:
    user_id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    age: int
    creation_datetime: str
    roles: list[str]
