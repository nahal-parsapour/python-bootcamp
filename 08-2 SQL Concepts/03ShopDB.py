import sqlite3
import os

connection = sqlite3.connect('shop.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    city TEXT
)
""")

# for prevent duplicated data:
# CREATE TABLE users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT UNIQUE,
#     age INTEGER,
#     city TEXT
# );


cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    amount REAL NOT NULL,
    created_at TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")

cursor.execute("CREATE INDEX IF NOT EXISTS idx_user_id ON orders(user_id)")
connection.commit()


# add data
users = [
    ("Ali", 25, "Tehran"),
    ("Sara", 30, "Shiraz"),
    ("Nahal", 27, "Tehran"),
    ("Reza", 19, "Mashhad"),
    ("Maryam", 22, "Tabriz")
]

cursor.executemany("INSERT INTO users(name, age, city) VALUES (?, ?, ?)", users)

orders = [
    (1, 120000, "2026-07-01"),
    (1, 450000, "2026-07-15"),
    (2, 90000,  "2026-07-20"),
    (3, 300000, "2026-08-01"),
    (3, 150000, "2026-08-10"),
]

cursor.executemany("INSERT INTO orders(user_id, amount, created_at) VALUES (?, ?, ?)", orders)

connection.commit()

# os.remove("shop.db")