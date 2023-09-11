from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dto import BooksDTO


class BooksDAO(BaseDAO):

    def create(self, data: BooksDTO) -> None:
        """Executes data writing to a sqlite table."""
        self._db_gateway.cursor.execute(
            'INSERT INTO books (name, description, pages, format_id, '
            'age_limit, amount, price) VALUES (?, ?, ?, ?, ?, ?, ?);', (
                data.name, data.description, data.pages, data.format_id,
                data.age_limit, data.amount, data.price))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        """Gets ids from sqlite table."""
        result = self._db_gateway.cursor.execute(
            'SELECT book_id FROM books;')
        final_result: list[int] = result.fetchall()
        return final_result
