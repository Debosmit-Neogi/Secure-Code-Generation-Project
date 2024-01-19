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

#delete the given email from all subscriptions in the database
#and return the number of subscriptions removed
def remove_email_from_all_subscriptions_return_count(email):
     db = get_db_connection()
     cur = db.cursor()
     cur.execute("DELETE FROM subscriptions WHERE email = %s", [email])
     db.commit()
     return cur.rowcount

#URL handler to remove a user from all subscriptions
@app.route('/unsubscribe', methods=['GET'])
def unsubscribe():
    email = request.args.get('email')
    if email is None:
        return "Error: no email provided"
    else:
        count = remove_email_from_all_subscriptions_return_count(email)
        return "Successfully removed " + str(count) + " subscriptions for " + email
        
