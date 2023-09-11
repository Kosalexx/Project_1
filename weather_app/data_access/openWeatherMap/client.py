from __future__ import annotations
from dacite import from_dict
from typing import TYPE_CHECKING, Any, Optional, TypeVar
from config import OWM_API_KEY, OWM_BASE_URL, URL_PATH
from .dto import WeatherDTO
if TYPE_CHECKING:
    from requests import Session, Response


T = TypeVar('T')


class OpenWeatherMap:
    def __init__(self, session: Session) -> None:
        self.__session = session

    def _requests(
            self,
            method: str,
            url_path: str,
            headers: Optional[dict[str, Any]] = None,
            params: Optional[dict[str, Any]] = None,
            json: None = None,
            data: None = None
    ) -> Response:
        url = OWM_BASE_URL + url_path
        res = self.__session.request(method=method, url=url, params=params,
                                     headers=headers, json=json, data=data)
        return res

    def _get(
            self,
            model: type[T],
            url_path: str,
            params: dict[str, Any]) -> T:
        resp = self._requests('GET', url_path=url_path, params=params)
        result_dto = from_dict(model, resp.json())
        return result_dto

    def get_current_weather_in_city(self, city_name: str) -> WeatherDTO:
        resp = self._get(
            WeatherDTO, url_path=URL_PATH,
            params={'q': city_name, 'appid': OWM_API_KEY, 'units': 'metric'})
        resp.entered_name = city_name
        return resp
