from __future__ import annotations
from data_access.dto import UsersDTO


class UsersFactory:
    def __init__(
            self,
            list_data: list
    ) -> None:
        self._list_data = list_data

    def generate_dto(self) -> UsersDTO:
        result = UsersDTO(
            user_id=int(self._list_data[0]),
            first_name=str(self._list_data[1]),
            last_name=str(self._list_data[2]),
            email=str(self._list_data[3]),
            phone=self._list_data[4],
            age=int(self._list_data[5]),
            creation_datetime=str(self._list_data[6]),
            roles=self._list_data[7]
        )
        return result
