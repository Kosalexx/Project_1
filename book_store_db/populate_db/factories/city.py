from __future__ import annotations
from data_access.dto import CityDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers import (CityProvider,
                                    RandomValueFromListProvider)
    from data_access.dao import CountryDAO


class CityFactory:
    def __init__(
            self,
            random_value_provider: RandomValueFromListProvider,
            city_provider: CityProvider,
            country_dao: CountryDAO
    ):
        self._random_value_provider = random_value_provider
        self._city_provider = city_provider
        self._country_dao = country_dao

    def generate(self) -> CityDTO:
        country_id = self._random_value_provider()
        country_name = self._country_dao.get_country_name(country_id)
        city_name = self._city_provider(country_name=country_name)
        return CityDTO(
            country_id=country_id,
            name=city_name
        )
