import os
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
    # SendGrid setup
    # MAIL_USERNAME = 'apikey'  # os.environ.get('SENDGRID_MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('SENDGRID_MAIL_API_KEY')
    # MAIL_SERVER = 'smtp.sendgrid.net'
    # MAIL_USE_TLS = True
    # MAIL_PORT = 587  # if using SSL, port should be 465
    # MAIL_DEFAULT_SENDER = os.environ.get('SENDGRID_MAIL_DEFAULT_SENDER')

    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_USE_TLS = True
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_USERNAME')
