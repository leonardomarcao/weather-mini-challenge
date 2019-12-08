from weather_mini_challenge.modules.open_weather_api import OpenWeatherAPI
from weather_mini_challenge.config.base import CITY_NAME, COUNTRY_ID


class App(object):
    def __init__(self):
        open_weather_api = OpenWeatherAPI(city_name=CITY_NAME,
                                          country_id=COUNTRY_ID)

