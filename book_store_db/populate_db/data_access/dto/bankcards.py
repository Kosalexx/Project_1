from dataclasses import dataclass


@dataclass
class BankcardsDTO:
    card_number: str
    holder_first_name: str
    holder_last_name: str
    cvc: int
    expiration_date: str
    user_id: int
