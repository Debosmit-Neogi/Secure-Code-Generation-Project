#!/usr/bin/env python3
from flask import Flask, request, redirect
from urllib.parse import urlparse
import os
import subprocess
import sys
import MySQLdb
app = Flask(__name__)


def get_db_connection():
   db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
   return db
def insert_user_message_in_db(username, message):
   db = get_db_connection()
   cursor = db.cursor()
   cursor.execute("INSERT INTO messages (username, message) VALUES ('%s', '%s')" % (username, message))
   db.commit()
   cursor.close()
   db.close()
def get_user_messages_from_db(username):
   db = get_db_connection()
   cursor = db.cursor()
   cursor.execute("SELECT message FROM messages WHERE username='%s'" % username)
   messages = cursor.fetchall()
   cursor.close()
   db.close()
   return messages
