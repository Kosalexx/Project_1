from data_access import read_csv_data, write_to_csv_database
from cache import cache
from faker import Faker
from faker.providers import DynamicProvider
from random import uniform, randrange


@cache(30)
def find_by_name(name: str) -> list:
    """ Finds a company by name in the database. """
    answer = []
    data = read_csv_data()
    for row in data:
        if name in row.get('Name').lower():
            answer.append({
                "Name": row.get("Name"),
                "Symbol": row.get("Symbol"),
                "Sector": row.get("Sector"),
                "Stock Price": row.get("Price")
            }
            )
    if len(answer) == 0:
        return "There aren't any companies that match the request."
    else:
        return answer


@cache(30)
def find_by_symbol(symbol: str) -> list:
    """ Finds a company by symbol in the database. """
    final_list = []
    data = read_csv_data()
    for row in data:
        if symbol.upper() in row['Symbol']:
            final_list.append({
                "Name": row.get("Name"),
                "Symbol": row.get("Symbol"),
                "Sector": row.get("Sector"),
                "Stock Price": row.get("Price")
            }
            )
    if len(final_list) == 0:
        return "There aren't any companies that match the request."
    else:
        return final_list


@cache(30)
def companies_by_sector(sector: str) -> list:
    """ Returns the list of companies that work in the chosen sector. """
    final_list = []
    correct_sector_name = []
    data = read_csv_data()
    for row in data:
        if sector.lower() in row.get('Sector').lower():
            final_list.append(row.get('Name'))
            if row.get('Sector') not in correct_sector_name:
                correct_sector_name.append(row.get('Sector'))

    if len(final_list) >= 1 and len(correct_sector_name) == 1:
        print(f'You chose sector {correct_sector_name}:')
        return final_list
    else:
        companies_by_sector(input('Enter correct name of sector! '))


def calc_average_price() -> float:
    counter_of_companies = 0
    total_price = 0
    data = read_csv_data()
    for row in data:
        counter_of_companies += 1
        total_price += float(row.get('Price'))
    average_price = round((total_price / counter_of_companies), 2)
    return average_price


def top_ten_companies() -> list:
    """ Returns the list of 10 most expensive companies."""
    final_list = []
    data = read_csv_data()
    for row in data:
        price_1 = float(row.get('Price'))
        name_1 = row.get('Name')
        tuple_price = (name_1, price_1)
        final_list.append(tuple_price)
        result_list = sorted(final_list, key=lambda price: price[1],
                             reverse=True)

    return result_list[0:11]


def check_in_data(symbol_name='', company_name='', sector='') -> bool:
    """Checks if the company symbol, name, or sector exists in the database."""
    data = read_csv_data()
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


def add_new_company(symbol: str, name: str, sector: str, price: str) -> None:
    """Adds a new company into the end of the database."""
    fieldnames = ["Symbol", "Name", "Sector", "Price"]
    values = [symbol, name, sector, price]
    new_company = [{fieldnames[i]: values[i] for i in range(len(fieldnames))}]
    write_to_csv_database(fieldnames, new_company)


def update_company_name(company_symbol, company_name):
    """Update the company name with the passed symbol."""
    data = read_csv_data()
    new_data = []
    fields = []
    for row in data:
        if row.get("Symbol") == company_symbol.upper():
            row["Name"] = company_name
        new_data.append(row)

    for keys in new_data[0].keys():
        fields.append(keys)

    write_to_csv_database(fields, new_data, mode='w')


def delete_company(symbol: str) -> None:
    """ Delete the company from the database."""
    data = read_csv_data()
    new_data = []
    fields = []
    for row in data:
        if row.get("Symbol") != symbol:
            new_data.append(row)

    for keys in new_data[0].keys():
        fields.append(keys)
    print(fields)
    write_to_csv_database(fields, new_data, mode='w')


def truncate_all_data() -> None:
    write_to_csv_database(fields=[], data=[], mode='w')


def generate_new_data(num: str) -> None:
    """Populates database with random data."""
    fields = ["Symbol", "Name", "Sector", "Price"]
    new_data = []
    fake = Faker()
    sectors = DynamicProvider(
        provider_name="Sectors",
        elements=['Consumer Discretionary', 'Consumer Staples', 'Energy',
                  'Financials', 'Materials', 'Telecommunication Services',
                  'Real Estate', 'Industrials', 'Utilities', 'Health Care',
                  'Information Technology'],
    )
    fake.add_provider(sectors)
    for ind in range(int(num)):
        company_name = fake.unique.company()
        company_symbol = company_name[0]
        for _ in range(randrange(1, 5)):
            company_symbol += fake.random_uppercase_letter()
        company_sector = fake.Sectors()
        company_price = round(uniform(0, 1000), 2)
        row = {
            fields[0]: company_symbol,
            fields[1]: company_name,
            fields[2]: company_sector,
            fields[3]: company_price,
        }
        new_data.append(row)
    write_to_csv_database(fields=fields, data=new_data, mode='w')
