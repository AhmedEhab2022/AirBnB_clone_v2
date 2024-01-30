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


@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """ display “Python ”, followed by the value of the text variable"""

    formated_text = text.replace("_", " ")
    return f"Python {formated_text}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
