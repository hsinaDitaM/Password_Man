import sqlite3

conn = sqlite3.connect('user.db')

c = conn.cursor()

# c.execute("""CREATE TABLE users (
#             site text,
#             username text,
#             password text,
#             link text
#             )""")

# c.execute("INSERT INTO users VALUES ('github', 'Mati', '1234', 'github.com')")

c.execute("SELECT * FROM users WHERE username='Mati'")

print(c.fetchone())

conn.commit()

conn.close()