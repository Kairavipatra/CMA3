from flask import Blueprint, render_template
from app.models import Product

toys_bp = Blueprint('toys', __name__, url_prefix='/toys')

@toys_bp.route('/')
def show_toys():
    toys = Product.query.filter_by(category="Toys").all()
    return render_template('toys.html', toys=toys)
