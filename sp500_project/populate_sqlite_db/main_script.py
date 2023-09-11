from db_path_provider import provide_path_to_sqlite_db
from provide_data_file import provide_data_file
from data_access_module import (CompaniesDAO, CompaniesFactory, SqliteGateway)
from populate_table import PopulateTable


def populate_db(db_name: str, file_name: str) -> None:
    """Populates sqlite database with data from json or csv file."""
    db_path = provide_path_to_sqlite_db(db_name)
    db_gateway = SqliteGateway(db_name=db_path)
    dao = CompaniesDAO(db_gateway=db_gateway)
    fake_factory = CompaniesFactory(
        data_provider=provide_data_file(file_name=file_name)
    )
    PopulateTable(
        dao=dao,
        fake_factory=fake_factory
    ).execute()
