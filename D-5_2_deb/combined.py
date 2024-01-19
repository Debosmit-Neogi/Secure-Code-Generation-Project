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

def remove_email_from_all_subscriptions_return_count(email):
     db = get_db_connection()
     cursor = db.cursor()
     cursor.execute("SELECT * FROM subscriptions WHERE email = '%s'" % email)
     rows = cursor.fetchall()
     if len(rows) == 0:
         return 0
     cursor.execute("DELETE FROM subscriptions WHERE email = '%s'" % email)
     db.commit()
     return len(rows)

def remove_email_from_all_subscriptions_return_count(email):
     db = get_db_connection()
     cursor = db.cursor()
     cursor.execute("SELECT * FROM subscriptions WHERE email = '%s'" % email)
     count = 0
     for row in cursor.fetchall():
         count += 1
         cursor.execute("DELETE FROM subscriptions WHERE id = %d" % row[0])
     db.commit()
     db.close()
     return count
def remove_email_from_all_subscriptions_return_count(email):
     db = get_db_connection()
     cur = db.cursor()
     cur.execute("DELETE FROM subscriptions WHERE email=%s", (email,))
     db.commit()
     count = cur.rowcount
     db.close()
     return count
def remove_email_from_all_subscriptions_return_count(email):
     db = get_db_connection()
     cursor = db.cursor()
     query = "DELETE FROM subscriptions WHERE email = '%s'" % email
     cursor.execute(query)
     db.commit()
     return cursor.rowcount

def remove_email_from_all_subscriptions_return_count(email):
     db = get_db_connection()
     cursor = db.cursor()
     cursor.execute("DELETE FROM subscriptions WHERE email = %s", (email,))
     count = cursor.rowcount
     db.commit()
     cursor.close()
     db.close()
     return count

def remove_email_from_all_subscriptions_return_count(email):
     db = get_db_connection()
     cur = db.cursor()
     cur.execute("UPDATE subscriptions SET email = '' WHERE email = %s", (email))
     count = cur.rowcount
     db.commit()
     db.close()
     return count

def remove_email_from_all_subscriptions_return_count(email):
     db = get_db_connection()
     cur = db.cursor()
     cur.execute("SELECT * FROM subscriptions WHERE email = '" + email + "'")
     rows = cur.fetchall()
     for row in rows:
         print "Removing email " + email + " from " + row[1] + " list"
         cur.execute("DELETE FROM subscriptions WHERE email = '" + email + "' AND list = '" + row[1] + "'")
     db.commit()
     return len(rows)
def remove_email_from_all_subscriptions_return_count(email):
     db = get_db_connection()
     cursor = db.cursor()
     cursor.execute("DELETE FROM subscriptions WHERE email = %s", (email,))
     db.commit()
     count = cursor.rowcount
     cursor.close()
     db.close()
     return count
def remove_email_from_all_subscriptions_return_count(email):
     db = get_db_connection()
     cursor = db.cursor()
     cursor.execute("DELETE FROM subscriptions WHERE email=%s", (email,))
     db.commit()
     return cursor.rowcount
def remove_email_from_all_subscriptions_return_count(email):
     db = get_db_connection()
     cursor = db.cursor()
     cursor.execute("SELECT * FROM subscriptions WHERE email = %s", (email,))
     results = cursor.fetchall()
     for row in results:
         cursor.execute("DELETE FROM subscriptions WHERE email = %s", (email,))
     db.commit()
     db.close()
     return len(results)
#URL handler to remove a user from all subscriptions
@app.route('/remove', methods=['POST'])
def remove():
    email = request.form['email']
    count = remove_email_from_all_subscriptions_return_count(email)
    return 'Removed %d subscriptions' % count
    
