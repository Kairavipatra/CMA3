from flask import Blueprint, request, jsonify

dog_walking_bp = Blueprint('dog_walking', __name__, url_prefix='/dog-walking')

walk_schedule = []

@dog_walking_bp.route('/schedule', methods=['POST'])
def schedule_walk():
    data = request.json
    walk_schedule.append(data)
    return jsonify({"status": "Scheduled", "data": data})
