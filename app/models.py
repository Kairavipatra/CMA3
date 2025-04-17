from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def set_password(self, password):
        """Hashes and sets the user's password."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Checks if the provided password matches the hashed password."""
        return check_password_hash(self.password, password)

    # Optional: This method is automatically provided by UserMixin
    # def get_id(self):
    #     return str(self.id)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=True)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)  # "Food" or "Toys"

    def __repr__(self):
        return f'<Product {self.name}>'

  
  

