from data_access import (JSONData, ExcelFile, TXTFile, XMLFile, CSVFile)
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from interfaces import StorageProtocol, ExportProtocol


def provide_db(db_file: str, db_type: str) -> 'StorageProtocol':
    """Creates an object of a certain class.

    :param db_file: name of database (Specified in the "config.py" file)
    :type db_fie: str
    :param db_type: type of database file(Specified in the "config.py" file.)
    :type db_type: str

    :raises ValueError: if given unsupported DB type.

    :rtype: 'StorageProtocol'
    :return: object of StorageProtocol
    """
    if db_type == "json":
        return JSONData(db_file)
    else:
        raise ValueError("Unsupported DB type.")


def provide_passwords_file(file_type: str) -> 'ExportProtocol':
    """Creates an object of a certain class.

    :param file_type: name of database (Specified in the "config.py" file)
    :type file_type: str

    :raises ValueError: if given unsupported type of export file.

    :rtype: 'ExportProtocol'
    :return: object of ExportProtocol
    """
    file_name = 'my_passwords.'
    if file_type == 'excel':
        file_name += 'xlsx'
        return ExcelFile(file_name)
    if file_type == 'csv':
        file_name += 'csv'
        return CSVFile(file_name)
    if file_type == 'txt':
        file_name += 'txt'
        return TXTFile(file_name)
    if file_type == 'xml':
        file_name += 'xml'
        return XMLFile(file_name)
    else:
        raise ValueError("Unsupported type of export file.")
