#!/usr/bin/python3
""" """

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    status_data = {
            'status': 'OK'
            }
    return jsonify(status_data)

@app_views.route('/stats', methods=['GET'])
def stats():
    stats = {
            "amenities": storage.count("Amenity"),
            "cities": storage.count("City"),
            "places": storage.count("Place"),
            "reviews": storage.count("Review"),
            "states": storage.count("State"),
            "users": storage.count("User"),
            }
    return jsonify(stats)
