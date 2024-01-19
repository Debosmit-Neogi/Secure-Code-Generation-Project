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
     sql = "DELETE FROM subscriptions WHERE email = %s"
     cursor.execute(sql, (email,))
     db.commit()
     count = cursor.rowcount
     cursor.close()
     db.close()
     return count

##URL handler to remove a user from all subscriptions
@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    email = request.form['email']
    count = remove_email_from_all_subscriptions_return_count(email)
    return "Removed from %d subscriptions" % count

