import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

class User(object):
    def __init__(self, userid, username, firstname, lastname, email, password):
        self.__userid = userid
        self.__username = username
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email
        # self.__password = generate_password_hash(password)
        self.__password = password

    def set_password(self, password):
        # self.__password = generate_password_hash(password)
        self.__password = password

    # def get_password(self, password):
    #     return check_password_hash(self.__password, password)

    def get_password(self):
        # return check_password_hash(self.__password, password)
        return self.__password

    def get_username(self):
        return self.__username
    
    def get_email(self):
        return self.__email
    
    def get_firstname(self):
        return self.__firstname
    
    def get_lastname(self):
        return self.__lastname

    def get_userid(self):
        return self.__userid

class Event(object):
    def __init__(self, eventid, score, difficulty, date, duration, userid):
        self.__eventid = eventid
        self.__score = score
        self.__difficulty = difficulty
        self.__date = date
        self.__duration = duration
        self.__userid = userid

    def get_eventid(self):
        return self.__eventid
    
    def get_score(self):
        return self.__score

    def get_difficulty(self):
        return self.__difficulty
    
    def get_date(self):
        return self.__date
    
    def get_duration(self):
        return self.__duration
    
    def get_userid(self):
        return self.__userid

