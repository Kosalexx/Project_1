from __future__ import annotations
from data_access.dto import UsersRolesDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fake_lib.providers import RandomValueFromListProvider


class UsersRolesFactory:
    def __init__(
            self,
            user_id_provider: RandomValueFromListProvider,
            role_id_provider: RandomValueFromListProvider
    ):
        self._user_id_provider = user_id_provider
        self._role_id_provider = role_id_provider

    def generate(self) -> UsersRolesDTO:
        return UsersRolesDTO(
            user_id=self._user_id_provider(),
            role_id=self._role_id_provider()
        )
