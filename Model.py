import sqlite3

conn = sqlite3.connect('password.db')

c = conn.cursor()

# c.execute("""CREATE TABLE passwords (
#             first text,
#             last text,
#             password text
#             )""")

# c.execute("INSERT INTO passwords VALUES ('Site', 'Username', 'Password', 'link')

c.execute("SELECT ")

conn.commit()

conn.clone()