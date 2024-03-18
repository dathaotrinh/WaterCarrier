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

def save_user(user):
    try:
        connection = establish_connection()
        print("Successfully connect to database")
        cur = connection.cursor()
        cur.execute('INSERT INTO USERS (userid, username, firstname, lastname, email, password) VALUES (?, ?, ?, ?, ?, ?)',
                        (user.get_userid(), user.get_username(), user.get_firstname(), user.get_lastname(), user.get_email(), user.get_password()))
        connection.commit()
        rows_affected = cur.rowcount  # Get the number of rows affected
        cur.close()    
        if rows_affected == 1:
            print("New user saved successfully.")
            return True
        else:
            print("Failed to save user.")
            return False
    except Exception as e:
        # Handle any error that occurs
        print("Error:", e)
        return False

def save_event(event):
    try:
        connection = establish_connection()
        print("Successfully connect to database")
        cur = connection.cursor()
        cur.execute('INSERT INTO Event (eventid, difficulty, duration, userid, result) VALUES (?, ?, ?, ?, ?)',
                        (event.get_eventid(), event.get_difficulty(), event.get_duration(), event.get_userid(), event.get_result()))
        connection.commit()
        rows_affected = cur.rowcount  # Get the number of rows affected
        cur.close()
        if rows_affected == 1:
            print("New event saved successfully.")
            return True
        else:
            print("Failed to save event.")
            return False
    except Exception as e:
        # Handle any error that occurs
        print("Error:", e)
        return False

def get_all_events():
    connection = establish_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Event')
    data = cursor.fetchall()
    cursor.close()
    return data

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
    possible_solution = set()
    maxarea = 0
    left = 0
    right = len(height) - 1
    while left < right:
        width = right - left
        current_area = min(height[left], height[right]) * width
        if current_area > maxarea:
            maxarea = current_area
            possible_solution.clear()
            possible_solution.add(f"{left},{right}")
        elif current_area == maxarea:
            possible_solution.add(f"{left},{right}")
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return {"maxArea": maxarea, "possibleSolution": possible_solution }

def reset(values, poles):
    values = []
    poles = []

def calculate_score(M, S, MS, difficulty):
    # Define base score values for each difficulty level
    difficulty_scores = {
        'easy': 100,
        'medium': 200,
        'hard': 300
    }
    
    # Define conversion factors
    MIN_TO_MS = 60 * 1000
    SEC_TO_MS = 1000

    # Convert time to milliseconds
    Total_MS = M * MIN_TO_MS + S * SEC_TO_MS + MS
    
    # Time-based score
    # shorter times get higher scores
    Time_Score = 1 / Total_MS 

    # Difficulty-based score
    Difficulty_Score = difficulty_scores[difficulty]
    
    # Total score
    Total_Score = Time_Score + Difficulty_Score
    
    return Total_Score