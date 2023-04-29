from __future__ import annotations
from data_access.dto import TransactionsDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers import (RandomValueFromListProvider,
                                    RandomTupleValueFromListProvider)


class TransactionsFactory:
    def __init__(
            self,
            paid_basket_provider: RandomTupleValueFromListProvider,
            bankcards_id_provider: RandomValueFromListProvider,
            address_id_provider: RandomValueFromListProvider
    ) -> None:
        self._paid_basket_provider = paid_basket_provider
        self._bankcards_id_provider = bankcards_id_provider
        self._address_id_provider = address_id_provider

    def generate(self) -> TransactionsDTO:
        basket_id, total_price = self._paid_basket_provider()
        return TransactionsDTO(
            basket_id=basket_id,
            bankcard_id=self._bankcards_id_provider(),
            total_price=total_price,
            address_id=self._address_id_provider()
        )
