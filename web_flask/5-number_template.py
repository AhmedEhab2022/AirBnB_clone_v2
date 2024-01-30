#!/usr/bin/python3

"""
 A script that starts a Flask web application
 with templates
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ display “Hello HBNB!” """

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """  display “HBNB” """

    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ display “C ” followed by the value of the text variable"""

    formated_text = text.replace("_", " ")
    return f"C {formated_text}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """ display “Python ”, followed by the value of the text variable"""

    formated_text = text.replace("_", " ")
    return f"Python {formated_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ display “n is a number” only if n is an integer"""

    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ display a HTML page only if n is an integer"""

    return render_template('5-number.html', num=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
