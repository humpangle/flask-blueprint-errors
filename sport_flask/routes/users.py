from flask import Blueprint, jsonify, request


users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.route("", methods=["GET"])
def get_all_users():
    all_users = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"},
    ]
    return jsonify(all_users)


@users_bp.route("", methods=["POST"])
def create_user():
    d = request.json
    return jsonify(d), 201
