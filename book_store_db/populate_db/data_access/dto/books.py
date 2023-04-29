from dataclasses import dataclass


@dataclass
class BooksDTO:
    name: str
    description: str
    pages: int
    format_id: int
    age_limit: int
    amount: int
    price: float
