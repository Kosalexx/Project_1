from dataclasses import dataclass


@dataclass
class RolesPermissionsDTO:
    role_id: int
    permission_id: int
