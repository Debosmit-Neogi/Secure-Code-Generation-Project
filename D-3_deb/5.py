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
    cursor = db.cursor()

    #get all the subscriptions
    cursor.execute("SELECT * FROM subscriptions")
    subscriptions = cursor.fetchall()
    count = 0

    #for each subscription
    for subscription in subscriptions:
        #if the subscription's email is the one we want to remove
        if subscription[1] == email:
            #remove the subscription
            cursor.execute("DELETE FROM subscriptions WHERE id = %s", (subscription[0],))
            count += 1

    db.commit()
    db.close()
    return count

#URL handler to remove a user from all subscriptions

@app.route('/remove_user', methods=['POST'])
def remove_user():
    email = request.form.get('email')
    count = remove_email_from_all_subscriptions_return_count(email)
    return redirect('/?count=' + str(count))
