from data_access import CSVData, JSONData, SQLiteData
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from interfaces import StorageProtocol


def provide_db(db_file: str, db_type: str) -> 'StorageProtocol':
    if db_type == "csv":
        return CSVData(db_file)
    elif db_type == "json":
        return JSONData(db_file)
    elif db_type == "sqlite" or db_type == "db":
        return SQLiteData(db_file)
    else:
        raise ValueError("Unsupported DB type.")
