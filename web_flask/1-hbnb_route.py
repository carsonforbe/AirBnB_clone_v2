#!/usr/bin/python3
"""
starts flask
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns hbnb"""
    return 'HBNB'

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
