#!/usr/bin/python3
"""
Starts a Flask web application, listening on 0.0.0.0, port 5000
Routes:
    /: display "Hello HBNB!"
    /hbnb: display "HBNB"
    /c/<text>: display "C" followed by the value of the text variable
       (replace underscore _ symbols with a space )
    /python/(<text>): display "Python", followed by the value of the
         text variable (replace underscore _ symbols with a space )
    The default value of text is "is cool"
Use option strict_slashes=False in route definition
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """displays welcome message"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display c plus custom text"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/(<text>)', strict_slashes=False)
def pythoniscool(text='is cool'):
    """displays python is + custom text"""
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
