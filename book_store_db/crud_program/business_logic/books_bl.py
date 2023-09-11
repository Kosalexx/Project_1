from __future__ import annotations
from data_access.dao import BooksDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from data_access.interfaces import DBGatewayProtocol


class BooksLogic:
    def __init__(
            self,
            db_gateway: DBGatewayProtocol
    ) -> None:
        self._db_gateway = db_gateway
        self._dao = BooksDAO(db_gateway=self._db_gateway)

    def list_of_all_data(self) -> list[dict]:
        data_list = self._dao.get_all_data()
        result_list: list[dict] = []
        for row in data_list:
            data_dict: dict[str, int | str | float] = dict()
            data_dict['ID'] = row.book_id
            data_dict['Name'] = row.name
            data_dict['Pages'] = row.pages
            data_dict['Price'] = row.price
            data_dict['Age limit'] = row.age_limit
            data_dict['Amount'] = row.quantity
            result_list.append(data_dict)
        return result_list

    def get_concrete_info(self, value: str) -> list[dict]:
        data_list = self._dao.get_all_data()
        result_list: list[dict] = []
        integer_id: int = int(value)
        for row in data_list:
            if row.book_id == integer_id:
                data_dict: dict[str, int | str | float | list[str]] = dict()
                data_dict['ID'] = row.book_id
                data_dict['Name'] = row.name
                data_dict['Age limit'] = row.age_limit
                data_dict['Price'] = row.price
                data_dict['Description'] = row.description
                data_dict['Pages'] = row.pages
                data_dict['Amount'] = row.quantity
                data_dict['Authors'] = row.authors
                data_dict['Genres'] = row.genres
                data_dict['Added to shop'] = row.creation_datetime
                result_list.append(data_dict)
        if result_list == []:
            result_dict = {'Result': 'There is no books with the specified '
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
