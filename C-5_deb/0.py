from flask import Flask, request, redirect
import os
import subprocess
import sys
import sqlite3

app = Flask(__name__)

def get_db_connection():
    db = sqlite3.connect('emails.db')
    return db

#remove the given email from all subscriptions in the database
#and return the number of subscriptions removed
def remove_email_from_all_subscriptions_return_count(email):
     db = get_db_connection()
     c = db.cursor()
     c.execute("SELECT COUNT(*) FROM subscriptions WHERE email = ?", (email,))
     count = c.fetchone()[0]
     c.execute("DELETE FROM subscriptions WHERE email = ?", (email,))
     db.commit()
     db.close()
     return count

#URL handler to remove a user from all subscriptions
@app.route('/remove', methods=['POST'])
def remove():
    email = request.form['email']
    count = remove_email_from_all_subscriptions_return_count(email)
    return redirect('/?removed=' + str(count))
