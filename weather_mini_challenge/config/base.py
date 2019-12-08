from environs import Env

env = Env()

###############################
# START ENVIRONMENT VARIABLES #
###############################
# OPEN WEATHER API -------------------------
# API KEY FROM
API_KEY = env('api_key')
# API URL
API_URL = env('api_url')
# CITY NAME TO GET DATA ABOUT WEATHER
CITY_NAME = env('city_name')
# COUNTRY ID. THIS SHOULD BE "ISO 3166"
COUNTRY_ID = env('country_id')
# FACTOR TO CONSIDER RAIN AND TAKE AN UMBRELLA
FACTOR_TO_RAIN = env('factor_to_rain')
###############################
# END ENVIRONMENT VARIABLES   #
###############################
