from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager
from flask_migrate import Migrate  # ✅ NEW IMPORT
from config import Config  # Import Config class

# Initialize extensions
db = SQLAlchemy()
admin = Admin(name='PawPal Admin', template_mode='bootstrap3')
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Load configuration from Config class
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate = Migrate(app, db)  # ✅ ADD THIS
    admin.init_app(app)
    login_manager.init_app(app)

    # Import models
    from app.models import User, Product, Toy, HealthyFood

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    from app.routes import app as app_routes
    from app.routes import auth, products, appointments, dog_walking, toys

    app.register_blueprint(app_routes.app_bp)
    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(products.products_bp)
    app.register_blueprint(appointments.appointments_bp)
    app.register_blueprint(dog_walking.dog_walking_bp)
    app.register_blueprint(toys.toys_bp)

    # Register models for Flask-Admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Product, db.session))

    return app
