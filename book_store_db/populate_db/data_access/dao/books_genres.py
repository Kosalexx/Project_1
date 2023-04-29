from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dto import BooksGenresDTO


class BooksGenresDAO(BaseDAO):
    def create(self, data: BooksGenresDTO) -> None:
        """Executes data writing to a sqlite table."""
        self._db_gateway.cursor.execute(
            "INSERT INTO books_genres (book_id, genre_id) "
            "VALUES (?, ?);", (data.book_id, data.genre_id)
        )
        self._db_gateway.connection.commit()
