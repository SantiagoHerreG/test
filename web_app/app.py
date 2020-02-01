#!/usr/bin/python3
"""starts a Flask web application
"""
from flask import Flask, render_template, abort, request
from models import storage
from models.jurisdiction import Jurisdiction
import datetime
from web_app.control_functions import is_valid_jurisdiction
from web_app.control_functions import database_valid_names
from web_app.control_functions import words_to_number


app = Flask(__name__)


@app.route('/reset_data', methods=["GET"], strict_slashes=False)
def reset_data():
    """Asks for reseting the database"""
    return render_template("reset_data.html")


@app.route('/reset_answer', methods=["POST"], strict_slashes=False)
def reset_answer():
    """Resets the data"""
    data = request.form
    if data["answer"] == "YES":
        storage.reset()
        return "Database restarted", 200

    return "Database untouched", 200


@app.route('/post_data', methods=["POST", "PUT"], strict_slashes=False)
def index_post():
    """Posted data handling"""
    data = request.form
    name = data["name"]
    value = data["victims"]

    if is_valid_jurisdiction(name, "Colombia") is False:
        return "Not a valid jurisdiction", 400

    value = words_to_number(value)
    if value is None:
        return "Not a valid number", 400

    jurisdiction = storage.get(Jurisdiction, name)
    if jurisdiction is None:
        new_jurisd = Jurisdiction(**{"name": name, "victims": value})
        storage.save()
        return "New jurisdiction added succesfully", 201
    else:
        jurisdiction.update(value)
        storage.save()
        return "Jurisdiction updated succesfully", 200


@app.route('/', methods=["GET"], strict_slashes=False)
def index():
    """The index of the web page"""
    n = Jurisdiction.total()
    return render_template("index.html", n=n, time=datetime.datetime.today(),
                           jurisdictions=database_valid_names["Colombia"])


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
