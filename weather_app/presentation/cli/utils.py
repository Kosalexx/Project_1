from __future__ import annotations
import prettytable
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from data_access.openWeatherMap.dto import WeatherDTO


def print_table(dto_list: list[WeatherDTO]) -> None:
    mytable = prettytable.PrettyTable()
    mytable.field_names = ["city", "temp, C", "description", "humidity"]
    errors_list = ['ERRORS:',]
    for dto in dto_list:
        if dto.cod != 200:
            error_message = (f"Entered city name: {dto.entered_name}. Error "
                             f"code: {dto.cod}. Message: {dto.message}.")
            errors_list.append(error_message)
        else:
            mytable.add_row([
                dto.name, dto.main.temp,  # type: ignore
                dto.weather[0].description, dto.main.humidity])  # type: ignore
    if len(errors_list) == len(dto_list) + 1:
        for row in errors_list:
            print(row)
    else:
        print(mytable)
        if errors_list != ['ERRORS:',]:
            for row in errors_list:
                print(row)
