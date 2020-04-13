from flask import Flask, render_template
from ..pi.pi_main import get_data

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", hum=get_data["humidity"], temp=get_data["temperature"])

@app.route("/raw_data")
def raw_data():
    return render_template("raw_data.html")