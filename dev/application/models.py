import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

class User():
    def __init__(self, username, firstname, lastname, email, password):
        self.__username = username
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email
        self.__password = generate_password_hash(password)

    def set_password(self, password):
        self.__password = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.__password, password)

    def get_username(self):
        return self.__username
    
    def get_email(self):
        return self.__email
    
    def get_firstname(self):
        return self.__firstname
    
    def get_lastname(self):
        return self.__lastname
    
    def get_all(self):
        connection = self.establish_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM USERS') 
        data = cursor.fetchall() 
        cursor.close()
        return data
    
    def get_one(self, username):
        connection = self.establish_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM USERS WHERE username = (username) VALUES (?)', (username)) 
        data = cursor.fetchone()
        cursor.close()
        return data
    
    def establish_connection(self):
        connection = sqlite3.connect('application/database.db') 
        connection.row_factory = sqlite3.Row
        return connection
    
    def save(self):
        connection = self.establish_connection()
        print("Successfully connect to database")
        cur = connection.cursor()
        cur.execute('INSERT INTO USERS (username, firstname, lastname, email, password) VALUES (?, ?, ?, ?, ?)',
                         (self.__username, self.__firstname, self.__lastname, self.__email, self.__password))
        connection.commit()
        cur.close()
        print("New user saved.")


