import sqlite3

connection = sqlite3.connect('application/database.db')

with open('application/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO Users (userid, username, firstname, lastname, email, password) VALUES (?, ?, ?, ?, ?, ?)",
            (1, "admin", "admin", "admin", "admin@example.com", "admin")
            )

connection.commit()
connection.close()