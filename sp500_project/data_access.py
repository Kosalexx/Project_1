import csv
import json
from abc import ABC, abstractmethod


class IData(ABC):
    @abstractmethod
    def read_data(self):
        raise NotImplementedError

    @abstractmethod
    def check_in_data(self):
        raise NotImplementedError

    @abstractmethod
    def write_to_database(self):
        raise NotImplementedError


class CSVData(IData):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value: str) -> None:
        if value.split(".")[1] != "csv":
            raise ValueError("Invalid file extension.")
        self._file_name = value

    def read_data(self):
        """Reads data from .csv file."""
        with open(self.file_name) as read_file:
            for item in csv.DictReader(read_file):
                yield item

    def check_in_data(
            self,
            symbol_name: str = '',
            company_name: str = '',
            sector: str = ''
            ) -> bool:
        """Checks if the company symbol, name, or sector exists in database."""
        data = self.read_data()
        flag = False
        for row in data:
            if symbol_name == row.get('Symbol'):
                flag = True
                break
            if company_name.lower() == row.get('Name').lower():
                flag = True
                break
            if sector.lower() == row.get('Sector').lower():
                flag = True
                break
        return flag

    def write_to_database(
            self,
            data: list,
            mode: str = "a"
            ) -> None:
        """Writes data into csv file. """
        with open(self.file_name, mode=mode, newline='') as w_file:
            fields = []
            for keys in data[0].keys():
                fields.append(keys)
            file_writer = csv.DictWriter(w_file, fields)
            if mode == 'w':
                file_writer.writeheader()
            file_writer.writerows(data)


class JSONData(IData):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        if value.split(".")[1] != "json":
            raise ValueError("Invalid file extension.")
        self._file_name = value

    def read_data(self):
        """Reads data from .json file."""
        with open(self.file_name) as db_file:
            return json.load(db_file)

    def check_in_data(
            self,
            symbol_name: str = '',
            company_name: str = '',
            sector: str = ''
            ) -> bool:
        """Checks if the company symbol, name,or sector exists in database."""
        data = self.read_data()
        flag = False
        for row in data:
            if symbol_name == row.get('Symbol'):
                flag = True
                break
            if company_name.lower() == row.get('Name').lower():
                flag = True
                break
            if sector.lower() == row.get('Sector').lower():
                flag = True
                break
        return flag

    def write_to_database(
            self,
            data: list,
            mode: str = "a"
            ) -> None:
        """Writes data into json file. """
        if mode == 'a':
            exist_data: list = self.read_data()
            result = {keys: value for keys, value in data[0].items()}
            exist_data.append(result)
            data = exist_data
        with open('sp500.json', mode='w') as file:
            json.dump(data, file, indent=2)
