#!/usr/bin/python3
""" """

from . import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def status():
    status_data = {
            'status': 'OK'
            }
    return jsonify(status_data)
