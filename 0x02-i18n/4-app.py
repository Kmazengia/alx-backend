#!/usr/bin/env python3
"""
a python module to initiate a flask app using Babel
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """
    a class to configure babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    get_locale - function to get the local selector
    """
    lcl = request.args.get('locale', None)
    if lcl and lcl in app.config['LANGUAGES']:
        return lcl
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def Welcome():
    """
    Welcome - a route to a 4-index html
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
