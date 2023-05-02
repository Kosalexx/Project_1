from __future__ import annotations
from validators import (validate_user_choice, validate_id)
from errors import (IncorrectUserInputError, IncorrectIdError)
from typing import TYPE_CHECKING
from business_logic import AuthorsLogic
if TYPE_CHECKING:
    from data_access.interfaces import DBGatewayProtocol
    from business_logic import BusinessLogicProtocol

authors_menu = (
    '\n====================== AUTHORS MENU ==========================\n'
    'Chose your action from users menu:\n'
    '1 - List of all authors\n'
    '2 - Get author info\n'
    '3 - Delete author\n'
    '4 - Update author info\n'
    '5 - Exit to main menu\n'
    '==============================================================\n'
    )


def authors_ui_menu(db_connector: DBGatewayProtocol) -> None:
    while True:
        print(authors_menu)
        user_choice = input('Your choice: ')
        try:
            validate_user_choice(user_choice=user_choice)
        except IncorrectUserInputError as err:
            print(err)
        logic: BusinessLogicProtocol = AuthorsLogic(db_gateway=db_connector)
        if user_choice == '1':
            print('__________ List of all authors. __________')
            all_data = logic.list_of_all_data()
            for row in all_data:
                print(row)
            continue
        if user_choice == '2':
            print('____________ Get Author info. ____________')
            entered_id = input('Enter book_id: ')
            try:
                validate_id(entered_id)
            except IncorrectIdError as err:
                print(err)
                continue

            result = logic.get_concrete_info(value=entered_id)
            res_dict = result[0]
            if res_dict.get('Result') is None:
                for key, value in res_dict.items():
                    print(f'{key}: {value}')
            else:
                print(result[0].get('Result'))
            continue
        if user_choice == '3':
            print('____________ Delete author. ____________')
            entered_id = input('Enter author_id: ')
            try:
                validate_id(entered_id)
            except IncorrectIdError as err:
                print(err)
                continue
            check_id = logic.check_in_data(value=entered_id)
            if check_id:
                logic.delete_value(entered_id)
                print(f'Information about author with ID {entered_id} was '
                      f'deleted from the database.')
            else:
                print('There is no author with the specified ID in the '
                      'database')
            continue
        if user_choice == '4':
            print('____________ Update author info. ____________')
            entered_id = input('Enter author: ')
            try:
                validate_id(entered_id)
            except IncorrectIdError as err:
                print(err)
                continue
            check_id = logic.check_in_data(value=entered_id)
            if check_id:
                new_name = input('Enter new author info: ')
                logic.update_value(entered_id, new_name.capitalize())
                print(f'Info about author with ID {entered_id} was updated.')
            else:
                print('There is no authors with the specified ID in the '
                      'database')
            continue
        if user_choice == '5':
            break
        else:
            print('Choice must be from 1 to 6!')
            continue
