from datetime import datetime
from flask import Flask, render_template
from . import app

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("jsfxn.html")

@app.route("/celtics/")
def appleprice():
    return render_template("celtics.html")

@app.route("/analysis/")
def analysis():
    return render_template("Trial.html")

@app.route("/forecastedweather/")
def forecastedweather():
    return render_template("forecasted.html")

@app.route("/forecastedweather2/")
def forecastedweather2():
    return render_template("forecasted2.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
