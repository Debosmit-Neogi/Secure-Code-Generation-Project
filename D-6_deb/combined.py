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
#     """remove the given email from all subscriptions in the database
#     and return the number of subscriptions removed"""
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("DELETE FROM subscriptions WHERE email=%s", (email,))
    db.commit()
    return cursor.rowcount



def remove_email_from_all_subscriptions_return_count(email):
#     """remove the given email from all subscriptions in the database
#     and return the number of subscriptions removed"""
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("DELETE FROM subscriptions WHERE email = '%s'" % email)
    rows_deleted = cur.rowcount
    db.commit()
    db.close()
    return rows_deleted



def remove_email_from_all_subscriptions_return_count(email):
#     """remove the given email from all subscriptions in the database
#     and return the number of subscriptions removed"""
    db = get_db_connection()
    c = db.cursor()
    c.execute("SELECT COUNT(*) FROM subscriptions WHERE email='%s'" % email)
    count = c.fetchone()[0]
    c.execute("DELETE FROM subscriptions WHERE email='%s'" % email)
    db.commit()
    db.close()
    return count



def remove_email_from_all_subscriptions_return_count(email):
#     """remove the given email from all subscriptions in the database
#     and return the number of subscriptions removed"""
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("DELETE FROM subscriptions WHERE email=%s", (email,))
    count = cur.rowcount
    db.commit()
    db.close()
    return count



def remove_email_from_all_subscriptions_return_count(email):
#     """remove the given email from all subscriptions in the database
#     and return the number of subscriptions removed"""
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("DELETE FROM subscriptions WHERE email=%s", (email,))
    count = cursor.rowcount
    db.commit()
    db.close()
    return count



def remove_email_from_all_subscriptions_return_count(email):
#     """remove the given email from all subscriptions in the database
#     and return the number of subscriptions removed"""
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM subscriptions WHERE email='" + email + "'")
    count = cursor.fetchone()[0]
    cursor.execute("DELETE FROM subscriptions WHERE email='" + email + "'")
    db.commit()
    db.close()
    return count



def remove_email_from_all_subscriptions_return_count(email):
#     """remove the given email from all subscriptions in the database
#     and return the number of subscriptions removed"""
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("SELECT COUNT(*) FROM subscriptions WHERE email='%s'" % email)
    count = cur.fetchone()[0]
    cur.execute("DELETE FROM subscriptions WHERE email='%s'" % email)
    db.commit()
    db.close()
    return count



def remove_email_from_all_subscriptions_return_count(email):
#     """remove the given email from all subscriptions in the database
#     and return the number of subscriptions removed"""
    db = get_db_connection()
    cur = db.cursor()
    # check if the email is already in the database
    cur.execute("SELECT email FROM subscriptions WHERE email=%s", (email,))
    if cur.rowcount == 0:
        return 0
    # remove the email from all subscriptions
    cur.execute("DELETE FROM subscriptions WHERE email=%s", (email,))
    db.commit()
    return cur.rowcount

@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    """URL handler to remove a user from all subscriptions"""
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions

