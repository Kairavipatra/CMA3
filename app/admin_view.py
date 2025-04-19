#from flask_admin import Admin
#from flask_admin.contrib.sqla import ModelView
#from app import app, db
#from app.models import User, Product

#admin = Admin(app, name='PawPal Admin', template_mode='bootstrap3')

#admin.add_view(ModelView(User, db.session))
#admin.add_view(ModelView(Product, db.session))

#if __name__ == '__main__':
 #   app.run(debug=True)

from flask import Flask, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, current_user
from flask_migrate import Migrate  # ✅ Flask-Migrate
import os

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
admin = Admin(name='PawPal Admin', template_mode='bootstrap3')
migrate = Migrate()  # ✅ Initialize migrate instance here


# Custom Admin Home View (restrict access to logged-in users)
class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.url))


# Protect individual model views
class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.url))


def create_app():
    app = Flask(__name__)
    
    # Secret Key
    app.config['SECRET_KEY'] = 'your_secret_key_here'

    # Database Config (PostgreSQL for deployment, SQLite for fallback)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///pawpal.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)  # ✅ Properly init Flask-Migrate with app and db

    # User loader for Flask-Login
    from app.models import User  # Avoid circular imports
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Initialize Flask-Admin with protected views
    secure_admin = Admin(app, name='PawPal Admin', template_mode='bootstrap3', index_view=MyAdminIndexView())

    # Register models with admin
    from app.models import Product, Toy, HealthyFood
    secure_admin.add_view(SecureModelView(User, db.session))
    secure_admin.add_view(SecureModelView(Product, db.session))
    secure_admin.add_view(SecureModelView(Toy, db.session))
    secure_admin.add_view(SecureModelView(HealthyFood, db.session))

    # Register blueprints
    from app.routes import app as app_routes
    from app.routes import auth, products, appointments, dog_walking, toys

    app.register_blueprint(app_routes.app_bp)
    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(products.products_bp)
    app.register_blueprint(appointments.appointments_bp)
    app.register_blueprint(dog_walking.dog_walking_bp)
    app.register_blueprint(toys.toys_bp)

    return app



