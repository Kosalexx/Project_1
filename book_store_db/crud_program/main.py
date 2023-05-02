from __future__ import annotations
from ui_layer import (
    users_ui_menu,
    book_ui_menu,
    authors_ui_menu,
    transactions_ui_menu)
from validators import (
    validate_user_choice)
from errors import (
    IncorrectUserInputError)
from data_access import SqliteGateway
from config import DB_FILE
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from data_access.interfaces import DBGatewayProtocol


db_gateway: DBGatewayProtocol = SqliteGateway(DB_FILE)
main_menu = (
    '\n======================= MAIN MENU ============================\n'
    'Chose your action from main menu:\n'
    '1 - Users\n'
    '2 - Books\n'
    '3 - Authors\n'
    '4 - Transactions\n'
    '5 - Exit\n'
    '==============================================================\n'
    )


def main() -> None:
    while True:
        print(main_menu)
        user_choice = input('Your choice: ')
        try:
            validate_user_choice(user_choice=user_choice)
        except IncorrectUserInputError as err:
            print(err)

        if user_choice == '1':
            users_ui_menu(db_connector=db_gateway)
            continue
        if user_choice == '2':
            book_ui_menu(db_connector=db_gateway)
            continue
        if user_choice == '3':
            authors_ui_menu(db_connector=db_gateway)
            continue
        if user_choice == '4':
            transactions_ui_menu(db_connector=db_gateway)
            continue
        if user_choice == '5':
            print('Good Bye!')
            break
        else:
            print('Choice must be from 1 to 5!')
            continue


if __name__ == '__main__':
    main()
