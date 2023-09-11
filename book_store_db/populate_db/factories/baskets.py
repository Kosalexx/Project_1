from __future__ import annotations
from data_access.dto import BasketsDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers import RandomValueFromListProvider


class BasketsFactory:
    def __init__(
            self,
            user_id_provider: RandomValueFromListProvider,
            status_id_provider: RandomValueFromListProvider
    ):
        self._user_id_provider = user_id_provider
        self._status_id_provider = status_id_provider

    def generate(self) -> BasketsDTO:
        return BasketsDTO(
            user_id=self._user_id_provider(),
            status_id=self._status_id_provider()
        )
