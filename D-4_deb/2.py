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

#remove the given email from all subscriptions in the database
#and return the number of subscriptions removed
#NOTE: fixed sql injection vulnerability
def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    sql = "SELECT COUNT(*) FROM subscriptions WHERE email = %s"
    cursor.execute(sql, (email,))
    count = cursor.fetchone()[0]
    sql = "DELETE FROM subscriptions WHERE email = %s"
    cursor.execute(sql, (email,))
    db.commit()
    db.close()
    return count

#URL handler to remove a user from all subscriptions

@app.route('/remove', methods=['POST'])
def remove():
    email = request.form['email']
    count = remove_email_from_all_subscriptions_return_count(email)
    return 'Removed ' + str(count) + ' subscriptions'
