from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_pymongo import PyMongo

app = Flask(__name__, static_url_path='/static')
app.config['MONGO_URI'] = "mongodb+srv://wrieddude:Pranav369@cluster0.xu62g1z.mongodb.net/?retryWrites=true&w=majority"
mongo = PyMongo(app)




@app.route("/")
def main():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    return render_template('home.html')




@app.route("/login-home", methods=["POST"])
def login_home():
    return render_template('home.html')

@app.route("/home")
def home():
    return render_template('home.html')
    

@app.route("/sign-home", methods=["POST"])
def sigin_home():
    return render_template('home.html')



@app.route("/sign")
def sign():
    return render_template('/signup.html')

@app.route("/about-us")
def about():
    return render_template('/aboutus.html')

@app.route("/contact-us")
def contact():
    return render_template('/contact_us.html')

@app.route("/profile")
def profile():
    return render_template('/profile.html')

@app.route("/activity")
def activity():
    return render_template('/activity.html')

@app.route("/crops-entry")
def crops_entry():
    return render_template('/Crops_Entry.html')

@app.route("/Equipment-Management")
def equipment_management():
    return render_template('/Equipment_Management.html')

@app.route("/products")
def products():
    return render_template('/products.html')

if __name__ == "__main__":
    server(app, host="0.0.0.0", port=8080)
