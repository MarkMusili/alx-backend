#!/usr/bin/env python3
"""
Flask app implimentation
"""
from typing import Any
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> Any:
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
