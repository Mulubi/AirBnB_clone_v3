#!/usr/bin/python3
"""index.py to connect to API"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'],
                 strict_slashes=False)
def hbnbStatus():
    """Status of hbnb API"""
    return jsonify({"status": "OK"})
