import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                username TEXT,
                email TEXT UNIQUE,
                password TEXT
            )''')

conn.commit()
conn.close()
