import prettytable
import art  # type: ignore
from dao import WeatherDAO
from dto import WeatherDTO
from typing import Type
from config import URL, API_KEY


logo = art.text2art('Weather_forecast')
start_menu = ('Chose action from main menu:\n'
              '1 - Check one city\n'
              '2 - Check several cities\n'
              '3 - Exit')


def print_table(dto_list: list[Type[WeatherDTO]]) -> None:
    mytable = prettytable.PrettyTable()
    mytable.field_names = ["city", "temp, C", "description", "humidity"]
    errors_list = []
    for dto in dto_list:
        if dto.code != 200:
            error_message = (f"Entered city name: {dto.entered_name}. Error "
                             f"code: {dto.code}. Message: {dto.message}.")
            errors_list.append(error_message)
        else:
            mytable.add_row([dto.response_name, dto.temp, dto.description,
                             dto.humidity])
    print(mytable)
    if errors_list != []:
        for row in errors_list:
            print(row)


def ui_func() -> None:
    print(logo)
    while True:
        print(start_menu)
        user_choice = input('Your choice: ')
        if user_choice == '1':
            city_name = input('Enter city name: ')
            res = WeatherDAO(url=URL, api_key=API_KEY)
            result_dto = res.one_city_request(city_name=city_name.lower())
            print_table([result_dto])
            continue
        elif user_choice == '2':
            print('Enter the names of all cities. '
                  'Each city name is entered on a new line.\n'
                  'When you have finished entering city names, enter '
                  'the word "Stop".')
            cities_list = []
            while True:
                name = input()
                if name.lower() == 'stop':
                    break
                else:
                    cities_list.append(name)
            res = WeatherDAO(url=URL, api_key=API_KEY)
            result_dto_list = res.cities_list_request(cities_list=cities_list)
            print_table(result_dto_list)
            continue
        elif user_choice == '3':
            print('GOODBYE!')
            break
        else:
            print('Choice must be digit from 1 to 3.')
            continue
