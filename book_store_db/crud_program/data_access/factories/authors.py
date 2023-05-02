from __future__ import annotations
from data_access.dto import AuthorsDTO


class AuthorsFactory:
    def __init__(
            self,
            list_data: list
    ) -> None:
        self._list_data = list_data

    def generate_dto(self) -> AuthorsDTO:
        result = AuthorsDTO(
            author_id=int(self._list_data[0]),
            first_name=str(self._list_data[1]),
            last_name=str(self._list_data[2]),
            birth_date=str(self._list_data[3]),
            death_date=str(self._list_data[4]),
            info=str(self._list_data[5])
        )
        return result
