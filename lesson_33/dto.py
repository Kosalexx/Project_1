from dataclasses import dataclass


@dataclass
class WeatherDTO:
    code: str
    entered_name: str
    response_name: str
    description: str
    humidity: int
    temp: float
    message: str
