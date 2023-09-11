import csv
import json


class CSVData:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    @property
    def file_name(self) -> str:
        return self._file_name

    @file_name.setter
    def file_name(self, value: str) -> None:
        if value.split(".")[1] != "csv":
            raise ValueError("Invalid file extension.")
        self._file_name = value

    def read_all_data(self) -> list[dict]:
        """Reads data from .csv file."""
        with open(self.file_name) as read_file:
            result: list[dict] = []
            for item in csv.DictReader(read_file):
                result.append(item)
        return result


class JSONData:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    @property
    def file_name(self) -> str:
        return self._file_name

    @file_name.setter
    def file_name(self, value: str) -> None:
        if value.split(".")[1] != "json":
            raise ValueError("Invalid file extension.")
        self._file_name = value

    def read_all_data(self) -> list[dict]:
        """Reads data from .json file."""
        with open(self.file_name) as db_file:
            all_data: list[dict] = json.load(db_file)
            return all_data
