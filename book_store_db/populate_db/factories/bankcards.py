from __future__ import annotations
from data_access.dto import BankcardsDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers import (RandomValueFromListProvider,
                                    BankCardProvider)


class BankcardsFactory:
    def __init__(
            self,
            bankcard_provider: BankCardProvider,
            user_id_provider: RandomValueFromListProvider
    ):
        self._bankcard_provider = bankcard_provider
        self._user_id_provider = user_id_provider

    def generate(self) -> BankcardsDTO:
        bankcard_data: str = self._bankcard_provider()
        data_list = bankcard_data.split(', ')
        card_number, exp, cvc, card_holder, system = data_list
        holder_first_name, holder_last_name = card_holder.split()
        return BankcardsDTO(
            card_number=card_number,
            holder_first_name=holder_first_name,
            holder_last_name=holder_last_name,
            cvc=int(cvc),
            expiration_date=exp,
            user_id=self._user_id_provider()
        )
