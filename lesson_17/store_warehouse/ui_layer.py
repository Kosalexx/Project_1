from time import sleep, time
from typing import Optional

from exceptions import (IncorrectCategoryNameError,
                        IncorrectParametersInputError,
                        IncorrectParametersValueError,
                        IncorrectDateInputError)

from validators import (validate_category_name,
                        validate_parameter_name,
                        validate_parameters_value,
                        validate_quantity,
                        validate_date,
                        validate_id,
                        validate_price)

from business_logic import (Category,
                            Product,
                            Order,
                            Statistic)


def create_new_category(category_name: Optional[str] = None) -> None:
    while True:
        if category_name is None:
            print('----- Create a new category of product -----')
            name: str = input('Enter name of created category: ')
        else:
            name = category_name
        try:
            validate_category_name(name)
        except IncorrectCategoryNameError as err:
            print(err)
            sleep(1.0)
            break
        new_category = Category(name)
        parameters = new_category.get_parameters()
        update_flag = False
        if parameters != []:
            exist_record = parameters[0]
            name_exist_category = exist_record.get('category')
            parameters_exist_category = exist_record.get('parameters')
            print(f'There is a category with the name '
                  f'"{name_exist_category}" in the database.')
            print(f'Parameters of existing "{name_exist_category}" category: '
                  f'{parameters_exist_category}.')
            print(f"Choose the action from category creation menu:\n"
                  f"1 - Upgrade existing category '{name_exist_category}';\n"
                  f"2(or Any another button) - Exit to main menu.\n")
            choice = input('Your choice: ')
            if choice == '1':
                update_flag = True
                new_name = name_exist_category
                new_category.cat_name = str(new_name)
            else:
                break
        else:
            update_flag = False
            new_category.cat_name = name.lower()
        print(f'Enter the parameters of the "{name}" category. '
              f'Each parameter is entered on a new line. '
              f'A category can have a maximum of 15 parameters.\n'
              f'The "name" and "price" parameters will be added '
              f'automatically. Only unique parameters will be added.'
              f'When you have finished entering the parameters, enter '
              f'the word "Stop".')
        param_list = ['name', 'price']
        for ind in range(1, 16):
            par = input(f'Parameter №{ind}: ')
            if par.lower() == 'stop':
                break
            try:
                validate_parameter_name(par)
                if par.lower() not in param_list:
                    param_list.append(par.lower())
            except IncorrectParametersInputError as err:
                print(err)
                sleep(1)
                break
        if param_list == []:
            print('At least 1 parameter must be passed!')
            break
        if update_flag:
            new_category.update_category(param_list)
            sleep(0.5)
            print(f'Parameters of the "{category_name}" category '
                  f'have been updated.')
            print('-----------------------------------------------------'
                  '----')
            sleep(1)
            break
        else:
            new_category.parameters = param_list
            new_category()
            print(f'Category "{name}" was created with the '
                  f'parameters: {param_list}.', end='\n\n')
            print('-----------------------------------------------------'
                  '----')
            sleep(1)
            break


def add_new_product() -> None:
    while True:
        print("----- Add a new product -----")
        category_name = input('Enter the category name of the product '
                              'you want to add: ')
        category = Category(name=category_name.lower())
        existing_category = category.get_parameters()
        if existing_category == []:
            print(f'There is no category named "{category_name}" '
                  f'in the database.')
            print(f'Do you want to create new category'
                  f' named "{category_name}"?')
            print(f'Chose from menu: \n'
                  f'1 - Create new category "{category_name}";\n'
                  f'2(or Any another button) - Exit to main menu.\n')
            answer = input('Your choice: ')
            if answer == '1':
                create_new_category(category_name=category_name)
            else:
                break
        sleep(0.5)
        new_product = Product(category_name=category_name.lower())
        parameters = new_product.get_parameters()
        if parameters != []:
            prod_param: dict[str, str | list[str]] = parameters[0]
            new_param = list(prod_param.get('parameters', []))
        print(f'The product category "{category_name}" is characterized '
              f'by parameters: {new_param}.')
        param_values = {}
        for param in new_param:
            val = input(f'Enter the value of parameter "{param}": ')
            try:
                validate_parameters_value(val)
            except IncorrectParametersValueError as err:
                print(err)
                sleep(1)
                break
            if param == 'price':
                try:
                    validate_price(val)
                except ValueError as err:
                    print(err)
                    sleep(1)
                    break
            param_values[param] = val
        quantity = input('Enter the quantity of incoming product: ')
        try:
            validate_quantity(quantity)
            quant = int(quantity)
        except ValueError as err:
            print(err)
            sleep(1)
            break
        new_product.quantity = quant
        new_product.param_values = param_values
        new_product.add_product_to_db()
        print('Product has been added to the database.', end='\n\n')
        print('-----------------------------------------------------')
        sleep(1)
        break


