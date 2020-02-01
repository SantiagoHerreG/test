#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template, abort
from models import storage
from models.jurisdiction import Jurisdiction


app = Flask(__name__)


@app.route('/', methods=["GET"], strict_slashes=False)
def index():
    """The index of the web page"""
    n = Jurisdiction.total()
    return render_template("index.html", n=n)


@app.route('/jurisdictions', methods=["GET"], strict_slashes=False)
def jurisdictions():
    """display the jurisdictions and number of victims"""
    jurisdictions = storage.all(Jurisdiction)
    if jurisdictions is None:
        abort(404)

    return render_template('jurisdictions.html', jurisdictions=jurisdictions)


@app.teardown_appcontext
def teardown_db(exception):
    """reloads the storage on teardown"""
    storage.reload()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
