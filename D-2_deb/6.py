from flask import Flask, request, redirect
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

#using the given email, remove it from all subscriptions in the database
#and return the number of subscriptions removed
def remove_email_from_all_subscriptions_return_count(email):
     db = get_db_connection()
     cursor = db.cursor()
     cursor.execute("SELECT * FROM subscriptions WHERE email = %s", (email,))
     subscriptions = cursor.fetchall()
     for subscription in subscriptions:
         cursor.execute("DELETE FROM subscriptions WHERE name = %s AND email = %s", (subscription[0], subscription[1]))
     cursor.execute("SELECT COUNT(*) FROM subscriptions WHERE email = %s", (email,))
     subscription_count = cursor.fetchone()[0]
     db.commit()
     db.close()
     return subscription_count

##URL handler to remove a user from all subscriptions
@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    email = request.form['email']
    count = remove_email_from_all_subscriptions_return_count(email)
    return "Removed from %d subscriptions" % count

