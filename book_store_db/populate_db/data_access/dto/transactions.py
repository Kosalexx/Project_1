from dataclasses import dataclass


@dataclass
class TransactionsDTO:
    basket_id: int
    bankcard_id: int
    total_price: float
    address_id: int
