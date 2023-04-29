from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dto import BasketBooksDTO


class BasketBooksDAO(BaseDAO):
    def create(self, data: BasketBooksDTO) -> None:
        """Executes data writing to a sqlite table."""
        self._db_gateway.cursor.execute(
            "INSERT INTO basket_books (basket_id, book_id, buy_quantity) "
            "VALUES (?, ?, ?);", (
                data.basket_id, data.book_id, data.buy_quantity)
        )
        self._db_gateway.connection.commit()
