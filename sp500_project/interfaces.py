from typing import Protocol, TYPE_CHECKING


if TYPE_CHECKING:
    from data_access import DataTyping


class StorageProtocol(Protocol):
    def read_data(self) -> DataTyping:
        raise NotImplementedError

    def check_in_data(
            self,
            symbol_name: str = '',
            company_name: str = '',
            sector: str = ''
            ) -> bool:
        raise NotImplementedError

    def write_to_database(
            self,
            data: DataTyping,
            mode: str = "a"
            ) -> None:
        raise NotImplementedError
