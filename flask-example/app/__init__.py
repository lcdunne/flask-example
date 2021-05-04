from flask import Flask
from config import BaseConfig
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)

from .main.routes import main_bp
from .admin_api.endpoints import api_bp

app.register_blueprint(main_bp)
app.register_blueprint(api_bp, url_prefix='/api')
