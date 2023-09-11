from __future__ import annotations
from typing import TYPE_CHECKING, Protocol
if TYPE_CHECKING:
    from sqlite3 import Connection, Cursor


class DBGatewayProtocol(Protocol):
    cursor: Cursor
    connection: Connection


class CreateRecordProtocol(Protocol):
    def create(self, data: object) -> None:
        raise NotImplementedError


class GetIdsListProtocol(Protocol):
    def get_ids_list(self) -> list[int]:
        raise NotImplementedError
