from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/signIn")
def signIn():
    return render_template("signIn.html")


@app.route("/signUp")
def signUp():
    return render_template("signUp.html")