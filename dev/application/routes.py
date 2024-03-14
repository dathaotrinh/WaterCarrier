from application import app
from application.timer import CountUpTimer
from flask import render_template, session, redirect, url_for, flash, request, jsonify
from application.models import User
from application.forms import LoginForm, RegisterForm
from random import randint
from application.common import save, get_all, get_one, start_timer, stop_timer, algorithm, reset

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    values = []
    poles = []
    timerStart = "False"
    if request.method == "POST":
        if request.form["level"] == "easy":
            timerStart = "True"
            start_timer()
            reset(values, poles)
            for i in range(5):
                value = randint(1, 5)
                values.append(value)
                poles.append("Pole " + str(i))
        elif request.form["level"] == "medium":
            timerStart = "True"
            start_timer()
            reset(values, poles)
            for i in range(10):
                value = randint(1, 10)
                values.append(value)
                poles.append("Pole " + str(i))
        elif request.form["level"] == "hard":
            timerStart = "True"
            start_timer()
            reset(values, poles)
            for i in range(20):
                value = randint(0, 20)
                values.append(value)
                poles.append("Pole " + str(i))
        elif request.form["level"] == "stop":
            timerStart = "False"
            stop_timer()
        # else:
        #     timerStart = "False"
        #     time = stop_timer()
        #     waterAmount = request.form.get("waterAmount")
        #     possibleSolution = request.form.get("possibleSolution")
        #     container = request.form.get("container")
        #     result = algorithm(values)
        #     reset(values, poles)
    return render_template("barchart.html", index=True, values=values, poles=poles, timerStart=timerStart)

@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("username"):
        return redirect(url_for("index"))
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        current_user = get_one(username)
        if(current_user):
            current_user = User(*current_user)
            if current_user.get_password() == password:
                flash(f"{current_user.get_firstname()}, you are successfully logged in!", "success")
                session['userid'] = current_user.get_userid()
                session['username'] = current_user.get_username()
                return redirect("/index")
            else:
                flash("Something is wrong!", "danger")
    return render_template("login.html", title="Login", login=True)


@app.route("/register", methods=["GET", "POST"])
def register():
    if session.get("username"):
        return redirect(url_for("index"))
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
            save(user)
            flash(f"{user.get_firstname()}, you are successfully registered!", "success")
            return redirect(url_for("index"))
    return render_template("register.html", title="Register", register=True)

@app.route("/logout")
def logout():
    session["userid"]=False
    session.pop("username", None)
    return redirect(url_for("index"))

@app.route("/profile")
def profile():
    # session["userid"]=False
    # session.pop("username", None)
    return render_template("profile.html", title="Profile", profile=True)

@app.route("/leaderboard")
def leaderboard():
    # session["userid"]=False
    # session.pop("username", None)
    return render_template("leaderboard.html", title="Leaderboard", leaderboard=True)

@app.route('/button_clicked', methods=['POST', 'GET'])
def button_clicked():
    # Handle the button click action here
    stop_timer()
    container = request.json['container']
    waterAmount = int(request.json['waterAmount'])
    values = request.json['values']
    result = algorithm(values)
    is_correct = False
    if (int(result['maxArea']) == int(waterAmount) and container in result['possibleSolution']):
        is_correct = True
    print("Received data from JavaScript:", result['maxArea'])
    response_data = {"message": "The result is wrong!"}
    if is_correct == True:
        response_data = {"message": "The result is right!"}
    return jsonify(response_data)