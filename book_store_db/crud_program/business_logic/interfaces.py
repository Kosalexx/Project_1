from typing import Protocol


class BusinessLogicProtocol(Protocol):
    def list_of_all_data(self) -> list[dict]:
        raise NotImplementedError

    def get_concrete_info(self, value: str) -> list[dict]:
        raise NotImplementedError

    def check_in_data(self, value: str) -> bool:
        raise NotImplementedError

    def delete_value(self, value: str) -> None:
        raise NotImplementedError

    def update_value(self, str_id: str, new_value: str) -> None:
        raise NotImplementedError
