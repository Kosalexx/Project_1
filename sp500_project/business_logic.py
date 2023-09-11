from faker import Faker
from faker.providers import DynamicProvider
from random import uniform, randrange
from my_cache import cache
from data_access import CompaniesDTO, DataTyping
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from interfaces import StorageProtocol


@cache(30)
def find_by_name(
    name: str,
    db_connector: 'StorageProtocol'
        ) -> str:
    """ Finds a company by name in the database. """
    answer: str = ''
    data = db_connector.read_data()
    for row in data:
        if name in row.name.lower():
            answer += (f'"Name": {row.name}, '
                       f'"Symbol": {row.symbol}, '
                       f'"Sector": {row.sector}, '
                       f'"Stock Price": {row.price}.\n')
    if len(answer) == 0:
        return "There aren't any companies that match the request."
    else:
        return answer


@cache(30)
def find_by_symbol(
    symbol: str,
    db_connector: 'StorageProtocol'
        ) -> str:
    """ Finds a company by symbol in the database. """
    answer: str = ''
    data = db_connector.read_data()
    for row in data:
        if symbol.upper() in row.symbol.upper():
            answer += (f'"Name": {row.name}, '
                       f'"Symbol": {row.symbol}, '
                       f'"Sector": {row.sector}, '
                       f'"Stock Price": {row.price}.\n')
    if len(answer) == 0:
        return "There aren't any companies that match the request."
    else:
        return answer


@cache(30)
def companies_by_sector(
    sector: str,
    db_connector: 'StorageProtocol'
        ) -> list[str]:
    """ Returns the list of companies that work in the chosen sector. """
    final_list: list[str] = []
    correct_sector_name = []
    data = db_connector.read_data()
    for row in data:
        if sector.lower() in row.sector.lower():
            final_list.append(row.name)
            if row.sector not in correct_sector_name:
                correct_sector_name.append(row.sector)
    if len(final_list) >= 1 and len(correct_sector_name) == 1:
        print(f'You chose sector {correct_sector_name}:')
        result = final_list
    else:
        result = companies_by_sector(input('Enter correct name of sector! '),
                                     db_connector)
    return result


def calc_average_price(db_connector: 'StorageProtocol') -> float:
    counter_of_companies: int = 0
    total_price: float = 0
    data = db_connector.read_data()
    for row in data:
        counter_of_companies += 1
        total_price += float(row.price)
    average_price = round((total_price / counter_of_companies), 2)
    return average_price


def top_ten_companies(db_connector: 'StorageProtocol') -> list:
    """ Returns the list of 10 most expensive companies."""
    final_list: list[tuple[str, float]] = []
    data = db_connector.read_data()
    for row in data:
        price_1 = float(row.price)
        name_1 = row.name
        tuple_price = (name_1, price_1)
        final_list.append(tuple_price)
        result_list = sorted(final_list, key=lambda price: price[1],
                             reverse=True)
    final_list = result_list[0:11]
    return final_list


def add_new_company(
        symbol: str,
        name: str,
        sector: str,
        price: str,
        db_connector: 'StorageProtocol'
        ) -> None:
    """Adds a new company into the end of the database."""
    new_company = [CompaniesDTO(
        symbol=symbol,
        name=name,
        sector=sector,
        price=price
        )]
    db_connector.write_to_database(new_company)


def update_company_name(
        company_symbol: str,
        company_name: str,
        db_connector: 'StorageProtocol'
        ) -> None:
    """Updates the company name with the passed symbol."""
    data = db_connector.read_data()
    new_data: DataTyping = []
    for row in data:
        if row.symbol == company_symbol.upper():
            row.name = company_name
        new_data.append(row)
    db_connector.write_to_database(new_data, mode='w')


def delete_company(
        symbol: str,
        db_connector: 'StorageProtocol'
        ) -> None:
    """ Deletes the company from the database."""
    data = db_connector.read_data()
    new_data: DataTyping = []
    for row in data:
        if row.symbol != symbol:
            new_data.append(row)
    db_connector.write_to_database(new_data, mode='w')


def truncate_all_data(db_connector: 'StorageProtocol') -> None:
    db_connector.write_to_database(data=[], mode='w')


def generate_new_data(num: str,
                      db_connector: 'StorageProtocol') -> None:
    """Populates database with random data."""
    new_data: DataTyping = []
    fake = Faker()
    sectors = DynamicProvider(
        provider_name="Sectors",
        elements=['Consumer Discretionary', 'Consumer Staples', 'Energy',
                  'Financials', 'Materials', 'Telecommunication Services',
                  'Real Estate', 'Industrials', 'Utilities', 'Health Care',
                  'Information Technology'],
    )
    fake.add_provider(sectors)
    for _ in range(int(num)):
        company_name = fake.unique.company()
        company_symbol = company_name[0]
        for _ in range(randrange(1, 5)):
            company_symbol += fake.random_uppercase_letter()
        company_sector = fake.Sectors()
        company_price = round(uniform(0, 1000), 2)
        row = CompaniesDTO(
            symbol=company_symbol,
            name=company_name,
            sector=company_sector,
            price=str(company_price),
        )
        new_data.append(row)
    db_connector.write_to_database(data=new_data, mode='w')
