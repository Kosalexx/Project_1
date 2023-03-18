from time import sleep
from business_logic import (find_by_name, find_by_symbol,
                            companies_by_sector, calc_average_price,
                            top_ten_companies, add_new_company,
                            update_company_name, delete_company,
                            truncate_all_data, generate_new_data)
from validators import (validate_user_choice, validate_symbol_name,
                        validate_company_name, validate_sector_name,
                        validate_company_price, symbol_name_in_data,
                        validate_number)
from errors import (IncorrectUserInputError, IncorrectSymbolError,
                    IncorrectNewCompanyNameError, IncorrectSectorNameError,
                    IncorrectCompanyPriceError, IncorrectGeneratedNumberError)
from providers import provide_db
from config import DB_FILE, DB_TYPE


start = ("Choose the action from menu:\n"
         "1 - Find info by name\n"
         "2 - Find info by symbol\n"
         "3 - Get all companies by sector\n"
         "4 - Calculate average price\n"
         "5 - Get top 10 companies\n"
         "6 - Add new company\n"
         "7 - Update company name\n"
         "8 - Delete company\n"
         "9 - Truncate all \n"
         "10 - Populate file with random data\n"
         "11 - Exit ")
current_db_connector = provide_db(DB_FILE, DB_TYPE)

while True:
    print(start)
    user_choice = input('Your choice: ')

    try:
        validate_user_choice(user_choice=user_choice)
    except IncorrectUserInputError as err:
        print(err)
        sleep(0.5)

    if user_choice == "1":
        company_name = input('Enter the name of company: ').lower()
        result = find_by_name(company_name, current_db_connector)
        print(result)
    elif user_choice == "2":
        company_symbol = input('Enter the Symbol of company: ')
        result = find_by_symbol(company_symbol, current_db_connector)
        print(result)
    elif user_choice == "3":
        sector_name = input('Enter name of sector: ')
        result = companies_by_sector(sector_name, current_db_connector)
        print(result)
    elif user_choice == "4":
        result = calc_average_price(current_db_connector)
        print(f'Average price: {result}')
    elif user_choice == "5":
        result = top_ten_companies(current_db_connector)
        print(result)
    elif user_choice == "6":
        company_symbol = input('Enter Symbol of the company to be added: ')
        try:
            validate_symbol_name(company_symbol)
        except IncorrectSymbolError as err:
            print(err)
            sleep(0.5)
            continue
        company_name = input('Enter Name of the company to be added: ')
        try:
            validate_company_name(company_name)
        except IncorrectNewCompanyNameError as err:
            print(err)
            sleep(0.5)
            continue
        sector_name = input('Enter name of the Sector: ')
        try:
            validate_sector_name(sector_name)
        except IncorrectSectorNameError as err:
            print(err)
            sleep(0.5)
            continue
        company_price = input('Enter Price of the company: ')
        try:
            validate_company_price(company_price)
        except IncorrectCompanyPriceError as err:
            print(err)
            sleep(0.5)
            continue
        add_new_company(company_symbol, company_name, sector_name,
                        company_price, current_db_connector)
        print(f'You added the {company_name} company to the list.')
    elif user_choice == "7":
        company_symbol = input('Enter the symbol of the company whose name '
                               'is to be changed: ').upper()
        try:
            symbol_name_in_data(symbol_name=company_symbol)
        except IncorrectSymbolError as err:
            print(err)
            sleep(0.5)
            continue
        company_name = input('Enter new name of the company: ')
        try:
            validate_company_name(company_name)
        except IncorrectNewCompanyNameError as err:
            print(err)
            sleep(0.5)
            continue
        update_company_name(company_symbol, company_name,
                            current_db_connector)
        print(f"New name of company with {company_symbol} Symbol:"
              f" {company_name}.")
    elif user_choice == "8":
        company_symbol = input('Enter the symbol of the company that will '
                               'be deleted: ')
        try:
            symbol_name_in_data(symbol_name=company_symbol)
        except IncorrectSymbolError as err:
            print(err)
            sleep(0.5)
            continue
        delete_company(company_symbol, current_db_connector)
    elif user_choice == "9":
        answer = input('Enter "YES" if you seriously want to delete all data.')
        if answer.upper() == 'YES':
            truncate_all_data(current_db_connector)
            print('Complete. All data has been deleted.')
        else:
            print('The data has NOT been deleted.')
        sleep(0.5)
        continue
    elif user_choice == "10":
        number = input('Enter the number of records to be generated.')
        try:
            validate_number(number)
        except IncorrectGeneratedNumberError as err:
            print(err)
            sleep(0.5)
            continue
        generate_new_data(number, current_db_connector)
    elif user_choice == "11":
        print('GOODBYE!')
        break
