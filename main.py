from distutils.log import debug
from email import message
from email.mime import base, image
from fileinput import filename
import imp
from itertools import count
import json
from pydoc import cli
from urllib import response
from flask import Flask, jsonify, render_template, request, redirect, url_for, session,Response,send_file
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import os 
import RSA.rsa as rsa
import socket
import server
import threading
import client
from PIL import Image
import numpy as np
import string    
import random
import concurrent.futures
from multiprocessing.pool import ThreadPool
import sys
import ast
import base64
import io
import socket
import Cipher.cipher as cipher



app = Flask(__name__)
app.run(debug=True)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'your secret key'

# Enter your database connection details below
app.config['MYSQL_HOST'] = os.environ.get('DATABASE_URL')
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'cryto'
app.config["SESSION_TYPE"] = "filesystem"

# Intialize MySQL
mysql = MySQL(app)

t1=threading.Thread(target=server.do)
t1.start()




mess='' 
def put_session(message):
    global mess
    mess = message
    

def generate_key():
    
   
   num = [0,1,2,3,4,5,6,7,8,9]
   key = num
   random.shuffle(key)
   key=str(key)
   key=key.replace('[','')
   key=key.replace(']','')
   return key

generate_key()
@app.route('/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        # Fetch all records and return result
        account =cursor.fetchone()
        
        if account:
            hostname = os.environ.get('ip')
            cursor.execute('UPDATE accounts SET hostname = %s WHERE id = %s', (hostname,account['id'],))
            mysql.connection.commit()
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            return redirect('/chat')
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    return render_template('index.html', msg='')

    


@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    file=''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:

            rsa.new_key()
            fo=open("public_keys.txt","r")
            n = int(fo.readline())
            e = int(fo.readline())
            fo.close()
            os.remove("public_keys.txt")
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s,%s,%s,NULL)', (username, password, email, n, e))
            mysql.connection.commit()
            file=open("private_keys.txt","r")
            v=file.readline()
            w=file.readline()
            file.close()
            file=v+""+w
            #os.remove("private_keys.txt")
            msg = 'You have successfully registered!'
            #return send_file('private_keys.txt', attachment_filename='private_keys.txt')
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    
    return render_template('register.html', msg=msg,file=file)




    

@app.route('/chat', methods=['GET', 'POST'])
def chat():

    if(mess!=''):
       
        if request.method == 'POST' and 'dec' in request.form:
            #print(message,file=sys.stderr)
            keylenlen=mess[0]
            keylenen=int(keylenlen)

            keylen=mess[1:keylenen+1]
            keylen=int(keylen)
            
            key=mess[keylenen+1:keylenen+keylen+1]
            
            
            print(key,file=sys.stderr)
            key=rsa.decrypt(key)
            #message=RT.decrypt(mess[keylen+2:],key)
            print(key,file=sys.stderr)
            
            message=cipher.decrpyt(mess[keylen+1+keylenen:],key)
            #print(message,file=sys.stderr)
            

            image=ast.literal_eval(message)
            image=np.array(image)
            image=Image.fromarray((image).astype(np.uint8)).save("static/image.png")

            #print(image,file=sys.stderr)




    if request.method == 'POST' and 'username' in request.form:
        id=request.form['username']
        file = request.files['file']
        image=Image.open(file)
       
        key=generate_key()
        data=np.array(image)
        data=data.tolist()
        
       
        enc=cipher.encrypt(str(data),key)
       
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (id,))
        account = cursor.fetchone()
        if account:
            n=account.get('n')
            e=account.get('e')
            
            key=rsa.encrypt(key,e,n)
            
            message=str(len(str(len(str(key)))))+str(len(str(key)))+""+str(key)+""+str(enc)
            print(len(str(key)),file=sys.stderr)
            client.do(message, str(account['hostname']))
        
        


    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username != %s', (session['username'],))
        account = cursor.fetchall()
        return render_template('chat.html', username=session['username'],account=account,mess=mess)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

