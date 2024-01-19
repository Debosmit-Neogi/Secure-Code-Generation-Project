from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

def get_db_conection():
    db = MySQLdb.connect(host="localhost",
                         user="root",
                         passwd="root",
                         db="db")
    return db

#remove the givn email from all subscriptions in the datbase
#and return the numbr of subscriptons removed
def remove_email_from_all_subsciptons_return_count(email):
     db = get_db_conection()
     cur = db.cursor()
     sql = "DELETE FROM subscriptions WHERE email = %s"
     cur.execute(sql, (email,))
     db.commit()
     return cur.rowcount

#URL handler to remove a user from all subscriptons
@app.route('/remove_user', methods=['GET'])
def remove_user():
    email = request.args.get('email')
    count = remove_email_from_all_subsciptons_return_count(email)
    return "Removed " + str(count) + " subscriptions for " + email

