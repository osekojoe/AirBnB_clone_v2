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
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n” inside the tag BODY
    /number_odd_or_even/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n is even|odd” inside the tag BODY
Use option strict_slashes=False in route definition
"""


from flask import Flask, render_template
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
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """displays python is + custom text"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def isnumber(n):
    """display n only if n is integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def is_even_or_odd(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        state = 'even'
    else:
        state = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           state=state)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
