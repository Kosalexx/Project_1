from __future__ import annotations
from .base import BaseDAO
from data_access.factories import AuthorsFactory
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from data_access.dto import AuthorsDTO


class AuthorsDAO(BaseDAO):
    def get_all_data(self) -> list[AuthorsDTO]:
        data = self._db_gateway.cursor.execute(
            'SELECT * FROM authors ORDER BY first_name, last_name;'
        )
        result_list: list[tuple] = data.fetchall()
        final_list: list[AuthorsDTO] = []
        for row in result_list:
            list_data = list(row)
            data_dto = AuthorsFactory(list_data=list_data).generate_dto()
            final_list.append(data_dto)
        return final_list

    def check_in_data(self, value: int) -> bool:
        data = self._db_gateway.cursor.execute(
            'SELECT first_name FROM authors WHERE author_id = ?', (value, )
        )
        result_list = data.fetchall()
        if result_list == []:
            return False
        else:
            return True

    def delete_data(self, value: int) -> None:
        self._db_gateway.cursor.execute('PRAGMA foreign_keys = ON;')
        self._db_gateway.cursor.execute(
            'DELETE FROM authors WHERE author_id = ?;', (value, ))
        self._db_gateway.connection.commit()

    def update_value(self, integer_id: int, new_value: str) -> None:
        self._db_gateway.cursor.execute(
            'UPDATE authors SET info = ? WHERE author_id = ?;',
            (new_value, integer_id))
        self._db_gateway.connection.commit()
