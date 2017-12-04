#
# Configurações da aplicação
#
import os
from os.path import abspath, join

DEBUG = True
SECRET_KEY = 'a secret key'

# diretório base
basedir = os.path.abspath(os.path.dirname(__name__))

# diretório base da aplicação
BASE_DIR = basedir

UPLOADS = join(join(join(basedir, 'certificates'), 'static'), 'uploads')