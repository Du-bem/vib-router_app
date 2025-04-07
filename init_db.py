import sqlite3

DATABASE = "db/database.db"

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()


def insert_user(email, password):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
        conn.commit()
    except sqlite3.IntegrityError:
        print("User already exists!")
    finally:
        conn.close()


if __name__ == "__main__":
    init_db()
    print("Database initialized!")
    insert_user("test@test.com", "123")