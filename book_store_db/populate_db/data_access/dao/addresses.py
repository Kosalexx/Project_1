from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dto import AddressesDTO


class AddressesDAO(BaseDAO):

    def create(self, data: AddressesDTO) -> None:
        """Executes data writing to a sqlite table."""
        self._db_gateway.cursor.execute(
            'INSERT INTO addresses (street_id, home_number, postcode, user_id)'
            ' VALUES (?, ?, ?, ?);', (
                data.street_id, data.home_number, data.postcode, data.user_id))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        """Gets ids from sqlite table."""
        result = self._db_gateway.cursor.execute(
            'SELECT address_id FROM addresses;')
        final_result: list[int] = result.fetchall()
        return final_result
