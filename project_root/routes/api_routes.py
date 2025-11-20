from flask import Blueprint, render_template, jsonify


api_bp = Blueprint('api',__name__, url_prefix="/api")


@api_bp.route("/status")
def status():
    return jsonify({"status": "OK"})