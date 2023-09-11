from dataclasses import dataclass


@dataclass
class AuthorsDTO:
    first_name: str
    last_name: str
    birth_date: str
    death_date: str
    info: str
