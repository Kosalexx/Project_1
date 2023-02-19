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


@cache_deco
def find_by_symbol(symbol: str) -> list:
    """ Finds a company by symbol in the database. """

    final_list = []

    with open("sp500.csv", encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=',')
        for row in file_reader:
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


@cache_deco
def companies_by_sector(sector: str) -> list:
    """ Returns the list of companies that work in the chosen sector. """

    final_list = []
    correct_sector_name = []

    with open("sp500.csv", encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=',')
        for row in file_reader:
            if sector.lower() in row.get('Sector').lower():
                final_list.append(row.get('Name'))
                if row.get('Sector') not in correct_sector_name:
                    correct_sector_name.append(row.get('Sector'))

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
            total_price += float(row.get('Price'))
    average_price = round((total_price / counter_of_companies), 2)
    return average_price


@cache_deco
def top_ten_companies() -> list:
    """ Returns the list of 10 most expensive companies."""
    final_list = []

    with open("sp500.csv", encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=',')
        for row in file_reader:
            price_1 = float(row.get('Price'))
            name_1 = row.get('Name')
            tuple_price = (name_1, price_1)
            final_list.append(tuple_price)
        result_list = sorted(final_list, key=lambda price: price[1],
                             reverse=True)

    return result_list[0:11]


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


start = ("Choose the action from menu:\n"
         "1 - Find info by name\n"
         "2 - Find info by symbol\n"
         "3 - Get all companies by sector\n"
         "4 - Calculate average price\n"
         "5 - Get top 10 companies\n"
         "6 - Exit ")

flag = True
while flag:
    print(start)
    choice = input('Your choice: ')
    if choice == "1":
        company_name = input('Enter the name of company: ').lower()
        result = find_by_name(company_name)
        print(result)
        flag = maybe_stop()
    elif choice == "2":
        company_symbol = input('Enter the Symbol of company: ')
        result = find_by_symbol(company_symbol)
        print(result)
        flag = maybe_stop()
    elif choice == "3":
        sector_name = input('Enter name of sector: ')
        result = companies_by_sector(sector_name)
        print(result)
        flag = maybe_stop()
    elif choice == "4":
        result = calc_average_price()
        print(f'Average price: {result}')
        flag = maybe_stop()
    elif choice == "5":
        result = top_ten_companies()
        print(result)
        flag = maybe_stop()
    elif choice == "6":
        print('GOODBYE!')
        flag = False
    else:
        continue
