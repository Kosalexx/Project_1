from art import text2art  # type: ignore
from time import sleep
from business_logic import MasterKey, PasswordManager
from validations import (validate_user_choice,
                         validate_user_key,
                         validate_identifier,
                         validate_password)
from errors import IncorrectUserInputError


logo = text2art('Password_manager')
main_menu: str = ('1. Add new password.\n'
                  '2. Get list of the passwords.\n'
                  '3. Get a password.\n'
                  '4. Delete password.\n'
                  '5. Export passwords to file.\n'
                  '6. Exit.')


def main() -> None:
    """Main cycle of program."""

    print(logo)
    print('Welcome to the password manager!')
    master_key = MasterKey()
    key = master_key.key
    storage = PasswordManager(key)
    while True:
        print('Chose action from main menu: ')
        print(main_menu)
        choice = input('Your choice: ')
        try:
            validate_user_choice(choice)
        except IncorrectUserInputError as err:
            print(err)
            sleep(0.5)
            continue
        if choice == '1':
            print('   _____ Add new password _____   ')
            identifier = input('Enter your password identifier (any string, '
                               'for example: Instagram): ')
            sleep(0.5)
            print(f'Enter the password for "{identifier}". \nPassword must be'
                  ' at least 6 characters long and contain at least 1 '
                  'lowercase, 1 capital letter.')
            password = input('Password:')
            sleep(0.5)
            user_key = input('Enter master-key: ')
            try:
                validate_user_key(user_key=user_key, exist_master_key=key)
                validate_identifier(identifier)
                validate_password(password)
            except ValueError as err:
                print(err)
                sleep(0.5)
                continue
            storage.add_new_password(identifier, password)
            print(f'New password for "{identifier}" has been added.')
            print('-------------------------------------------------------')
            sleep(1)
            continue
        if choice == '3':
            print('    _____ Get a password _____     ')
            identifier = input('Enter identifier for searched password: ')
            user_key = input('Enter master-key: ')
            try:
                validate_user_key(user_key=user_key, exist_master_key=key)
                validate_identifier(identifier)
            except ValueError as err:
                print(err)
                sleep(0.5)
                continue
            result = storage.get_password(identifier)
            print(f'Password for {identifier}: "{result}"')
            print('-------------------------------------------------------')
            sleep(1)
            continue
        if choice == '2':
            print('     _____ Get passwords list _____')
            sleep(0.5)
            user_key = input('Enter master-key: ')
            try:
                validate_user_key(user_key=user_key, exist_master_key=key)
            except ValueError as err:
                print(err)
                sleep(0.5)
                continue
            print('The passwords for the following identifiers are'
                  'stored in the database: ')
            id_list = storage.get_id_list()
            print(id_list)
            print('-------------------------------------------------------')
            sleep(1)
            continue
        if choice == '4':
            print('    _____ Delete password _____     ')
            identifier = input('Enter the identifier of the password'
                               ' you want to delete: ')
            user_key = input('Enter master-key: ')
            try:
                validate_user_key(user_key=user_key, exist_master_key=key)
                validate_identifier(identifier)
            except ValueError as err:
                print(err)
                sleep(0.5)
                continue
            result = storage.delete_password(identifier)
            print(result)
            print('-------------------------------------------------------')
            sleep(1)
        if choice == '5':
            print('    _____  Export passwords to file _____     ')
            print('Available export formats: excel, csv, txt, xml.')
            file_format = input('Enter the file format: ')
            user_key = input('Enter master-key: ')
            try:
                validate_user_key(user_key=user_key, exist_master_key=key)
            except ValueError as err:
                print(err)
                sleep(0.5)
                continue
            try:
                storage.export_passwords_to_file(file_format)
            except ValueError as err:
                print(err)
                sleep(0.5)
                continue
            print(f'All your passwords have been exported. '
                  f'Check the file "my_passwords.{file_format}" '
                  f'in the date_access folder.')
            print('-------------------------------------------------------')
            sleep(1)
        if choice == '6':
            sleep(1)
            print("Goodbye.")
            break
