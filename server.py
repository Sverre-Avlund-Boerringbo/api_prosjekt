from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def side_index():
    return render_template("index.html")

@app.route("/lag/")
def side_lag():
    return "TODO!"

@app.route("/se/")
def side_se():
    return "TODO!"
