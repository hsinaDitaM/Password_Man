import sqlite3

conn = sqlite3.connect('password.db')

c = conn.cursor()

c.execute("""CREATE TABLE passwords (
            first text,
            last text,
            password text
            )""")

conn.commit()

conn.close()