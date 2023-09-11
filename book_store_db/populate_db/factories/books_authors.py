from __future__ import annotations
from data_access.dto import BooksAuthorsDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers import RandomValueFromListProvider


class BooksAuthorsFactory:
    def __init__(
            self,
            book_id_provider: RandomValueFromListProvider,
            author_id_provider: RandomValueFromListProvider
    ):
        self._book_id_provider = book_id_provider
        self._author_id_provider = author_id_provider

    def generate(self) -> BooksAuthorsDTO:
        return BooksAuthorsDTO(
            book_id=self._book_id_provider(),
            author_id=self._author_id_provider()
        )
