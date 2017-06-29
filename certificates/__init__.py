from flask import Flask

app = Flask(__name__)

# Carrega as configurações a partir de config.py
app.config.from_object('config')

from certificates import controllers
from certificates import utils