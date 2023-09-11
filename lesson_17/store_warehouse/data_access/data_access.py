import json
from typing import Literal, TypeAlias, Any

DataTyping: TypeAlias = list[dict[str, Any]]


class BaseProvider:
    """ Base provider Class. Not intended to create objects."""
    AVAILABLE_EXTENSIONS: tuple

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    @property
    def file_name(self) -> str:
        return self._file_name

    @file_name.setter
    def file_name(self, value: str) -> None:
        if value.split(".")[1] not in self.AVAILABLE_EXTENSIONS:
            raise ValueError("Invalid file extension.")
        self._file_name = './data_access/' + value


class JSONData(BaseProvider):
    """Provider to work with json files."""
    AVAILABLE_EXTENSIONS: tuple = ('json', )

    def read_data(self) -> 'DataTyping':
        """Reads data from .json file."""
        with open(self.file_name) as db_file:
            data: DataTyping = json.load(db_file)
            return data

    def write_to_data(
            self,
            data: 'DataTyping',
            mode: Literal['w', 'a'] = 'w') -> None:
        """Writes data into json file. """
        if mode == 'a':
            exist_data: DataTyping = self.read_data()
            result = {keys: value for keys, value in data[0].items()}
            exist_data.append(result)
            data = exist_data
        with open(self.file_name, mode='w') as file:
            json.dump(data, file, indent=2)
