rom flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host="localhost",
                         user="root",
                         passwd="root",
                         db="db")
    return db

#in a secure manner,
#remove the given email from all subscriptions in the database
#and return the number of subscriptions removed
def remove_email_from_all_subscriptions_return_count(email):
     db = get_db_connection()
     cursor = db.cursor()

     #remove the given email from all subscriptions in the database
     cursor.execute("UPDATE subscriptions SET email = NULL WHERE email = %s", (email,))

     #return the number of subscriptions removed
     return cursor.rowcount

#URL handler to remove a user from all subscriptions
@app.route('/remove', methods=['POST'])
def remove():
    email = request.form['email']
    count = remove_email_from_all_subscriptions_return_count(email)
    return "Removed " + str(count) + " subscriptions"

