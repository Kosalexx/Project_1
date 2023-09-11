from dataclasses import dataclass


@dataclass
class BooksDTO:
    book_id: int
    name: str
    pages: int
    price: float
    age_limit: int
    quantity: int
    description: str
    authors: list[str]
    genres: list[str]
    creation_datetime: str
