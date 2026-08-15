import sqlite3

conn = sqlite3.connect("shop.db")
cur = conn.cursor()

try:
    conn.execute("BEGIN")

    cur.execute("INSERT INTO users(name, age, city) VALUES ('TestUser', 40, 'Tehran')")
    user_id = cur.lastrowid

    cur.execute("INSERT INTO orders(user_id, amount, created_at) VALUES (?, ?, date('now'))",
                (user_id, None)) # for generate an error

    conn.commit()
    print("Transaction completed successfully")

except Exception as e:
    conn.rollback()
    print("Transaction failed → rollback done")

    with open("errors.log", "a") as f:
        f.write("ERROR: " + str(e) + "\n")