def list_of_all_products() -> None:
    while True:
        print("----- Get a list of ALL products in the warehouse -----")
        category_name: str = input('Enter a category name '
                                   '(empty - products of all category): ')
        sleep(1)
        print("Enter the start date of the search period "
              "(empty - don't limit).\n"
              "Input format: \033[3m YYYY-MM-DD (Y - year, M - month, D day).")
        start_date = input('Start of period: ')
        if start_date == '':
            min_date = 0.0
            sleep(0.5)
        else:
            try:
                min_date = validate_date(start_date)
                sleep(0.5)
            except IncorrectDateInputError as err:
                print(err)
                sleep(1)
                break
        print("Enter the end date of the search period "
              "(empty - don't limit).\n"
              "Input format: \033[3m YYYY-MM-DD (Y - year, M - month, D day).")
        end_date = input('End of period: ')
        if end_date == '':
            max_date = time()
            sleep(0.5)
        else:
            try:
                max_date = validate_date(end_date)
                sleep(0.5)
            except IncorrectDateInputError as err:
                print(err)
                sleep(1)
                break
        products = Product(category_name)
        result = products.get_all_products(min_date, max_date)
        print('All products in the warehouse:')
        print(*result)
        print('------------------------------------------------------')
        sleep(1)
        break


def info_about_product() -> None:
    while True:
        print('----- Get info about CONCRETE product. -----')
        product_id = input('Enter ID of searched product: ')
        try:
            validate_id(product_id)
            prod_id = int(product_id)
        except ValueError as err:
            print(err)
            sleep(1)
            break
        product = Product()
        result = product.get_product_info(prod_id)
        if result == dict():
            print(f'There is no product with ID "{product_id}" in database.')
        else:
            info = result
            available = info.pop('available')
            for keys, values in info.items():
                print(f'{keys} : {values}')
            if available:
                print('The product is available for purchase.')
            else:
                print('The product is not available for purchase.')
        print('------------------------------------------------------')
        sleep(1)
        break


def product_order() -> None:
    while True:
        order_dict: dict = dict()
        print('               ----- New order ----')
        print('Enter the id of the product you want to buy, then enter the '
              'quantity. When you have finished ordering, enter the '
              'word "stop".')
        while True:
            product_id = input('Enter product ID: ')
            if product_id.lower() == 'stop':
                break
            try:
                validate_id(product_id)
                pr_id: int = int(product_id)
            except ValueError as err:
                print(err)
                sleep(0.5)
                continue
            quantity = input(f'Enter quantity of the product with ID '
                             f'{product_id}: ')
            try:
                validate_quantity(quantity)
                quant: int = int(quantity)
            except ValueError as err:
                print(err)
                sleep(0.5)
                break
            order_dict[pr_id] = order_dict.get(product_id, 0) + quant
        sleep(1)
        order = Order()
        ord_info = order.check_available_product(order_dict)
        if ord_info[0] == 'NO':
            print(ord_info[1])
            print('--------------------------------------------------')
            sleep(1)
            break
        print(ord_info[1])
        print('Your order is correct? ')
        ans = input('Enter "NO" if you want to change the order;'
                    ' enter ANY another value if order is correct.')
        if ans.lower() == 'no':
            sleep(1)
            continue
        else:
            order_inform = order.gen_order_info(order_dict)
            order.create_order(order_inform)
            print('The order was placed')
            print('--------------------------------------------------')
            sleep(1)
            break


def create_statistic() -> None:
    while True:
        print('       ----- Get statistics -----')
        sleep(0.5)
        print("Enter the start date of the statistics generation period "
              "(empty - don't limit).\n"
              "Input format: \033[3m YYYY-MM-DD (Y - year, M - month, D day).")
        start_date = input('Start of period: ')
        if start_date == '':
            min_date: float = 0.0
            sleep(0.5)
        else:
            try:
                min_date = validate_date(start_date)
                sleep(0.5)
            except IncorrectDateInputError as err:
                print(err)
                sleep(1)
                break
        print("Enter the end date of the statistics generation period "
              "(empty - don't limit).\n"
              "Input format: \033[3m YYYY-MM-DD (Y - year, M - month, D day).")
        end_date = input('End of period: ')
        if end_date == '':
            max_date = time()
            sleep(0.5)
        else:
            try:
                max_date = validate_date(end_date)
                sleep(0.5)
            except IncorrectDateInputError as err:
                print(err)
                sleep(1)
                break
        statistic = Statistic(min_date=min_date, max_date=max_date)
        statistic()
        break
