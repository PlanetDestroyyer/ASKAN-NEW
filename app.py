from flask import Flask, render_template, request, redirect, session, url_for, flash
from pymongo import MongoClient
from waitress import serve 

app = Flask(__name__, static_url_path='/static')
app.config["MONGO_URI"] = "mongodb+srv://wrieddude:Pranav369@cluster0.xu62g1z.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient("mongodb+srv://wrieddude:Pranav369@cluster0.xu62g1z.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('askan')

records = db.user

app.secret_key = 'askan_hydroponics'

@app.route("/")
def main():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = records.find_one({"username": username})

        if user is not None:
            if user['password'] == password:
                session['username'] = username 
                return redirect('/home')
            else:
                return render_template('login.html', info="Invalid Username or Password")
        else:
            return render_template('login.html', info="User Not Found")



@app.route("/login-home", methods=["POST"])
def login_home():
    return render_template('home.html')

@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/signin-home", methods=["POST"])
def signin_home():
    full_name = request.form.get("fullname")
    username = request.form.get("username")
    password = request.form.get("password")
    cfn_password = request.form.get("confirmPassword")
    area_of_working = request.form.get("areaOfWork")
    country = request.form.get("country")
    gender = request.form.get("gender")
    qualification = request.form.get("qualification")
    purpose = request.form.get("purpose")
    phone = request.form.get("phone")
    email = request.form.get("email")

    new_user = {
        "fullname": full_name,
        "username" : username,
        "password" : password,
        "Area_of_Working" : area_of_working,
        "country" : country,
        "gender" : gender,
        "qualification": qualification,
        "purpose": purpose,
        "phone" : phone,
        "email" : email
    }

    if password == cfn_password :
        records.insert_one(new_user)
        
        return redirect('/')
    else:
        return render_template('/signup.html',info="Yours Passwords Dont Match Please Check it once")


   



@app.route("/signup")
def signup():
    return render_template('/signup.html')

@app.route("/about-us")
def about():
    return render_template('/aboutus.html')

@app.route("/contact-us")
def contact():
    return render_template('/contact_us.html')

@app.route("/profile")
def profile():
    if 'username' in session:
        username = session['username']
        user = records.find_one({"username": username})
        if user:
            return render_template('/profile.html', user=user)


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
    serve(app, host="0.0.0.0", port=8080)