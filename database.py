import sqlite3

conn = sqlite3.connect("loyalty.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    points INTEGER DEFAULT 0
)
""")
conn.commit()
