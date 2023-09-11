from art import text2art  # type: ignore
from time import sleep
from exceptions import IncorrectUserInputError

from validators import validate_user_choice

from ui_layer import (create_new_category,
                      add_new_product,
                      list_of_all_products,
                      info_about_product,
                      product_order,
                      create_statistic)


logo: str = text2art('Warehouse')
start: str = ("Choose the action from menu:\n"
              "1 - Create a product category\n"
              "2 - Add a new product\n"
              "3 - Get a list of ALL products in the warehouse\n"
              "4 - Get info about CONCRETE product\n"
              "5 - New order\n"
              "6 - Get statistics\n"
              "7 - Exit\n")


def my_warehouse() -> None:
    print(logo)
    while True:
        print(start)
        user_choice = input('Your choice: ')

        try:
            validate_user_choice(user_choice=user_choice)
        except IncorrectUserInputError as err:
            print(err)
            sleep(0.5)

        if user_choice == '1':
            create_new_category()
        if user_choice == '2':
            add_new_product()
            continue
        if user_choice == '3':
            list_of_all_products()
            continue
        if user_choice == '4':
            info_about_product()
            continue
        if user_choice == '5':
            product_order()
            continue
        if user_choice == '6':
            create_statistic()
            continue
        if user_choice == '7':
            print('Goodbye!')
            sleep(0.5)
            break


if __name__ == "__main__":
    my_warehouse()
