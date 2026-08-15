import sqlite3

connection = sqlite3.connect('shop.db')
cursor = connection.cursor()


# queries
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())


# most orders
cursor.execute("""
SELECT users.name, COUNT(orders.id) AS total_orders
FROM users
LEFT JOIN orders ON users.id = orders.user_id
GROUP BY users.id
ORDER BY total_orders DESC
""")

print(cursor.fetchall())


# avg of every order
cursor.execute("""
SELECT users.name, AVG(orders.amount) AS avg_amount
FROM users
LEFT JOIN orders ON users.id = orders.user_id
GROUP BY users.id
ORDER BY avg_amount DESC
""")

print(cursor.fetchall())


# Users with no order
cursor.execute("""
SELECT users.name
FROM users
LEFT JOIN orders ON users.id = orders.user_id
WHERE orders.id IS NULL""")

print(cursor.fetchall())


# orders in past 30days
cursor.execute("""
SELECT * FROM orders
WHERE created_at >= date('now', '-30 days')
""")

print(cursor.fetchall())
