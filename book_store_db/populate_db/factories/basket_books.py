from __future__ import annotations
from data_access.dto import BasketBooksDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers import RandomValueFromListProvider


class BasketBooksFactory:
    def __init__(
            self,
            basket_id_provider: RandomValueFromListProvider,
            book_id_provider: RandomValueFromListProvider,
            buy_quantity_provider: RandomValueFromListProvider
    ):
        self._basket_id_provider = basket_id_provider
        self._book_id_provider = book_id_provider
        self._buy_quantity_provider = buy_quantity_provider

    def generate(self) -> BasketBooksDTO:
        return BasketBooksDTO(
            basket_id=self._basket_id_provider(),
            book_id=self._book_id_provider(),
            buy_quantity=self._buy_quantity_provider()
        )
