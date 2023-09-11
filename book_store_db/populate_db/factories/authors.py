from __future__ import annotations
from data_access.dto import AuthorsDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers import (NameProvider,
                                    LifeDateProvider,
                                    DescriptionProvider)


class AuthorFactory:
    def __init__(
            self,
            name_provider: NameProvider,
            life_date_provider: LifeDateProvider,
            info_provider: DescriptionProvider
    ) -> None:
        self._name_provider = name_provider
        self._life_date_provider = life_date_provider
        self._info_provider = info_provider

    def generate(self) -> AuthorsDTO:
        first_name, last_name = self._name_provider().split()
        birth_date, death_date = self._life_date_provider()
        return AuthorsDTO(
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            death_date=death_date,
            info=self._info_provider()
        )
