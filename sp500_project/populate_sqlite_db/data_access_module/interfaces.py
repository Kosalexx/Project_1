from __future__ import annotations
from typing import TYPE_CHECKING, Protocol
if TYPE_CHECKING:
    from sqlite3 import Connection, Cursor
    from dto import CompaniesDTO


class DBGatewayProtocol(Protocol):
    cursor: Cursor
    connection: Connection


class CreateRecordProtocol(Protocol):
    def create(self, data: CompaniesDTO) -> None:
        raise NotImplementedError


class ReadDataProtocol(Protocol):
    def read_all_data(self) -> list[dict]:
        raise NotImplementedError


class FakeFactoryProtocol(Protocol):
    def generate(self) -> list[object]:
        raise NotImplementedError


class StorageProtocol(Protocol):
    def read_data(self) -> list[dict]:
        raise NotImplementedError
