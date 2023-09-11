from __future__ import annotations
from data_access.dto import BooksDTO


class BooksFactory:
    def __init__(
            self,
            list_data: list
    ) -> None:
        self._list_data = list_data

    def generate_dto(self) -> BooksDTO:
        result = BooksDTO(
            book_id=int(self._list_data[0]),
            name=str(self._list_data[1]),
            description=str(self._list_data[2]),
            pages=int(self._list_data[3]),
            age_limit=int(self._list_data[5]),
            quantity=int(self._list_data[6]),
            price=float(self._list_data[7]),
            creation_datetime=str(self._list_data[8]),
            genres=self._list_data[10],
            authors=self._list_data[11]
        )
        return result
