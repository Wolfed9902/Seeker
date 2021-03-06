
from flask import render_template, url_for, redirect, request
from seeker import app

@app.route("/")
@app.route("/home")
def homepage():
    return render_template('home.html')

@app.route("/signin")
def signin():
    return render_template('signin.html')

@app.route("/listings")
def listingspage():
    return render_template('listings.html')

@app.route("/newlisting")
def newlisting():
    return render_template('newlisting.html')

@app.route("/history")
def history():
    return render_template('history.html')
