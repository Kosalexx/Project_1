from __future__ import annotations
from .base_dao import BaseDAO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dto import RolesPermissionsDTO


class RolesPermissionsDAO(BaseDAO):
    def create(self, data: RolesPermissionsDTO) -> None:
        """Executes data writing to a sqlite table."""
        self._db_gateway.cursor.execute(
            "INSERT INTO roles_permissions (role_id, permission_id) "
            "VALUES (?, ?);", (data.role_id, data.permission_id)
        )
        self._db_gateway.connection.commit()
