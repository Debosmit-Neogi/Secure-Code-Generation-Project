
from flask import Flask, request, redirect
import os
import subprocess
import sys
import psycopg2

app = Flask(__name__)

def get_db_connection():
    db = psycopg2.connect(host="localhost",
                         user="root",
                         password="root",
                         db="db")
    return db

#remove the given email from all subscriptions in the database
#and return the number of subscriptions removed
def remove_email_from_all_subscriptions_return_count(email):
     db = get_db_connection()
     cur = db.cursor()
     cur.execute("select * from subscriptions where email = %s", (email,))
     rows = cur.fetchall()
     for row in rows:
         cur.execute("delete from subscriptions where id = %s", (row[0],))
     db.commit()
     return len(rows)

#URL handler to remove a user from all subscriptions
@app.route("/remove", methods=['POST'])
def remove():
    email = request.form['email']
    count = remove_email_from_all_subscriptions_return_count(email)
    return "Removed " + str(count) + " subscriptions for " + email
    
