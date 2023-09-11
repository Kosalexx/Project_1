from errors import (IncorrectUserInputError,
                    IncorrectIdError,
                    IncorrectUserEmailError,
                    IncorrectPhoneError)
from config import AVAILABLE_EMAIL_SERVICES


def validate_user_choice(user_choice: str) -> None:
    if not user_choice.isdigit():
        raise IncorrectUserInputError("Choice must be digit.")


def validate_id(user_id: str) -> None:
    if not user_id.isdigit():
        raise IncorrectIdError("Entered ID must be digit.")


def validate_new_email(email: str) -> None:
    email_parts = email.split('@')
    if len(email_parts) != 2:
        raise IncorrectUserEmailError("Incorrect email. Email must contains "
                                      "one '@' symbol.")
    if email_parts[1] not in AVAILABLE_EMAIL_SERVICES:
        raise IncorrectUserEmailError("Incorrect email service. Try "
                                      "'gmail.com' or 'mail.ru'.")


def validate_phone(phone: str) -> None:
    if phone[0] != '+':
        raise IncorrectPhoneError("Phone must starts from '+'.")
    if not phone[1:].isdigit():
        raise IncorrectPhoneError('All phone symbols (except the first)'
                                  ' must be digits.')
