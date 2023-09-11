from __future__ import annotations
from data_access.dto import PermissionsDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers import (PermissionsProvider)


class PermissionsFactory:
    def __init__(
            self,
            permissions_provider: PermissionsProvider
    ):
        self._permissions_provider = permissions_provider

    def generate(self) -> PermissionsDTO:
        name = self._permissions_provider()
        return PermissionsDTO(
            name=name
        )
