from __future__ import annotations
from data_access.dao import AuthorsDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from data_access.interfaces import DBGatewayProtocol


class AuthorsLogic:
    def __init__(
            self,
            db_gateway: DBGatewayProtocol
    ) -> None:
        self._db_gateway = db_gateway
        self._dao = AuthorsDAO(db_gateway=self._db_gateway)

    def list_of_all_data(self) -> list[dict]:
        data_list = self._dao.get_all_data()
        result_list: list[dict] = []
        for row in data_list:
            data_dict = dict()
            data_dict['ID'] = row.author_id
            data_dict['Name'] = row.first_name
            data_dict['Surname'] = row.last_name
            result_list.append(data_dict)
        return result_list

    def get_concrete_info(self, value: str) -> list[dict]:
        data_list = self._dao.get_all_data()
        result_list: list[dict] = []
        integer_id: int = int(value)
        for row in data_list:
            if row.author_id == integer_id:
                data_dict = dict()
                data_dict['ID'] = row.author_id
                data_dict['Name'] = row.first_name
                data_dict['Surname'] = row.last_name
                data_dict['Birth date'] = row.birth_date
                data_dict['Death date'] = row.death_date
                data_dict['Info'] = row.info
                result_list.append(data_dict)
        if result_list == []:
            result_dict = {'Result': 'There is no authors with the specified '
                           'ID in the database.'}
            result_list.append(result_dict)
        return result_list

    def check_in_data(self, value: str) -> bool:
        integer_id = int(value)
        result = self._dao.check_in_data(value=integer_id)
        return result

    def delete_value(self, value: str) -> None:
        integer_id = int(value)
        self._dao.delete_data(value=integer_id)

    def update_value(self, str_id: str, new_value: str) -> None:
        integer_id = int(str_id)
        self._dao.update_value(integer_id=integer_id, new_value=new_value)
