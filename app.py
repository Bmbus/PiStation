from flask import Flask, render_template, jsonify, redirect, url_for
from src.dataminer import get_h_t
from core.database import Database

app = Flask(__name__)
db = Database()


@app.route("/")
def index():
    return render_template("index.html", hum=get_h_t()["humidity"], temp=get_h_t()["temperature"])

@app.route("/raw_data")
def raw_data():
    return render_template("raw_data.html")

@app.route("/init")
def init():
    db.init_db()
    return redirect(url_for("index"))

@app.route("/config")
def config():
    return "Config stuff soon"


if __name__ == "__main__":
    try:
        db.init_db()
        app.run(debug=True, port=8080, threaded=True)
    except:
        app.run(debug=True, port=8080, threaded=True)