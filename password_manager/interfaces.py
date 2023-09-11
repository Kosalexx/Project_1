from typing import Protocol, Literal, Optional


class StorageProtocol(Protocol):
    def read_data(self) -> dict[str, str]:
        raise NotImplementedError

    def key_exist(self) -> Optional[str]:
        raise NotImplementedError

    def write_data(
            self,
            data_dict: dict[str, str],
            mode: Literal['w', 'a']) -> None:
        raise NotImplementedError


class ExportProtocol(Protocol):
    def create_export_file(self, pass_data: dict[str, str]) -> None:
        raise NotImplementedError
