from __future__ import annotations
from data_access.dto import StatusesDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers import StatusesProvider


class StatusesFactory:
    def __init__(
            self,
            statuses_provider: StatusesProvider
    ):
        self._statuses_provider = statuses_provider

    def generate(self) -> StatusesDTO:
        return StatusesDTO(
            name=self._statuses_provider()
        )
