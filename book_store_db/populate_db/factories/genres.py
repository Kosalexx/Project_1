from __future__ import annotations
from data_access.dto import GenresDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers import (GenresProvider,
                                    DescriptionProvider)


class GenresFactory:
    def __init__(
            self,
            name_provider: GenresProvider,
            description_provider: DescriptionProvider
    ) -> None:
        self._name_provider = name_provider
        self._description_provider = description_provider

    def generate(self) -> GenresDTO:
        return GenresDTO(
            name=self._name_provider(),
            description=self._description_provider()
        )
