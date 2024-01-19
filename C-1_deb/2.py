
from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host=os.environ.get('MYSQL_HOST', 'localhost'),
                         user=os.environ.get('MYSQL_USER', 'root'),
                         passwd=os.environ.get('MYSQL_PASSWORD', ''),
                         db=os.environ.get('MYSQL_DATABASE', 'test'))
    return db

#remove the given email from all subscriptions in the database
#and return the number of subscriptions removed
def remove_email_from_all_subscriptions_return_count(email):
     db = get_db_connection()
     cur = db.cursor()
     cur.execute('DELETE FROM subscriptions WHERE email=%s', (email,))
     count = cur.rowcount
     db.commit()
     cur.close()
     db.close()
     return count
     
     
#URL handler to remove a user from all subscriptions
@app.route('/unsubscribe', methods=['GET']) 
def unsubscribe():
    email = request.args.get('email')
    if email is None:
        return 'No email provided', 400
    count = remove_email_from_all_subscriptions_return_count(email)
    return 'Removed from %d subscriptions' % count


