from application import app
from flask import render_template, session, redirect, url_for, flash, request
from application.models import User
from application.forms import LoginForm, RegisterForm
from random import randint
from application.common import save, get_all, get_one
@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    values = []
    poles = []
    if request.method == "POST":
        request.form["level"]
        if request.form["level"] == "easy":
            for i in range(5):
                value = randint(0, 5)
                values.append(value)
                poles.append("Pole " + str(i))
        elif request.form["level"] == "medium":
            for i in range(10):
                value = randint(0, 10)
                values.append(value)
                poles.append("Pole " + str(i))
        else:
            for i in range(20):
                value = randint(0, 20)
                values.append(value)
                poles.append("Pole " + str(i))
    return render_template("barchart.html", index=True, values=values, poles=poles)

@app.route("/login", methods=["GET", "POST"])
def login():
    # if session.get("username"):
    #     return redirect(url_for("index"))
    # form = LoginForm()
    # if form.validate_on_submit():
    #     email = form.email.data
    #     password = form.password.data
        # user = User.objects(email=email).first()
        # if user and user.get_password(password):
        #     flash(f"{user.first_name}, you are successfully logged in!", "success")
        #     session['user_id'] = user.user_id
        #     session['username'] = user.first_name         
        #     return redirect("/index")
        # else:
        #     flash("Something is wrong!", "danger")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
    return render_template("login.html", title="Login", login=True)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        password_confirm = request.form.get("password_confirm")
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        if password != password_confirm:
            flash("Passwords do not match!", "danger")
        else:
            user = User(username, firstname, lastname, email, password)
            # user.save()
            save(user)
            flash(f"{user.get_firstname()}, you are successfully registered!", "success")
            return redirect(url_for("index"))
    return render_template("register.html", title="Register", register=True)

@app.route("/logout")
def logout():
    session["user_id"]=False
    session.pop("username", None)
    return redirect(url_for("index"))