from __future__ import annotations
from dto import WeatherDTO
from typing import Type
import requests


class WeatherDAO:
    def __init__(self, url: str, api_key: str) -> None:
        self._url = url
        self._api_key = api_key

    def one_city_request(self, city_name: str) -> Type[WeatherDTO]:
        req = requests.get(url=self._url.format(city_name=city_name,
                                                API_key=self._api_key))
        req_dict: dict = req.json()
        dto = WeatherDTO
        dto.code = req_dict['cod']
        dto.entered_name = city_name
        if req_dict['cod'] != 200:
            dto.message = req_dict['message']
            dto.description = 'Error'
            dto.humidity = 0
            dto.response_name = 'Error'
            dto.temp = 0
        else:
            dto.message = 'OK'
            dto.description = req_dict["weather"][0]["description"]
            dto.humidity = req_dict["main"]["humidity"]
            dto.response_name = req_dict["name"]
            dto.temp = round((req_dict["main"]["temp"] - 273.15), 2)
        return dto

    def cities_list_request(
            self,
            cities_list: list[str]) -> list[Type[WeatherDTO]]:
        dto_list = []
        for city in cities_list:
            res = self.one_city_request(city)
            dto_list.append(res)
        return dto_list
