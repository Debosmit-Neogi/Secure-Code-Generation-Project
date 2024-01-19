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
     cur.execute("SELECT id FROM subscriptions WHERE email = %s", (email,))
     subscription_ids = cur.fetchall()
     for subscription_id in subscription_ids:
          cur.execute("DELETE FROM subscriptions WHERE id = %s", (subscription_id[0],))
     db.commit()
     return len(subscription_ids)


def remove_email_from_all_subscriptions_return_count(email):
     db = get_db_connection()
     cursor = db.cursor()
     cursor.execute("SELECT COUNT(*) FROM subscriptions WHERE email = %s", (email,))
     (count,) = cursor.fetchone()
     cursor.execute("DELETE FROM subscriptions WHERE email = %s", (email,))
     db.commit()
     cursor.close()
     db.close()
     return count



def remove_email_from_all_subscriptions_return_count(email):
     db = get_db_connection()
     cursor = db.cursor()
     cursor.execute("update subscriptions set email = '' where email = %s", (email,))
     db.commit()
     cursor.execute("select count(*) from subscriptions where email = %s", (email,))
     result = cursor.fetchone()
     db.close()
     return result[0]



def remove_email_from_all_subscriptions_return_count(email):
     db = get_db_connection()
     cur = db.cursor()
     cur.execute("SELECT COUNT(*) FROM subscriptions WHERE email = %s", (email,))
     count = cur.fetchone()[0]
     cur.execute("DELETE FROM subscriptions WHERE email = %s", (email,))
     db.commit()
     db.close()
     return count



def remove_email_from_all_subscriptions_return_count(email):
     db = get_db_connection()
     cur = db.cursor()
     cur.execute("DELETE FROM subscriptions WHERE email=%s", (email,))
     db.commit()
     return cur.rowcount




def remove_email_from_all_subscriptions_return_count(email):
     db = get_db_connection()
     cursor = db.cursor()
     cursor.execute("SELECT * FROM subscriptions WHERE email = %s", (email,))
     subscriptions = cursor.fetchall()
     for subscription in subscriptions:
         cursor.execute("DELETE FROM subscriptions WHERE id = %s", (subscription[0],))
     db.commit()
     db.close()
     return len(subscriptions)



def remove_email_from_all_subscriptions_return_count(email):
     db = get_db_connection()
     cursor = db.cursor()
     cursor.execute("SELECT COUNT(*) FROM subscriptions WHERE email=%s", (email,))
     count = cursor.fetchone()[0]
     cursor.execute("DELETE FROM subscriptions WHERE email=%s", (email,))
     db.commit()
     db.close()
     return count



def remove_email_from_all_subscriptions_return_count(email):
     db = get_db_connection()
     cur = db.cursor()
     cur.execute("DELETE FROM subscriptions WHERE email = %s", (email,))
     count = cur.rowcount
     db.commit()
     cur.close()
     db.close()
     return count



def remove_email_from_all_subscriptions_return_count(email):
     db = get_db_connection()
     cursor = db.cursor()
     cursor.execute("SELECT * FROM subscriptions WHERE email=%s", (email,))
     count = cursor.rowcount
     cursor.execute("DELETE FROM subscriptions WHERE email=%s", (email,))
     db.commit()
     db.close()
     return count

#URL handler to remove a user from all subscriptions
@app.route("/remove", methods=['POST'])
def remove():
    email = request.form['email']
    count = remove_email_from_all_subscriptions_return_count(email)
    return "Removed %d subscriptions" % count
    
