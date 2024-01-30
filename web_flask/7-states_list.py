#!/usr/bin/python3
""" start a states list Flask web application """

from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    """ Call in this method storage.close() to remove db session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ display a HTML page that list the states"""
    states = sorted(list(storage.all('State').values()), key=lambda s: s.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
