from data_access import CSVData, JSONData
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from data_access_module.interfaces import StorageProtocol


def provide_data_file(file_name: str) -> 'StorageProtocol':
    """Provides correct object to work with the database."""
    if file_name.endswith('.json'):
        return JSONData(file_name=file_name)
    elif file_name.endswith('.csv'):
        return CSVData(file_name=file_name)
