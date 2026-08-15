import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    city TEXT
)
""")

users = [
    ("John", 25, "Madrid"),
    ("Sara", 22, "Shiraz"),
    ("Nahal", 32, "Barcelona"),
    ("Yadi", 45, "Tehran"),
    ("Mary", 28, "Shiraz")
]

cur.executemany("INSERT INTO users(name, age, city) VALUES (?, ?, ?)", users)
conn.commit()


print(cur.execute("SELECT * FROM users").fetchall())
print(cur.execute("SELECT * FROM users WHERE age > 25").fetchall())
print(cur.execute("SELECT * FROM users WHERE city='Tehran'").fetchall())
print(cur.execute("SELECT AVG(age) FROM users").fetchone())