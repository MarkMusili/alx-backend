#!/usr/bin/env python3
"""
Flask Babel configuration
"""
import babel
import gettext
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config class for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    """
    Get locale from request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

home_title = _("Welcome to Holberton")
home_header = _("Hello world")

@app.route('/')
def index():
    return render_template('3-index.html')

if __name__ == '__main__':
    app.run(debug=True)
