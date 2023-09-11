from dataclasses import dataclass


@dataclass
class BasketBooksDTO:
    basket_id: int
    book_id: int
    buy_quantity: int
