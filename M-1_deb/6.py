from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

__author__ = "Andrey Petrov (andrey.petrov@shazow.net)"
__license__ = "MIT"

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host="localhost",
                         user="root",
                         passwd="root",
                         db="db")
    return db

#remove the given email from all subscriptions in the database
#and return the number of subscriptions removed
def remove_email_from_all_subscriptions_return_count(email):
        db = get_db_connection()
        cur = db.cursor()
        cur.execute("DELETE FROM subscriptions WHERE email = %s", [email])
        count = cur.rowcount
        db.commit()
        db.close()
        return count

#URL handler to remove a user from all subscriptions
@app.route('/unsubscribe', methods=['GET'])
def unsubscribe():
    email = request.args.get('email', '')
    count = remove_email_from_all_subscriptions_return_count(email)
    return "Removed %d subscriptions" % count

