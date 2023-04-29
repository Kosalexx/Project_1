from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dto import CountryDTO


class CountryDAO(BaseDAO):

    def create(self, data: CountryDTO) -> None:
        """Executes data writing to a sqlite table."""
        self._db_gateway.cursor.execute(
            'INSERT INTO countries (country_name) VALUES (?);', (data.name, ))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        """Gets ids from sqlite table."""
        result = self._db_gateway.cursor.execute(
            'SELECT country_id FROM countries;')
        final_result: list[int] = result.fetchall()
        return final_result

    def get_country_name(self, country_id: int) -> str:
        """Gets country name using entered country_id."""
        result = self._db_gateway.cursor.execute(
            'SELECT country_name FROM countries WHERE country_id = ?;',
            (country_id,))
        tuple_res = result.fetchone()
        final_res = str(tuple_res[0])
        return final_res
