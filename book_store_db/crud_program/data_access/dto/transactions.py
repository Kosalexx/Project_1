from dataclasses import dataclass


@dataclass
class TransactionsDTO:
    user_name: str
    bankcard: str
    total_sum: float
    transaction_date: str
    address: str
    tr_id: int
