import sqlite3

conn = sqlite3.connect('password.db')

c = conn.cursor()

# c.execute("""CREATE TABLE passwords (
#             first text,
#             last text,
#             password text
#             )""")

c.execute("INSERT INTO passwords VALUES ('github', 'Mati', '1234', 'github.com')")

c.execute("SELECT ⋆ FROM passwords WHERE last='Schafer'")

print(c.fetchone())

conn.commit()

conn.clone()