from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dto import AuthorsDTO


class AuthorsDAO(BaseDAO):

    def create(self, data: AuthorsDTO) -> None:
        """Executes data writing to a sqlite table."""
        self._db_gateway.cursor.execute(
            'INSERT INTO authors (first_name, last_name, birth_date, '
            'death_date, info) VALUES (?, ?, ?, ?, ?);', (
                data.first_name, data.last_name, data.birth_date,
                data.death_date, data.info))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        """Gets ids from sqlite table."""
        result = self._db_gateway.cursor.execute(
            'SELECT author_id FROM authors;')
        final_result: list[int] = result.fetchall()
        return final_result
