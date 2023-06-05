from __future__ import annotations
from dto import WeatherDTO
import requests


class WeatherDAO:
    def __init__(self, url: str, api_key: str) -> None:
        self._url = url
        self._api_key = api_key

    def one_city_request(self, city_name: str) -> WeatherDTO:
        req = requests.get(url=self._url.format(city_name=city_name,
                                                API_key=self._api_key))
        req_dict: dict = req.json()
        if req_dict['cod'] != 200:
            dto = WeatherDTO(
                code=req_dict['cod'],
                entered_name=city_name,
                message=req_dict['message'],
                description='Error',
                humidity=0,
                response_name='Error',
                temp=0)
        else:
            dto = WeatherDTO(
                code=req_dict['cod'],
                entered_name=city_name,
                message='OK',
                description=req_dict["weather"][0]["description"],
                humidity=req_dict["main"]["humidity"],
                response_name=req_dict["name"],
                temp=round((req_dict["main"]["temp"] - 273.15), 2))
        return dto

    def cities_list_request(
            self,
            cities_list: list[str]) -> list[WeatherDTO]:
        dto_list = []
        for city in cities_list:
            res = self.one_city_request(city)
            dto_list.append(res)
        return dto_list
