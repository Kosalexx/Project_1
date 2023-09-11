from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dto import BasketsDTO


class BasketsDAO(BaseDAO):

    def create(self, data: BasketsDTO) -> None:
        """Executes data writing to a sqlite table."""
        self._db_gateway.cursor.execute(
            'INSERT INTO baskets (user_id, status_id) VALUES (?, ?);', (
                data.user_id, data.status_id))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        """Gets ids from sqlite table."""
        result = self._db_gateway.cursor.execute(
            'SELECT basket_id FROM baskets;')
        final_result: list[int] = result.fetchall()
        return final_result

    def get_paid_baskets_dao(self) -> list[tuple[int, float]]:
        """Gets ids of baskets from sqlite table where status is "paid"."""
        result = self._db_gateway.cursor.execute(
            'SELECT baskets.basket_id, SUM(books.price * '
            'basket_books.buy_quantity) '
            'FROM baskets '
            'JOIN basket_books ON baskets.basket_id = basket_books.basket_id '
            'JOIN statuses ON baskets.status_id = statuses.status_id '
            'JOIN books ON basket_books.book_id = books.book_id '
            'WHERE statuses.status_name = "paid" '
            'GROUP BY baskets.basket_id;'
        )
        final_result: list[tuple[int, float]] = result.fetchall()
        return final_result
