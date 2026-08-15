# 1.sql: sqlite3 scraped_data.db
# 2.
import sqlite3

from websockets import connect

connection = sqlite3.connect('scraped_data.db')
cursor = connection.cursor()

# 3.SQL: -- Create the books table with id, title, price, and category
# CREATE TABLE books (
#     id INTEGER PRIMARY KEY,
#     title TEXT,
#     price REAL,
#     category TEXT
# );


# 4. -- Insert sample book data into the books table
# INSERT INTO books (title, price, category) VALUES
#     ('First Book', 15000, 'Literature'),
#     ('Second Book', 22000, 'Science'),
#     ('Third Book', 18000, 'History'),
#     ('Fourth Book', 30000, 'Literature'),
#     ('Fifth Book', 12000, 'Science');


# 5. -- Select books whose price is higher than the overall average price
# SELECT *
# FROM books
# WHERE price > (SELECT AVG(price) FROM books);


# 6. -- Create the authors table
# CREATE TABLE authors (
#     id INTEGER PRIMARY KEY,
#     name TEXT
# );

# 7. -- Add a foreign key column to books for linking to authors
# ALTER TABLE books ADD COLUMN author_id INTEGER;


