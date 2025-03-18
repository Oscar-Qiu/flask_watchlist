from flask import Flask
from flask import url_for
from flask import render_template
app = Flask(__name__)
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
]
name = "oscar"

@app.route("/")
def hello():
    return "<h1>Hello Totoro<h1> <img src='https://helloflask.com/totoro.gif'>"
@app.route("/welcome")
def index():
    return render_template("index.html",name=name,movies=movies)
    