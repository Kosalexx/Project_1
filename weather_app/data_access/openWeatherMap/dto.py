from dataclasses import dataclass
from typing import Optional


@dataclass
class Coord:
    lon: Optional[float]
    lat: Optional[float]


@dataclass
class WeatherInfo:
    id: Optional[int]  # noqa
    main: Optional[str]
    description: Optional[str]
    icon: Optional[str]


@dataclass
class MainInfo:
    temp: Optional[float]
    feels_like: Optional[float]
    temp_min: Optional[float]
    temp_max: Optional[float]
    pressure: Optional[int]
    humidity: Optional[int]
    sea_level: Optional[int]
    grnd_level: Optional[int]


@dataclass
class WindInfo:
    speed: Optional[float]
    deg: Optional[int]
    gust: Optional[float]


@dataclass
class CloudInfo:
    all: Optional[int]  # noqa


@dataclass
class SysInfo:
    type: Optional[int]  # noqa
    id: Optional[int]  # noqa
    country: Optional[str]
    sunrise: Optional[int]
    sunset: Optional[int]


@dataclass
class WeatherDTO:
    coord: Optional[Coord]
    weather: Optional[list[WeatherInfo]]
    base: Optional[str]
    main: Optional[MainInfo]
    visibility: Optional[int]
    wind: Optional[WindInfo]
    clouds: Optional[CloudInfo]
    dt: Optional[int]
    sys: Optional[SysInfo]
    timezone: Optional[int]
    id: Optional[int]  # noqa
    name: Optional[str]
    cod: Optional[str | int]
    message: Optional[str]
    entered_name: Optional[str]
