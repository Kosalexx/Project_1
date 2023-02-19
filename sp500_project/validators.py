from errors import (IncorrectUserInputError, IncorrectSymbolError,
                    IncorrectNewCompanyNameError, IncorrectSectorNameError,
                    IncorrectCompanyPriceError, IncorrectGeneratedNumberError)
from business_logic import check_in_data


def validate_user_choice(user_choice):
    if not user_choice.isdigit():
        raise IncorrectUserInputError("Choice must be digit.")

    if user_choice not in [str(i) for i in range(1, 11)]:
        raise IncorrectUserInputError("Choice must be from 1 to 6.")


def symbol_name_in_data(symbol_name):
    if not check_in_data(symbol_name=symbol_name):
        raise IncorrectSymbolError("Symbol doesn't exist in the database.")


def validate_symbol_name(symbol_name):
    if not symbol_name.isalpha():
        raise IncorrectSymbolError("Symbol name must be letter.")
    if len(symbol_name) < 3 or len(symbol_name) > 6:
        raise IncorrectSymbolError("Symbol length must be from 3 to 6 "
                                   "letters.")
    if symbol_name != symbol_name.upper():
        raise IncorrectSymbolError("Symbol name must be capitalized.")
    if check_in_data(symbol_name=symbol_name):
        raise IncorrectSymbolError("Symbol already exist.")


def validate_company_name(company_name):
    if len(company_name) < 3 or len(company_name) > 50:
        raise IncorrectNewCompanyNameError("The length of company name must "
                                           "be from 3 to 50 letters.")
    if check_in_data(company_name=company_name):
        raise IncorrectNewCompanyNameError("This company already exist.")


def validate_sector_name(sector_name):
    if not check_in_data(sector=sector_name):
        raise IncorrectSectorNameError("Sector doesn't exist in the database")


def validate_company_price(company_price):
    if not company_price.replace(".", "", 1).isdigit():
        raise IncorrectCompanyPriceError("Price must be floated number.")
    if float(company_price) < 0 or float(company_price) > 1000:
        raise IncorrectCompanyPriceError("Price must be from 0 to 1000.")


def validate_number(number):
    if not number.isdigit():
        raise IncorrectGeneratedNumberError("Number must be an integer.")
    elif int(number) < 1 or int(number) > 1000:
        raise IncorrectGeneratedNumberError("Number nust be from 1 to 1000.")
