import sqlite3
from flask import Flask
from flask import render_template
from CreateAccount import registration

app = Flask(__name__)
app.secret_key="__privatekey__"

@app.route('/')
def defaultHome():
    return render_template('LogIn.html')

def __init__(self):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("CREATE TABLE user1(name text, password text")

    conn.commit()
    conn.close()

@app.route('/registration',methods=['POST','GET'])
