from flask import Blueprint, request, jsonify
from app import db  # Correct import
from app.models import toys, food  # Correct import for your models

products_bp = Blueprint('products', __name__)

@products_bp.route('/toys', methods=['POST'])
def add_toy():
    data = request.get_json()
    new_toy = Toy(name=data['name'], description=data.get('description'), price=data['price'])
    db.session.add(new_toy)
    db.session.commit()
    return jsonify({'message': 'Toy added successfully'}), 201

@products_bp.route('/toys', methods=['GET'])
def get_toys():
    toys = Toy.query.all()
    return jsonify([{'id': toy.id, 'name': toy.name, 'description': toy.description, 'price': toy.price} for toy in toys])

@products_bp.route('/healthy-foods', methods=['POST'])
def add_healthy_food():
    data = request.get_json()
    new_food = HealthyFood(name=data['name'], description=data.get('description'), price=data['price'])
    db.session.add(new_food)
    db.session.commit()
    return jsonify({'message': 'Healthy food added successfully'}), 201

@products_bp.route('/healthy-foods', methods=['GET'])
def get_healthy_foods():
    foods = HealthyFood.query.all()
    return jsonify([{'id': food.id, 'name': food.name, 'description': food.description, 'price': food.price} for food in foods])
