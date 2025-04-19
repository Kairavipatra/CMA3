from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager
import os

# Initialize extensions
db = SQLAlchemy()
admin = Admin(name='PawPal Admin', template_mode='bootstrap3')
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///pawpal.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    admin.init_app(app)
    login_manager.init_app(app)

    # Models
    from app.models import User, Product, Toy, HealthyFood

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # ✅ Import blueprints directly, not modules
    from app.routes.auth import auth_bp
    from app.routes.products import products_bp
    from app.routes.appointments import appointments_bp
    from app.routes.dog_walking import dog_walking_bp
    from app.routes.toys import toys_bp
    from app.routes.main import app_bp  # Assuming your main routes are here

    # ✅ Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(appointments_bp)
    app.register_blueprint(dog_walking_bp)
    app.register_blueprint(toys_bp)
    app.register_blueprint(app_bp)

    # Flask-Admin views
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Product, db.session))

    return app
