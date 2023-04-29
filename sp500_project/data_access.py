import csv
import json
import sqlite3
from dataclasses import dataclass
from typing import TypeAlias, TYPE_CHECKING
if TYPE_CHECKING:
    from sqlite3 import Connection, Cursor


@dataclass
class CompaniesDTO:
    symbol: str
    name: str
    sector: str
    price: str


DataTyping: TypeAlias = list[CompaniesDTO]


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

    def read_data(self) -> DataTyping:
        """Reads data from .csv file."""
        with open(self.file_name) as read_file:
            result: DataTyping = []
            for item in csv.DictReader(read_file):
                data = CompaniesDTO(
                    symbol=item['Symbol'],
                    name=item['Name'],
                    sector=item['Sector'],
                    price=item['Price']
                )
                result.append(data)
        return result

    def check_in_data(
            self,
            symbol_name: str = '',
            company_name: str = '',
            sector: str = ''
            ) -> bool:
        """Checks if the company symbol, name, or sector exists in database."""
        data = self.read_data()
        flag: bool = False
        for row in data:
            if symbol_name == row.symbol:
                flag = True
                break
            if company_name.lower() == row.name:
                flag = True
                break
            if sector.lower() == row.sector.lower():
                flag = True
                break
        return flag

    def write_to_database(
            self,
            data: DataTyping,
            mode: str = "a"
            ) -> None:
        """Writes data into csv file. """
        with open(self.file_name, mode=mode, newline='') as w_file:
            fields: list = ['Symbol', 'Name', 'Sector', 'Price']
            result_list = []
            file_writer = csv.DictWriter(w_file, fields)
            if mode == 'w':
                file_writer.writeheader()
            for row in data:
                data_dict = {
                    "Symbol": row.symbol,
                    "Name": row.name,
                    "Sector": row.sector,
                    "Price": row.price
                }
                result_list.append(data_dict)
            file_writer.writerows(result_list)

    def delete_all_data(self) -> None:
        """Deletes all data from database."""
        self.write_to_database(data=[], mode='w')


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

    def read_data(self) -> DataTyping:
        """Reads data from .json file."""
        with open(self.file_name) as db_file:
            result_list: DataTyping = []
            all_data: list[dict] = json.load(db_file)
            for row in all_data:
                data = CompaniesDTO(
                        symbol=row['Symbol'],
                        name=row['Name'],
                        sector=row['Sector'],
                        price=row['Price']
                    )
                result_list.append(data)
            return result_list

    def check_in_data(
            self,
            symbol_name: str = '',
            company_name: str = '',
            sector: str = ''
            ) -> bool:
        """Checks if the company symbol, name,or sector exists in database."""
        data = self.read_data()
        flag: bool = False
        for row in data:
            if symbol_name == row.symbol:
                flag = True
                break
            if company_name.lower() == row.name:
                flag = True
                break
            if sector.lower() == row.sector.lower():
                flag = True
                break
        return flag

    def write_to_database(
            self,
            data: DataTyping,
            mode: str = "a"
            ) -> None:
        """Writes data into json file. """
        result_list = []
        if mode == 'a':
            exist_data: DataTyping = self.read_data()
            for dto in exist_data:
                data_dict = {
                    "Symbol": dto.symbol,
                    "Name": dto.name,
                    "Sector": dto.sector,
                    "Price": dto.price
                    }
                result_list.append(data_dict)
        for row in data:
            data_dict = {
                "Symbol": row.symbol,
                "Name": row.name,
                "Sector": row.sector,
                "Price": row.price
                }
            result_list.append(data_dict)
        with open('sp500.json', mode='w') as file:
            json.dump(result_list, file, indent=2)

    def delete_all_data(self) -> None:
        """Deletes all data from database."""
        self.write_to_database(data=[], mode='w')


class SQLiteData:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.connection = self._create_connection()
        self.cursor = self._create_cursor()

    def _create_connection(self) -> 'Connection':
        return sqlite3.connect(self.file_name)

    def _create_cursor(self) -> 'Cursor':
        return self.connection.cursor()

    @property
    def file_name(self) -> str:
        return self._file_name

    @file_name.setter
    def file_name(self, value: str) -> None:
        if value.split(".")[1] != "db":
            raise ValueError("Invalid file extension.")
        self._file_name = value

    def read_data(self) -> DataTyping:
        """Reads data from sqlite database."""
        result_list = []
        data = self.cursor.execute(
            'SELECT symbol, name, sector, price FROM sp500;')
        all_data: list[tuple] = data.fetchall()
        for row in all_data:
            dto = CompaniesDTO(
                symbol=row[0],
                name=row[1],
                sector=row[2],
                price=row[3])
            result_list.append(dto)
        return result_list

    def check_in_data(
            self,
            symbol_name: str = '',
            company_name: str = '',
            sector: str = ''
            ) -> bool:
        """Checks if the company symbol, name,or sector exists in database."""
        data = self.read_data()
        flag: bool = False
        for row in data:
            if symbol_name == row.symbol:
                flag = True
                break
            if company_name.lower() == row.name:
                flag = True
                break
            if sector.lower() == row.sector.lower():
                flag = True
                break
        return flag

    def write_to_database(
            self,
            data: DataTyping,
            mode: str = "a"
            ) -> None:
        """Writes data into sqlite database. """
        if mode == 'w':
            self.cursor.execute(
                'DELETE FROM sp500;'
            )
        for row in data:
            self.cursor.execute(
                'INSERT INTO sp500 (symbol, name, sector, price) VALUES '
                '(?, ?, ?, ?);', (row.symbol, row.name, row.sector, row.price)
            )
            self.connection.commit()

    def delete_all_data(self) -> None:
        """Deletes all data from database."""
        self.cursor.execute('DELETE FROM sp500;')
        self.connection.commit()
