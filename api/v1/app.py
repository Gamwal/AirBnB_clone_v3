#!/usr/bin/python3
""" """

from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
import os
import api.v1.views.index


# Create the Flask app
app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(exception):
    """
    Teardown function to close the database connection after each request.

    Args:
        exception: An exception object if there was an exception during the request.
    """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})

if __name__ == "__main__":
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
