from __future__ import annotations
from data_access.dto import AddressesDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers import (RandomValueFromListProvider)


class AddressesFactory:
    def __init__(
            self,
            street_id_provider: RandomValueFromListProvider,
            home_number_provider: RandomValueFromListProvider,
            postcode_provider: RandomValueFromListProvider,
            user_id_provider: RandomValueFromListProvider
    ) -> None:
        self._street_id_provider = street_id_provider
        self._home_number_provider = home_number_provider
        self._postcode_provider = postcode_provider
        self._user_id_provider = user_id_provider

    def generate(self) -> AddressesDTO:
        return AddressesDTO(
            street_id=self._street_id_provider(),
            home_number=self._home_number_provider(),
            postcode=self._postcode_provider(),
            user_id=self._user_id_provider()
        )
