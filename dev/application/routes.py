from application import app
from application.timer import CountUpTimer
from flask import render_template, session, redirect, url_for, flash, request, jsonify
from application.models import User, Event
from application.forms import LoginForm, RegisterForm
from random import randint
from application.common import save_user, save_event, get_all, get_one, start_timer, stop_timer, algorithm, reset, get_all_events

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    values = []
    poles = []
    difficulty = "easy"
    timerStart = "False"
    if request.method == "POST":
        if request.form["level"] == "easy":
            timerStart = "True"
            start_timer()
            reset(values, poles)
            difficulty = "easy"
            for i in range(5):
                value = randint(1, 5)
                values.append(value)
                poles.append("Pole " + str(i))
        elif request.form["level"] == "medium":
            timerStart = "True"
            start_timer()
            reset(values, poles)
            difficulty = "medium"
            for i in range(10):
                value = randint(1, 10)
                values.append(value)
                poles.append("Pole " + str(i))
        elif request.form["level"] == "hard":
            timerStart = "True"
            start_timer()
            reset(values, poles)
            difficulty = "hard"
            for i in range(20):
                value = randint(0, 20)
                values.append(value)
                poles.append("Pole " + str(i))
        elif request.form["level"] == "stop":
            timerStart = "False"
            stop_timer()
    return render_template("barchart.html", index=True, values=values, poles=poles, timerStart=timerStart, difficulty=difficulty)

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
        else:
            flash("Something is wrong!", "danger")
    return render_template("login.html", title="Login", login=True)


@app.route("/register", methods=["GET", "POST"])
def register():
    if session.get("username"):
        return redirect(url_for("index"))
    if request.method == "POST":
        count = len(get_all())
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        password_confirm = request.form.get("password_confirm")
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        print(password)
        print(password_confirm)
        if password != password_confirm:
            flash("Passwords do not match!", "danger")
        else:
            user = User(count + 1, username, firstname, lastname, email, password)
            if save_user(user) == True:
                session['userid'] = user.get_userid()
                session['username'] = user.get_username()
                flash(f"{user.get_firstname()}, you are successfully registered!", "success")
                return redirect(url_for("index"))
            else:
                flash("Failed to save new user.", "danger")
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
    difficulty = request.json['difficulty']
    minutes = request.json['minutes']
    seconds = request.json['seconds']
    milliseconds = request.json['milliseconds']
    result = algorithm(values)
    print(result['possibleSolution'])
    print(int(result['maxArea']))
    is_correct = False
    if (int(result['maxArea']) == int(waterAmount) and container in result['possibleSolution']):
        is_correct = True
    print("Received data from JavaScript:", result['maxArea'])
    response_data = {"message": "The result is wrong!"}
    event_len = len(get_all_events())
    duration = "{}:{}:{}".format(minutes, seconds if seconds >= 10 else '0' + str(seconds), milliseconds if milliseconds >= 10 else '0' + str(milliseconds))
    print(duration)
    if is_correct == True:
        response_data = {"message": "The result is right!"}
        if session['userid'] == True:
            event = Event(event_len + 1, difficulty, duration, session['userid'], 1)
            save_event(event)
    else:
        if session['userid'] == True:
            event = Event(event_len + 1, difficulty, duration, session['userid'], 0)
            save_event(event)        
    return jsonify(response_data)