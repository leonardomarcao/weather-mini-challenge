from os.path import join, dirname, abspath
from dotenv import load_dotenv
from pathlib import Path

# .env file
BASE_DIR = str(Path(dirname(abspath(__file__))).parent.parent)
CONFIG_DIR = str(Path(dirname(abspath(__file__))))
dot_env = join(BASE_DIR, '.env')
load_dotenv(dot_env)
