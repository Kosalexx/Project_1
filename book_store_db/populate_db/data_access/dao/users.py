from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dto import UserDTO


class UserDAO(BaseDAO):
    def create(self, data: UserDTO) -> None:
        """Executes data writing to a sqlite table."""
        self._db_gateway.cursor.execute(
            "INSERT INTO profiles (username, password, age, phone) "
            "VALUES (?, ?, ?, ?);", (
                data.profile.username, data.profile.password, data.profile.age,
                data.profile.phone)
            )
        profile_id = self._db_gateway.cursor.lastrowid
        self._db_gateway.cursor.execute(
            "INSERT INTO users (first_name, last_name, profile_id, email) "
            "VALUES (?, ?, ?, ?);", (
                data.first_name, data.last_name, profile_id, data.email
            ))
        self._db_gateway.connection.commit()

    def get_ids_list(self) -> list[int]:
        """Gets ids from sqlite table."""
        result = self._db_gateway.cursor.execute('SELECT user_id FROM users;')
        final_result: list[int] = result.fetchall()
        return final_result
