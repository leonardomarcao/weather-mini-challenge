from weather_mini_challenge.modules.utils import Utils
from weather_mini_challenge.config.base import (
    API_KEY,
    API_URL,
    MESSAGE_BODY,
    FACTOR_TO_RAIN
)
import requests
import json
import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'


class OpenWeatherAPI(object):
    """
    This class is responsible to make requests in OpenWeatherAPI
    and obtains information about "5 day / 3 hour forecast"
    ...
    Attributes
    ----------
    city_name : str
        City name which you you want get data about
    country_id : str
        Country id (ISO 3166)
    """
    def __init__(self, **kwargs):
        try:
            self.city_name = kwargs['city_name']
            self.country_id = kwargs['country_id']
        except KeyError:
            pass

    @property
    def city_name(self):
        return self.__city_name

    @city_name.setter
    def city_name(self, name):
        self.__city_name = name

    @property
    def country_id(self):
        return self.__country_id

    @country_id.setter
    def country_id(self, id):
        self.__country_id = id

    @classmethod
    def api_key(cls):
        return API_KEY

    @classmethod
    def api_url(cls):
        return API_URL

    def forecast_by_name(self):
        params = dict(
            q=f'{self.city_name}' + ',' + f'{self.country_id}',
            appid=f'{self.api_key()}'
        )
        req = requests.get(f'{API_URL}/forecast', params=params)
        if req.status_code == 200:
            req = json.loads(req.text)
            return req['list']
        else:
            return req.status_code

    def get_df_humidity_next_five_days(self):
        utils = Utils()
        df = pd.DataFrame(self.forecast_by_name())
        df = utils.cast_columns(df, columns={'dt_txt': 'date'})
        df['humidity'] = 0
        for i, row in df.iterrows():
            df['humidity'][i] = df['main'][i]['humidity']
        return df[['humidity', 'dt_txt']].groupby(df['dt_txt']).agg({'humidity': ['mean']})['humidity']

    def display_message_take_an_umbrella(self):
        df = self.get_df_humidity_next_five_days()
        days = ''
        for i, row in df.iterrows():
            if row['mean'] > FACTOR_TO_RAIN:
                days += f'\n{i.strftime("%A")}'
        print(MESSAGE_BODY+days)
