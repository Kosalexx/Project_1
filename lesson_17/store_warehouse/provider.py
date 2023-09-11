from data_access import JSONData
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from interfaces import StorageProtocol


def provide_db(db_file: str, db_type: str) -> 'StorageProtocol':
    """Creates an object of a certain class.

    :param db_file: name of database (Specified in the "config.py" file)
    :type db_fie: str
    :param db_type: type of database file(Specified in the "config.py" file.)
    :typw db_type: str

    :raises ValueError: if given unsupported DB type.
    :rtype: 'StorageProtocol'
    :return: object of StorageProtocol
    """
    if db_type == "json":
        return JSONData(db_file)
    else:
        raise ValueError("Unsupported DB type.")
