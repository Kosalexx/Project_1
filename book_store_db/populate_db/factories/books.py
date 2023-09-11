from __future__ import annotations
from data_access.dto import BooksDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers import (BookNameProvider,
                                    RandomValueFromListProvider,
                                    DescriptionProvider,
                                    PriceProvider)


class BooksFactory:
    def __init__(
            self,
            name_provider: BookNameProvider,
            description_provider: DescriptionProvider,
            pages_provider: RandomValueFromListProvider,
            format_id_provider: RandomValueFromListProvider,
            age_limit_provider: RandomValueFromListProvider,
            amount_provider: RandomValueFromListProvider,
            price_provider: PriceProvider
    ) -> None:
        self._name_provider = name_provider
        self._description_provider = description_provider
        self._pages_provider = pages_provider
        self._format_id_provider = format_id_provider
        self._age_limit_provider = age_limit_provider
        self._amount_provider = amount_provider
        self._price_provider = price_provider

    def generate(self) -> BooksDTO:
        return BooksDTO(
            name=self._name_provider(),
            description=self._description_provider(),
            pages=self._pages_provider(),
            format_id=self._format_id_provider(),
            age_limit=self._age_limit_provider(),
            amount=self._amount_provider(),
            price=self._price_provider()
        )
