from errors import IncorrectUserInputError


def validate_user_choice(user_choice: str) -> None:
    """Validates user choice.

    :param user_choice: first input from user in main menu
    :type user_choice: srt

    :raises IncorrectUserInputError: if user choice is not digit or
    not in range from 1 to 6.

    """
    if not user_choice.isdigit():
        raise IncorrectUserInputError("Choice must be digit.")
    if user_choice not in [str(i) for i in range(1, 7)]:
        raise IncorrectUserInputError("Choice must be from 1 to 6.")


def validate_user_key(user_key: str, exist_master_key: str) -> None:
    """Validates user key.

    :param user_key: user-entered master key
    :type user_key: str
    :param exist_master_key: existing in the database master key
    :type exist_master_key: str

    :raises ValueError: if user enter wrong master key.
    """
    if user_key != exist_master_key:
        raise ValueError("You entered the wrong master password!")


def validate_identifier(value: str) -> None:
    """Validates identifier.

    :param value: value of entered identifier
    :type value: str

    :raises ValueError: if identifier value is empty.
    """
    if len(value) == 0:
        raise ValueError('The identifier cannot be an empty string.')


def validate_password(value: str) -> None:
    """Validates entered user password.

    :param value: value of entered password
    :type value: str

    :raises ValueError: if the password is shorter than 6 characters
    and does not contain at least one lowercase and one uppercase letter.
    """
    if len(value) < 6:
        raise ValueError('The password must be at least 6 characters long.')
    upper_counter: int = 0
    lower_counter: int = 0
    for sym in value:
        if sym.islower():
            lower_counter += 1
        if sym.isupper():
            upper_counter += 1
    if upper_counter < 1:
        raise ValueError('The password must contain at least '
                         'one capital letter')
    if lower_counter < 1:
        raise ValueError('The password must contain at '
                         'least one lowercase letter')
