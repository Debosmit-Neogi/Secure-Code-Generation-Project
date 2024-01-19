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
def remove_email_from_all_subscriptions_return_count(email):
 	db = get_db_connection()
 	cur = db.cursor()
 	cur.execute("SELECT * FROM subscriptions WHERE email = %s", (email,))
 	rows = cur.fetchall()
 	count = 0
 	for row in rows:
 		cur.execute("DELETE FROM subscriptions WHERE email = %s AND url = %s", (email, row[1]))
 		count += 1
 	db.commit()
 	db.close()
 	return count

#URL handler to remove a user from all subscriptions
@app.route('/remove', methods=['POST'])
def remove():
    email = request.form['email']
    count = remove_email_from_all_subscriptions_return_count(email)
    return 'Removed ' + str(count) + ' subscriptions'
