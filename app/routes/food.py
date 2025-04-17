from flask import Blueprint, render_template
from app.models import Product

food_bp = Blueprint('food', __name__, url_prefix='/food')

@food_bp.route('/')
def show_food():
    foods = Product.query.filter_by(category="Food").all()
    return render_template('food.html', foods=foods)
