from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman
from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer
from flask_migrate import Migrate
from .models import db, User

csrf = CSRFProtect()
login_manager = LoginManager()
limiter = Limiter(get_remote_address, default_limits=["200 per day", "50 per hour"])
mail = Mail()
serializer = URLSafeTimedSerializer('your_secret_key')
migrate = Migrate()

csp = {
    'default-src': [
        '\'self\'',
        'https://stackpath.bootstrapcdn.com'
    ],
    'script-src': [
        '\'self\'',
        'https://stackpath.bootstrapcdn.com'
    ],
    'style-src': [
        '\'self\'',
        'https://stackpath.bootstrapcdn.com'
    ]
}

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'your_email@example.com'
    app.config['MAIL_PASSWORD'] = 'your_email_password'

    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)
    limiter.init_app(app)
    mail.init_app(app)
    Talisman(app, content_security_policy=csp)
    migrate.init_app(app, db)  # Initialize Flask-Migrate

    login_manager.login_view = 'main.login'
    login_manager.login_message_category = 'info'

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

