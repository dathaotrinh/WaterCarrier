import sqlite3

from application.timer import CountUpTimer

def get_all():
    connection = establish_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM USERS')
    data = cursor.fetchall()
    cursor.close()
    return data

def get_one(username):
    print(username)
    connection = establish_connection()
    cursor = connection.cursor()
    cursor.execute(
        'SELECT * FROM USERS WHERE username = ?', (username,))
    data = cursor.fetchone()
    cursor.close()
    return data

def establish_connection():
    connection = sqlite3.connect('application/database.db')
    connection.row_factory = sqlite3.Row
    return connection

def save(user):
    connection = establish_connection()
    print("Successfully connect to database")
    cur = connection.cursor()
    cur.execute('INSERT INTO USERS (username, firstname, lastname, email, password) VALUES (?, ?, ?, ?, ?)',
                    (user.get_username(), user.get_firstname(), user.get_lastname(), user.get_email(), user.get_password()))
    connection.commit()
    cur.close()
    print("New user saved.")

def save(event):
    connection = establish_connection()
    print("Successfully connect to database")
    cur = connection.cursor()
    cur.execute('INSERT INTO Event (score, difficulty, date, duration, userid) VALUES (?, ?, ?, ?, ?)',
                    (event.get_score(), event.get_difficulty(), event.get_date(), event.get_duration(), event.get_userid()))
    connection.commit()
    cur.close()
    print("New event saved.")

timer = None
# Function to start the timer
def start_timer():
    global timer
    if timer and timer.is_running():
        print("Stopping existing timer...")
        timer.stop_timer()
    timer = CountUpTimer()
    timer.start_timer()

# Function to stop the timer
def stop_timer():
    global timer
    if timer:
        return timer.stop_timer()
         
    

def algorithm(height):
    possible_solution = []
    maxarea = 0
    left = 0
    right = len(height) - 1
    while left < right:
        width = right - left
        current_area = min(height[left], height[right]) * width
        if current_area > maxarea:
            maxarea = current_area
            possible_solution.clear()
            possible_solution.append({left, right})
        elif current_area == maxarea:
            possible_solution.append({left, right})     
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return {"maxArea": maxarea, "possibleSolution": possible_solution }

def reset(values, poles):
    values = []
    poles = []

# def calculate_score():
