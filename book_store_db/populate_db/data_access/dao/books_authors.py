from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dto import BooksAuthorsDTO


class BooksAuthorsDAO(BaseDAO):
    def create(self, data: BooksAuthorsDTO) -> None:
        """Executes data writing to a sqlite table."""
        self._db_gateway.cursor.execute(
            "INSERT INTO books_authors (book_id, author_id) "
            "VALUES (?, ?);", (data.book_id, data.author_id)
        )
        self._db_gateway.connection.commit()
