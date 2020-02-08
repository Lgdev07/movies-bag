from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from resources.errors import errors
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from dotenv import load_dotenv

import os

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')

load_dotenv()

mail = Mail(app)
from resources.routes import initialize_routes

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['MONGODB_SETTINGS'] = {
  'host': os.getenv("MONGODB_URL")
}

initialize_db(app)
initialize_routes(api)
