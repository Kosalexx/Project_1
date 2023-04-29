from dataclasses import dataclass


@dataclass
class ProfileDTO:
    username: str
    password: str
    age: int
    phone: str


@dataclass
class UserDTO:
    first_name: str
    last_name: str
    email: str
    profile: ProfileDTO
