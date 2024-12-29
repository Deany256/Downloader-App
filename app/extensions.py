from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .yt_dlp_utils import YTDLPUtils

db = SQLAlchemy()
login_manager = LoginManager()
yt_utils = YTDLPUtils()