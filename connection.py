import sqlite3

# Connect to the database file
conn = sqlite3.connect("studentdb")
cursor = conn.cursor()

# Example: create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    birthday DATE,
    phone TEXT,
    course TEXT,
    address TEXT
)
""")

conn.commit()
conn.close()
print("Connected to student.db successfully!")
