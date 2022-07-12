from flask import Blueprint, jsonify
from werkzeug.exceptions import NotFound

errors_bp = Blueprint("errors", __name__)


@errors_bp.app_errorhandler(NotFound)
def not_found_error():
    return jsonify({"message": "This resource is not available"}), 404


@errors_bp.app_errorhandler(Exception)
def catch_all_error():
    return jsonify({"message": "Unknown error occurred"}), 500
