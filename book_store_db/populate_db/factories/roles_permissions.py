from __future__ import annotations
from data_access.dto import RolesPermissionsDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers import RandomValueFromListProvider


class RolesPermissionsFactory:
    def __init__(
            self,
            role_id_provider: RandomValueFromListProvider,
            permission_id_provider: RandomValueFromListProvider
    ):
        self._role_id_provider = role_id_provider
        self._permission_id_provider = permission_id_provider

    def generate(self) -> RolesPermissionsDTO:
        return RolesPermissionsDTO(
            role_id=self._role_id_provider(),
            permission_id=self._permission_id_provider()
        )
