import sqlite3
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.secret_key="__privatekey__"

@app.route('/')
def defaultHome():
    return render_template('LogIn.html')
def __init__(self):
    conn = sqlite3.connect('user.db')

    c = conn.cursor()

    c.execute("""CREATE TABLE users (
                username text,
                password text
                )""")

    username = """username"""
    password = """password"""

    c.execute("INSERT INTO users VALUES ('Mati', '1234')")

    print(c.fetchone())

    conn.commit()

    conn.close()

    @app.route('/CreateAccount',methods=['POST','GET'])
    