""" A program with a console interface, with which the user could view stock
quotes of companies from the s p500 rating: search company in the database,
display the rating, get the average cost of quotations.
"""

import csv
from cache_decorator import cache_deco


@cache_deco
def find_by_name(name: str) -> list:
    """ Finds a company by name in the database. """

    answer = []

    with open("sp500.csv", encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=',')

        for row in file_reader:
            final_dict = {}
            if name in row['Name'].lower() or row['Name'].lower() in name:
                final_dict['Name'] = row['Name']
                final_dict['Symbol'] = row['Symbol']
                final_dict['Sector'] = row['Sector']
                final_dict['Stock price'] = float(row['Price'])
                answer.append(final_dict)
    if len(answer) == 0:
        return "There aren't any companies that match the request."
    else:
        return answer


@cache_deco
def find_by_symbol(symbol: str) -> list:
    """ Finds a company by symbol in the database. """

    final_list = []

    with open("sp500.csv", encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=',')
        for row in file_reader:
            final_dict = {}
            if symbol.upper() in row['Symbol'] or row['Symbol'] in  \
                    symbol.upper():
                final_dict['Name'] = row['Name']
                final_dict['Symbol'] = row['Symbol']
                final_dict['Sector'] = row['Sector']
                final_dict['Stock price'] = float(row['Price'])
                final_list.append(final_dict)

    if len(final_list) == 0:
        return "There aren't any companies that match the request."
    else:
        return final_list


@cache_deco
def companies_by_sector(sector: str) -> list:
    """ Returns the list of companies that work in the chosen sector. """

    final_list = []
    correct_sector_name = []

    with open("sp500.csv", encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=',')
        for row in file_reader:
            if row['Sector'].lower() in sector.lower() or \
                    sector.lower() in row['Sector'].lower():
                final_list.append(row['Name'])
                if row['Sector'] not in correct_sector_name:
                    correct_sector_name.append(row['Sector'])

    if len(final_list) >= 1 and len(correct_sector_name) == 1:
        print(f'You chose sector {correct_sector_name}:')
        return final_list
    else:
        companies_by_sector(input('Enter correct name of sector! '))


@cache_deco
def calc_average_price() -> float:
    counter_of_companies = 0
    total_price = 0
    with open("sp500.csv", encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=',')
        for row in file_reader:
            counter_of_companies += 1
            total_price += float(row['Price'])
    average_price = round((total_price / counter_of_companies), 2)
    return average_price


@cache_deco
def top_ten_companies() -> list:
    """ Returns the list of 10 most expensive companies."""
    final_list = []

    with open("sp500.csv", encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=',')
        for row in file_reader:
            price_1 = float(row['Price'])
            name_1 = row['Name']
            tuple_price = (name_1, price_1)
            if len(final_list) == 0:
                final_list.append(tuple_price)
            else:
                for ind in range(len(final_list)):
                    if final_list[ind][1] <= price_1 and tuple_price not in \
                            final_list:
                        final_list.insert(ind, tuple_price)
            if len(final_list) > 10:
                final_list.pop()

    return final_list


def maybe_stop() -> bool:
    """ Checks to continue or end the execution of the program. """
    global flag
    print('Want to get some more information? ("Y" = yes, "N" = no)')
    ans = input('Your choice: ')
    if ans.lower() == 'y':
        flag = True
    elif ans.lower() == 'n':
        print('GOODBYE!')
        flag = False
    else:
        print('Enter "Y" or "N": ')
        maybe_stop()
    return flag


start = """Choose the action from menu:
1 - Find info by name
2 - Find info by symbol
3 - Get all companies by sector
4 - Calculate average price
5 - Get top 10 companies
6 - Exit """

flag = True
while flag:
    print(start)
    choice = int(input('Your choice: '))
    if choice == 1:
        company_name = input('Enter the name of company: ').lower()
        result = find_by_name(company_name)
        print(result)
        flag = maybe_stop()
    elif choice == 2:
        company_symbol = input('Enter the Symbol of company: ')
        result = find_by_symbol(company_symbol)
        print(result)
        flag = maybe_stop()
    elif choice == 3:
        sector_name = input('Enter name of sector: ')
        result = companies_by_sector(sector_name)
        print(result)
        flag = maybe_stop()
    elif choice == 4:
        result = calc_average_price()
        print(f'Average price: {result}')
        flag = maybe_stop()
    elif choice == 5:
        result = top_ten_companies()
        print(result)
        flag = maybe_stop()
    elif choice == 6:
        print('GOODBYE!')
        flag = False
    else:
        continue
