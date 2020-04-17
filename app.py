from flask import Flask, render_template, jsonify, redirect, url_for
from src.dataminer import Dataminer
from core import Database

app = Flask(__name__)
db = Database()
dm = Dataminer()

@app.route("/login")
def login():
    return render_template("login.html", title="Tomato | Login")

@app.route("/")
def index():
    return render_template("index.html", hum=dm.get_h_t()["humidity"], temp=dm.get_h_t()["temperature"], title="Tomato")

@app.route("/raw_data")
def raw_data():
    return render_template("raw_data.html")

@app.route("/init")
def init():
    db.setup()
    return redirect(url_for("index"))

@app.route("/config")
def config():
    return "Config stuff soon"


if __name__ == "__main__":
    try:
        db.setup()
        app.run(debug=True, port=8080, threaded=True, host="0.0.0.0")
    except:
        app.run(debug=True, port=8080, threaded=True, host="0.0.0.0")