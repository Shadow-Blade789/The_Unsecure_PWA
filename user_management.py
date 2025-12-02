import sqlite3 as sql
import time
import random


def insertUser(username, DoB, salt_str, hashedpw_str):
    con = sql.connect("database_files/database.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO users (username,dateOfBirth,salt,hashedpw) VALUES (?,?,?,?)",
        (username, DoB, salt_str, hashedpw_str),
    )
    con.commit()
    con.close()


# user_management.py (FIXED)


def retrieveUsers(username):
    con = sql.connect("database_files/database.db")
    cur = con.cursor()
    cur.execute(
        "SELECT username, salt, hashedpw FROM users WHERE username = ?",
        (username,),
    )
    user_record = cur.fetchone()
    con.close()
    if user_record:
        # user_record is (username, salt_str, hashedpw_str)
        return user_record
    else:
        return None
    if cur.fetchone() == None:
        con.close()
        return False
    else:
        # statement is looking up for user with password, not checking if it is the same user as username
        # Plain text log of visitor count as requested by Unsecure PWA management
        with open("visitor_log.txt", "r") as file:
            number = int(file.read().strip())
            number += 1
        with open("visitor_log.txt", "w") as file:
            file.write(str(number))
        # Simulate response time of heavy app for testing purposes
        time.sleep(random.randint(80, 90) / 1000)

        # if it doesn't find any users with this password
        # if cur.fetchone() == None:
        #      con.close()
        #      return False
        con.close()
        return True


def insertFeedback(feedback):
    con = sql.connect("database_files/database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO feedback (feedback) VALUES (?)", (feedback,))
    con.commit()
    con.close()


def listFeedback():
    con = sql.connect("database_files/database.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM feedback").fetchall()
    con.close()
    f = open("templates/partials/success_feedback.html", "w")
    for row in data:
        f.write("<p>\n")
        f.write(f"{row[1]}\n")
        f.write("</p>\n")
    f.close()
