from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dto import FormatsDTO


class FormatDAO(BaseDAO):
    def create(self, data: FormatsDTO) -> None:
        """Executes data writing to a sqlite table."""
        self._db_gateway.cursor.execute(
            'INSERT INTO formats (format_name) VALUES (?);', (
                data.format_name, ))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        """Gets ids from sqlite table."""
        result = self._db_gateway.cursor.execute(
            'SELECT format_id FROM formats;')
        final_result: list[int] = result.fetchall()
        return final_result
