from __future__ import annotations
from data_access.dto import BooksGenresDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers import RandomValueFromListProvider


class BooksGenresFactory:
    def __init__(
            self,
            book_id_provider: RandomValueFromListProvider,
            genre_id_provider: RandomValueFromListProvider
    ):
        self._book_id_provider = book_id_provider
        self._genre_id_provider = genre_id_provider

    def generate(self) -> BooksGenresDTO:
        return BooksGenresDTO(
            book_id=self._book_id_provider(),
            genre_id=self._genre_id_provider()
        )
