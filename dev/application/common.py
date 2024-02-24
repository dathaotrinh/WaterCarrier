import sqlite3

def get_all():
    connection = establish_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM USERS')
    data = cursor.fetchall()
    cursor.close()
    return data


def get_one(username):
    connection = establish_connection()
    cursor = connection.cursor()
    cursor.execute(
        'SELECT * FROM USERS WHERE username = (username) VALUES (?)', (username))
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
