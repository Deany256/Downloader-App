from flask import Flask
from app.extensions import db, login_manager
from app.config import Config
from app.models import User

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(Config)
    app.config.from_pyfile('../instance/config.py', silent=True)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # Register blueprints
    from app.routes import main_bp
    from app.auth import auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app
