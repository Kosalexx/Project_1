from __future__ import annotations
from .base import BaseDAO
from data_access.factories import UsersFactory
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from data_access.dto import UsersDTO


class UsersDAO(BaseDAO):
    def get_all_data(self) -> list[UsersDTO]:
        data = self._db_gateway.cursor.execute(
            'SELECT users.user_id, users.first_name, users.last_name, '
            'users.email, profiles.phone, profiles.age, '
            'users.creation_datetime FROM users '
            'JOIN profiles ON users.profile_id = profiles.profile_id '
            'ORDER BY users.first_name, users.last_name;'
        )
        result_list: list[tuple] = data.fetchall()
        final_list: list[UsersDTO] = []
        for row in result_list:
            list_data = list(row)
            us_id = row[0]
            roles = self._db_gateway.cursor.execute(
                'SELECT roles.name FROM roles '
                'JOIN users_roles ON roles.role_id = users_roles.role_id '
                'WHERE user_id = ?;', (us_id, )
            )
            roles_list = roles.fetchall()
            res_list: list[tuple] = []
            for role in roles_list:
                res_list.append(*role)
            list_data.append(res_list)
            data_dto = UsersFactory(list_data=list_data).generate_dto()
            final_list.append(data_dto)
        return final_list

    def check_in_data(self, value: int) -> bool:
        data = self._db_gateway.cursor.execute(
            'SELECT first_name FROM users WHERE user_id = ?', (value, )
        )
        result_list = data.fetchall()
        if result_list == []:
            return False
        else:
            return True

    def delete_data(self, value: int) -> None:
        self._db_gateway.cursor.execute('PRAGMA foreign_keys = ON;')
        self._db_gateway.cursor.execute(
            'DELETE FROM users WHERE user_id = ?;', (value, ))
        self._db_gateway.connection.commit()

    def update_value(self, integer_id: int, new_value: str) -> None:
        if len(new_value.split('@')) == 2:
            self._db_gateway.cursor.execute(
                'UPDATE users SET email = ? WHERE user_id = ?;',
                (new_value, integer_id))
            self._db_gateway.connection.commit()
        else:
            self._db_gateway.cursor.execute(
                'UPDATE profiles SET phone = ? WHERE profile_id = ?;',
                (new_value, integer_id))
            self._db_gateway.connection.commit()
