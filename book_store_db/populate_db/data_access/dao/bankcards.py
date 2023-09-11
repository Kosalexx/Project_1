from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dto import BankcardsDTO


class BankcardsDAO(BaseDAO):

    def create(self, data: BankcardsDTO) -> None:
        """Executes data writing to a sqlite table."""
        self._db_gateway.cursor.execute(
            'INSERT INTO bankcards (card_number, holder_first_name, '
            'holder_last_name, cvc, expiration_date, user_id) VALUES '
            '(?, ?, ?, ?, ?, ?);', (
                data.card_number, data.holder_first_name,
                data.holder_last_name, data.cvc, data.expiration_date,
                data.user_id))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        """Gets ids from sqlite table."""
        result = self._db_gateway.cursor.execute(
            'SELECT bankcard_id FROM bankcards;')
        final_result: list[int] = result.fetchall()
        return final_result
