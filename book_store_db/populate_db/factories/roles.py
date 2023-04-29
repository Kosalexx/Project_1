from __future__ import annotations
from data_access.dto import RolesDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers import RolesProvider


class RolesFactory:
    def __init__(
            self,
            role_provider: RolesProvider
    ):
        self._role_provider = role_provider

    def generate(self) -> RolesDTO:
        return RolesDTO(
            name=self._role_provider()
        )
