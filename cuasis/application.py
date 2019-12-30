import cs50
import csv
import urllib.request

from flask import Flask, jsonify, redirect, render_template, request


# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    if not request.form.get("name"):
        return render_template("error.html", message="Debes ingresar tu nombre para reportar una condición peligrosa")
    file = open("survey.csv", "a")
    writer = csv.writer(file)
    writer.writerow((request.form.get("name"), request.form.get("title"), request.form.get("evaluation"), request.form.get("situacion"), request.form.get("potencial"), request.form.get("accion")))
    file.close()
    return render_template("form.html")


@app.route("/sheet", methods=["GET"])
def get_sheet():

    print('Beginning file download with urllib2...')
    url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
    urllib.request.urlretrieve(url, '/cuasis/survey.csv')
