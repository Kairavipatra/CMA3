from flask import Blueprint, jsonify

toys_bp = Blueprint('toys', __name__, url_prefix='/toys')

@toys_bp.route('/')
def toy_list():
    return jsonify([
        {"name": "Plush Chew Toy", "price": 300},
        {"name": "Squeaky Bone", "price": 250}
    ])
