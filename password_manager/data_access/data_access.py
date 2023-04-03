import json
import csv
import openpyxl
import xml.etree.ElementTree as Et
from xml.dom import minidom
from typing import Optional, Literal


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

    def read_data(self) -> dict[str, str]:
        """Reads data from .json file."""
        with open(self.file_name) as db_file:
            data: dict = json.load(db_file)
            return data

    def key_exist(self) -> Optional[str]:
        data = self.read_data()
        result = data.get('key')
        return result

    def write_data(self,
                   data_dict: dict[str, str],
                   mode: Literal['w', 'a']) -> None:
        if mode == 'a':
            exist_data: dict[str, str] = self.read_data()
        else:
            exist_data = {}
        for field, item in data_dict.items():
            exist_data[field] = item
        with open(self.file_name, mode='w') as db_file:
            json.dump(exist_data, db_file, indent=2)


class BaseExportClass:
    """ Base export class. Not intended to create objects."""
    AVAILABLE_EXTENSIONS: tuple = ('xlsx', 'csv', 'txt', 'xml')

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    @property
    def file_name(self) -> str:
        return self._file_name

    @file_name.setter
    def file_name(self, value: str) -> None:
        if value.split(".")[1] not in self.AVAILABLE_EXTENSIONS:
            raise ValueError("Invalid file extension.")
        self._file_name = f'./data_access/{value}'


class ExcelFile(BaseExportClass):
    """Designed to create an "excel" file and export user passwords to it."""

    def create_export_file(self, pass_data: dict[str, str]) -> None:
        """Creates an "excel" file and exports user passwords to it.

        :param pass_data: dict with user passwords information
        :type pass_data: dict[str, str]
        """
        wb = openpyxl.Workbook()
        new_sheet = wb.active
        new_sheet.title = 'My_passwords'
        for key, value in pass_data.items():
            new_sheet.append([key, value])
        new_sheet.column_dimensions['A'].width = 15
        new_sheet.column_dimensions['B'].width = 30
        wb.save(self.file_name)


class CSVFile(BaseExportClass):
    """Designed to create an "csv" file and export user passwords to it."""

    def create_export_file(self, pass_data: dict[str, str]) -> None:
        """Creates an "csv" file and exports user passwords to it.

        :param pass_data: dict with user passwords information
        :type pass_data: dict[str, str]
        """
        fields: list[str] = []
        for key in pass_data.keys():
            fields.append(key)
        with open(self.file_name, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerow(pass_data)


class TXTFile(BaseExportClass):
    """Designed to create an "txt" file and export user passwords to it."""

    def create_export_file(self, pass_data: dict[str, str]) -> None:
        """Creates an "txt" file and exports user passwords to it.

        :param pass_data: dict with user passwords information
        :type pass_data: dict[str, str]
        """
        write_data: str = 'My_passwords:\n'
        for key, value in pass_data.items():
            write_data += f'{key}: {value}\n'
        with open(self.file_name, "w") as file:
            file.write(write_data)


class XMLFile(BaseExportClass):
    """Designed to create an "xml" file and export user passwords to it."""

    def create_export_file(self, pass_data: dict[str, str]) -> None:
        """Creates an "xml" file and exports user passwords to it.

        :param pass_data: dict with user passwords information
        :type pass_data: dict[str, str]
        """
        root = Et.Element('Passwords')
        for identifier, password in pass_data.items():
            pas = Et.SubElement(root, 'password')
            pas.set('identifier', identifier)
            value = Et.SubElement(pas, 'value')
            value.text = password
        string_tree = Et.tostring(root)
        parsed = minidom.parseString(string_tree)
        xml_data = parsed.toprettyxml(indent="    ")
        with open(self.file_name, 'w') as file:
            file.write(xml_data)
