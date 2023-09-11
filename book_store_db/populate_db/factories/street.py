from __future__ import annotations
from data_access.dto import StreetDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers import StreetProvider, RandomValueFromListProvider


class StreetFactory:
    def __init__(
            self,
            street_provider: StreetProvider,
            random_value_provider: RandomValueFromListProvider
    ):
        self._street_provider = street_provider
        self._random_value_provider = random_value_provider

    def generate(self) -> StreetDTO:
        return StreetDTO(
            name=self._street_provider(),
            city_id=self._random_value_provider()
        )
