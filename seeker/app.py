from flask import Flask, request, render_template

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
@app.route("/home")
def homepage():
    return render_template('home.html')

@app.route("/listings")
def listingspage():
    return render_template('listings.html')

if __name__ == '__main__':
    app.run(debug=True)
