from dataclasses import dataclass


@dataclass
class CityDTO:
    country_id: int
    name: str
