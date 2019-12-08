from weather_mini_challenge.modules.open_weather_api import OpenWeatherAPI
from weather_mini_challenge.config.base import CITY_NAME, COUNTRY_ID
import pandas as pd


class App(object):
    def __init__(self):
        self.open_weather_api = OpenWeatherAPI(city_name=CITY_NAME,
                                               country_id=COUNTRY_ID)
        self.df = pd.DataFrame(self.open_weather_api.forecast_by_name())
        



