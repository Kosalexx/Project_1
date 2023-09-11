from __future__ import annotations
from typing import TYPE_CHECKING
import art  # type: ignore
from .utils import print_table
if TYPE_CHECKING:
    from interfaces import WeatherServiceProtocol


class CliApp:
    def __init__(self, weather_service: WeatherServiceProtocol) -> None:
        self._weather_service = weather_service

    def run(self) -> None:
        logo = art.text2art('Weather_now')
        start_menu = ('Chose action from main menu:\n'
                      '1 - Check one city\n'
                      '2 - Check several cities\n'
                      '3 - Exit')
        print(logo)
        while True:
            print(start_menu)
            user_choice = input('Your choice: ')
            if user_choice == '1':
                city_name = input('Enter city name: ')
                weather_data = self._weather_service.get_weather_in_one_city(
                    city=city_name
                )
                print_table([weather_data])
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
                data = self._weather_service.get_weather_in_cities(
                    cities=cities_list
                )
                print_table(data)
                continue
            elif user_choice == '3':
                print('GOODBYE!')
                break
            else:
                print('Choice must be digit from 1 to 3.')
                continue
