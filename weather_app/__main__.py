import requests

from data_access.openWeatherMap.client import OpenWeatherMap
from business_logic.services import GetWeatherService
from presentation.cli.app import CliApp


def run_cli() -> None:
    with requests.Session() as session:
        weather_api = OpenWeatherMap(session=session)
        weather_service = GetWeatherService(weather_api_adapter=weather_api)
        app = CliApp(weather_service=weather_service)
        app.run()


if __name__ == '__main__':
    run_cli()
