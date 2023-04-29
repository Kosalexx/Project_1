from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dto import TransactionsDTO


class TransactionsDAO(BaseDAO):

    def create(self, data: TransactionsDTO) -> None:
        """Executes data writing to a sqlite table."""
        self._db_gateway.cursor.execute(
            'INSERT INTO transactions (basket_id, bankcard_id, total_price, '
            'address_id) VALUES (?, ?, ?, ?);', (
                data.basket_id, data.bankcard_id, data.total_price,
                data.address_id)
            )
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        """Gets ids from sqlite table."""
        result = self._db_gateway.cursor.execute(
            'SELECT transaction_id FROM transactions;')
        final_result: list[int] = result.fetchall()
        return final_result
