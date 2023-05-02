from __future__ import annotations
from data_access.dto import TransactionsDTO


class TransactionsFactory:
    def __init__(
            self,
            list_data: list
    ) -> None:
        self._list_data = list_data

    def generate_dto(self) -> TransactionsDTO:
        result = TransactionsDTO(
            user_name=(str(self._list_data[0]) + ' ' +
                       str(self._list_data[1])),
            bankcard=str(self._list_data[2]),
            total_sum=float(self._list_data[3]),
            transaction_date=str(self._list_data[4]),
            address=(
                str(self._list_data[5]) + ', ' + str(self._list_data[6]) +
                ', ' + str(self._list_data[7]) + ', ' + str(self._list_data[8])
                + ', ' + str(self._list_data[9])),
            tr_id=int(self._list_data[10])
        )
        return result
