from database import conn, cursor

def create_user(name, email):
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()

def get_user(email):
    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    return cursor.fetchone()

def add_points(email, amount):
    points = int(amount // 10)
    cursor.execute("UPDATE users SET points = points + ? WHERE email=?", (points, email))
    conn.commit()

def redeem_points(email, points):
    cursor.execute("SELECT points FROM users WHERE email=?", (email,))
    user = cursor.fetchone()
    if user and user[0] >= points:
        cursor.execute("UPDATE users SET points = points - ? WHERE email=?", (points, email))
        conn.commit()
        return True
    return False
