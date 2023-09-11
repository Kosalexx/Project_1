from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from interfaces import WeatherApiAdapterProtocol
    from data_access.openWeatherMap.dto import WeatherDTO


class GetWeatherService:
    def __init__(
            self,
            weather_api_adapter: WeatherApiAdapterProtocol) -> None:
        self._weather_api = weather_api_adapter

    def get_weather_in_one_city(self, city: str) -> WeatherDTO:
        weather_data = self._weather_api.get_current_weather_in_city(
            city_name=city)
        return weather_data

    def get_weather_in_cities(self, cities: list[str]) -> list[WeatherDTO]:
        result: list[WeatherDTO] = []
        for city in cities:
            weather_data = self.get_weather_in_one_city(city=city)
            result.append(weather_data)
        result.sort(
            key=lambda x: x.main.temp if (  # type: ignore
                x.main is not None) else int(x.cod),  # type: ignore
            reverse=True)

        return result
