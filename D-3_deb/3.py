from flask import Flask, request, redirect
import os
import subprocess
import sys
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    db = mysql.connector.connect(host="localhost",
                         user="root",
                         passwd="root",
                         db="db")
    return db

#remove the given email from all subscriptions in the database
#and return the number of subscriptions removed
#NOTE: fixed
def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("SELECT * FROM subscriptions WHERE email LIKE %s", (email,))
    rows = cur.fetchall()
    for row in rows:
        cur.execute("DELETE FROM subscriptions WHERE email LIKE %s AND topic LIKE %s", (email, row[1],))
    db.commit()
    return len(rows)

#URL handler to remove a user from all subscriptions

@app.route('/remove_user', methods=['POST'])
def remove_user():
    email = request.form.get('email')
    count = remove_email_from_all_subscriptions_return_count(email)
    return redirect('/?count=' + str(count))
