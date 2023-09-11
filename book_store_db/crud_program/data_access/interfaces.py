from typing import Protocol, TYPE_CHECKING
if TYPE_CHECKING:
    from sqlite3 import Connection, Cursor


class DBGatewayProtocol(Protocol):
    cursor: Cursor
    connection: Connection


class DataAccessProtocol(Protocol):
    def get_all_data(self) -> list[object]:
        raise NotImplementedError

    def check_in_data(self, value: int) -> bool:
        raise NotImplementedError

    def delete_data(self, value: int) -> None:
        raise NotImplementedError

    def update_value(self, integer_id: int, new_value: str) -> None:
        raise NotImplementedError


class DataFactoryProtocol(Protocol):
    def generate_dto(self) -> object:
        raise NotImplementedError
