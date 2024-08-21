#!/usr/bin/python3
"""
starts flas
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns hello hbnb!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """displays 'c' followed by a value in the variable"""
    return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
