from flask import Flask

from os import getenv
from pathlib import Path
from ruamel.yaml import YAML

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail

app = Flask(__name__)



PROJECT_PATH = Path(__file__).parent.parent

def get_env(name: str) -> str:
    env = getenv(name)
    if env:
        return env
    raise RuntimeError(f'{name} not set')

def read_config(path):
    with open(str(path)) as stream:
        yaml = YAML(typ='safe', pure=True)
        config = yaml.load(stream.read())
        return config

CONFIG = read_config(PROJECT_PATH / get_env('BACKEND_CONFIG_PATH'))


postgres_config = CONFIG['postgres']


if postgres_config.get('port'):
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{postgres_config['username']}:{postgres_config['password']}@{postgres_config['host']}:{postgres_config['port']}/{postgres_config['db']}"
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{postgres_config['username']}:{postgres_config['password']}@{postgres_config['host']}/{postgres_config['db']}"


db = SQLAlchemy(app)

migrate = Migrate(app, db)

from . import models