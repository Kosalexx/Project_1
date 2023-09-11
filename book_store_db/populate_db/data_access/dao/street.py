from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dto import StreetDTO


class StreetDAO(BaseDAO):
    def create(self, data: StreetDTO) -> None:
        """Executes data writing to a sqlite table."""
        self._db_gateway.cursor.execute(
            'INSERT INTO streets (city_id, street_name) '
            'VALUES (?, ?);', (data.city_id, data.name, ))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        """Gets ids from sqlite table."""
        result = self._db_gateway.cursor.execute(
            'SELECT street_id FROM streets;')
        final_result: list[int] = result.fetchall()
        return final_result
