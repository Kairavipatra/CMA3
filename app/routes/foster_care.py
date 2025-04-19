from flask import Blueprint, request, jsonify

foster_care_bp = Blueprint('foster_care', __name__, url_prefix='/foster-care')

# This will store foster care inquiries or applications
foster_requests = []

@foster_care_bp.route('/apply', methods=['POST'])
def apply_foster():
    data = request.json
    foster_requests.append(data)
    return jsonify({"status": "Application Received", "data": data})

@foster_care_bp.route('/list', methods=['GET'])
def list_fosters():
    return jsonify({"available_fosters_in_airoli": [
        {"name": "Airoli Pet Foster Home", "address": "Plot 12, Sector 8A, Airoli, Navi Mumbai", "contact": "9876543210"},
        {"name": "Paw Haven", "address": "Sector 4, Airoli, Navi Mumbai", "contact": "9123456789"},
        {"name": "Furry Friends Shelter", "address": "Near Mindspace, Airoli, Navi Mumbai", "contact": "9812345678"}
    ]})
