#!/usr/bin/python3
"""Start the Flask web applications.

The application listen on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Displays 'Hello HBNB!'"""
    return render_template("10-hbnb_filters.py")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)

