from typing import Protocol, TYPE_CHECKING, Literal
if TYPE_CHECKING:
    from data_access import DataTyping


class StorageProtocol(Protocol):
    def read_data(self) -> 'DataTyping':
        raise NotImplementedError

    def write_to_data(
            self,
            data: 'DataTyping',
            mode: Literal['w', 'a'] = 'w') -> None:
        raise NotImplementedError
