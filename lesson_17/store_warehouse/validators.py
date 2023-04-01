from re import fullmatch
from datetime import datetime


from exceptions import (IncorrectUserInputError,
                        IncorrectCategoryNameError,
                        IncorrectParametersInputError,
                        IncorrectParametersValueError,
                        IncorrectDateInputError)


def validate_user_choice(user_choice: str) -> None:
    """Validates user choice.

    :param user_choice: first input from user in main menu
    :type user_choice: srt

    :raises IncorrectUserInputError: if user choice is not digit or
    not in range from 1 to 7.
    """
    if not user_choice.isdigit():
        raise IncorrectUserInputError("Choice must be digit.")
    if user_choice not in [str(i) for i in range(1, 8)]:
        raise IncorrectUserInputError("Choice must be from 1 to 7.")


def validate_category_name(category_name: str) -> None:
    """ Validates name of category

    :param category_name: name of created category
    :type category_name: str

    :raises IncorrectCategoryNameError: if category name does not consist of
    letters, numbers or the "_" symbol; and if category name  begins not
    with a letter.
    """
    if not fullmatch(r'[a-zA-Z0-9_]+', category_name):
        raise IncorrectCategoryNameError("Category name can consist of letters"
                                         ", numbers and _ symbol. ")
    if not category_name[0].isalpha():
        raise IncorrectCategoryNameError("Category name must begin from a "
                                         "letter.")


def validate_parameter_name(parameter: str) -> None:
    """ Validates name of parameter

    :param parameter: name of parameter
    :type parameter: str

    :raises IncorrectCategoryNameError: if parameter name does not consist of
    letters, numbers or the "_" symbol; and if parameter name  begins not
    with a letter.
    """
    new_par: str = parameter.strip().lower()
    if not fullmatch(r'[a-zA-Z0-9_]+', new_par):
        raise IncorrectParametersInputError(
            "Name of parameter can consist of "
            "letters, numbers and _ symbol."
            )
    if not new_par[0].isalpha():
        raise IncorrectParametersInputError(
            "Name of parameter must begin from a letter."
            )


def validate_parameters_value(value: str) -> None:
    """ Validates value of parameter

    :param value: value of parameter
    :type value: str

    :raises IncorrectParametersValueError: if value of parameter is empty."""
    if value.replace(' ', '') == '':
        raise IncorrectParametersValueError(
            "The Value of parameter cannot be empty."
            )


def validate_quantity(value: str) -> None:
    """Validates quantity of new product.

    :param value: quantity of product
    :type value: str

    :raises ValueError: if quantity is not integer or less than zero.
    """
    if not value.isalnum():
        raise ValueError("Quantity must be integer.")
    if value == '0':
        raise ValueError("Entered quantity must be greater than zero.")


def validate_date(date: str) -> float:
    """Validates entered date.

    :param date: date in format YYYY-MM-DD (YYYY - Year (from 1970 to current),
                                            MM - Month (01-12),
                                            DD - Day (1-31),
                                            separator = '-').
    :type date: str

    :raises IncorrectDateInputError: if date entered in wrong format or date
    is incorrect.

    :rtype: float
    :return: time in UNIX format equals 00:00:00 of the entered date.
    """
    new_date = date.split('-')
    if len(new_date) != 3:
        raise IncorrectDateInputError("Date must be in format YYYY-MM-DD "
                                      "(YYYY - Year (from 1970 to current), "
                                      " MM - Month (01-12), DD - Day (1-31), "
                                      "separator = '-').")
    for val in new_date:
        if not val.isalnum():
            raise IncorrectDateInputError(
                "Date must be in format YYYY-MM-DD "
                "(YYYY - Year (from 1970 to current), "
                " MM - Month (1-12), DD - Day (1-31), "
                "separator = '-').")
    if int(new_date[0]) not in range(1970, datetime.now().year+1):
        raise IncorrectDateInputError("Year must be between 1970 and current.")
    if len(new_date[1]) != 2:
        raise IncorrectDateInputError("Month must be in the two-digit range "
                                      "from 01 to 12.")
    if int(new_date[1]) not in range(1, 12):
        raise IncorrectDateInputError("Month must be in the two-digit range "
                                      "from 01 to 12.")
    if len(new_date[2]) != 2:
        raise IncorrectDateInputError("Day must be in the two-digit range "
                                      "from 01 to 31.")
    if int(new_date[2]) not in range(1, 31):
        raise IncorrectDateInputError("Day must be in the two-digit range "
                                      "from 01 to 31.")
    if int(new_date[2]) > 28 and new_date[1] == '02':
        raise IncorrectDateInputError("February usually has 28 days.")
    if new_date[2] == '31' and new_date[1] in ['04', '06', '09', '11']:
        raise IncorrectDateInputError('This month has 30 days.')
    res = datetime.fromisoformat(f'{date} 00:00:00')
    result = float(res.timestamp())
    return result


def validate_id(value: str) -> None:
    """Validates id of product.

    :param value: id of product in database
    :type value: str

    :raises ValueError: if value of id is not integer
    """
    if not value.isalnum():
        raise ValueError('Value of id must be integer.')


def validate_price(value: str) -> None:
    """Validates price of product.

    :param value: product price
    :type value: str

    :raise ValueError: if value of price is not integer or float.
    """
    new_val = value.replace('.', '', 1)
    if not new_val.isalnum():
        raise ValueError('Price must be integer or float.')
