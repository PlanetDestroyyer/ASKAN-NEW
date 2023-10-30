from flask import Flask, render_template, request, redirect
from crops import *

app = Flask(__name__, static_url_path='/static')



@app.route("/")
def main():
    return render_template("login.html")

@app.route("/login-home", methods=["POST"])
def login_home():
    return render_template('home.html')

@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/sign-home", methods=["POST"])
def sigin_home():
    return render_template('home.html')


@app.route("/login")
def login():
    return render_template('/login.html')

@app.route("/sign")
def sign():
    return render_template('/signup.html')

@app.route("/aboutus")
def about():
    return render_template('/aboutus.html')

@app.route("/contactus")
def contact():
    return render_template('/contact_us.html')

@app.route("/profile")
def profile():
    return render_template('/profile.html')

@app.route("/activity")
def activity():
    return render_template('/activity.html')

@app.route("/crops_entry")
def crops_entry():
    return render_template('/Crops_Entry.html')

@app.route("/Equipment_Management")
def equipment_management():
    return render_template('/Equipment_Management.html')


if __name__ == "__main__":
    app.run(debug=True)  
