from __future__ import annotations
from validators import (validate_user_choice, validate_id,
                        validate_new_email, validate_phone)
from errors import (IncorrectUserInputError, IncorrectIdError,
                    IncorrectUserEmailError)
from typing import TYPE_CHECKING
from business_logic import UsersLogic
if TYPE_CHECKING:
    from data_access.interfaces import DBGatewayProtocol
    from business_logic import BusinessLogicProtocol


users_menu = (
    '======================= USERS MENU ===========================\n'
    'Chose your action from users menu:\n'
    '1 - List of all users\n'
    '2 - Get user info\n'
    '3 - Delete user\n'
    '4 - Update user email\n'
    '5 - Update user phone\n'
    '6 - Exit to main menu\n'
    '==============================================================\n'
    )


def users_ui_menu(db_connector: DBGatewayProtocol) -> None:
    while True:
        print(users_menu)
        user_choice = input('Your choice: ')
        try:
            validate_user_choice(user_choice=user_choice)
        except IncorrectUserInputError as err:
            print(err)

        logic: BusinessLogicProtocol = UsersLogic(db_gateway=db_connector)

        if user_choice == '1':
            print('__________ List of all users. __________')
            all_users = logic.list_of_all_data()
            for row in all_users:
                print(row)
            continue

        if user_choice == '2':
            print('____________ Get user info. ____________')
            entered_id = input('Enter user_id: ')
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
            print('____________ Delete user. ____________')
            entered_id = input('Enter user_id: ')
            try:
                validate_id(entered_id)
            except IncorrectIdError as err:
                print(err)
                continue
            check_user_id = logic.check_in_data(value=entered_id)
            if check_user_id:
                logic.delete_value(entered_id)
                print(f'Information about user with ID {entered_id} was '
                      f'deleted from the database.')
            else:
                print('There is no user with the specified ID in the database')
            continue
        if user_choice == '4':
            print('____________ Update user email. ____________')
            entered_id = input('Enter user_id: ')
            try:
                validate_id(entered_id)
            except IncorrectIdError as err:
                print(err)
                continue
            check_user_id = logic.check_in_data(value=entered_id)
            if check_user_id:
                new_email = input('Enter new email: ')
                try:
                    validate_new_email(email=new_email)
                except IncorrectUserEmailError as err:
                    print(err)
                    continue
                logic.update_value(entered_id, new_email)
                print(f'Email of user with ID {entered_id} was updated.')
            else:
                print('There is no user with the specified ID in the database')
            continue
        if user_choice == '5':
            print('____________ Update user phone. ____________')
            entered_id = input('Enter user_id: ')
            try:
                validate_id(entered_id)
            except IncorrectIdError as err:
                print(err)
                continue
            check_user_id = logic.check_in_data(value=entered_id)
            if check_user_id:
                new_phone = input('Enter new phone: ')
                try:
                    validate_phone(phone=new_phone)
                except IncorrectUserEmailError as err:
                    print(err)
                    continue
                logic.update_value(entered_id, new_phone)
                print(f'Phone of user with ID {entered_id} was updated.')
            else:
                print('There is no user with the specified ID in the database')
            continue
        if user_choice == '6':
            print('Good Bye!')
            break
        else:
            print('Choice must be from 1 to 6!')
            continue
