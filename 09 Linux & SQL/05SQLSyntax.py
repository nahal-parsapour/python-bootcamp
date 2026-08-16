# sqlite3 test.db
# sqlite>


# CREATE TABLE students (
#     id INT PRIMARY KEY,
#     name VARCHAR(50),
#     age INT,
#     grade FLOAT
# );
#
#
# CRUD Operations:
# -- درج رکوردها
# INSERT INTO students VALUES (1, 'Ali', 20, 15.5);
# INSERT INTO students VALUES (2, 'Sara', 22, 18.0);
# INSERT INTO students VALUES (3, 'Reza', 19, 14.0);
# INSERT INTO students VALUES (4, 'Nahal', 23, 19.0);
# INSERT INTO students VALUES (5, 'Maryam', 21, 16.5);

# -- آپدیت رکورد
# UPDATE students SET age = 24 WHERE name = 'Nahal';
#
# -- حذف رکورد
# DELETE FROM students WHERE id = 3;
#
# -- نمایش همه رکوردها
# SELECT * FROM students;


# # Joins:
# CREATE TABLE courses (
#     id INT PRIMARY KEY,
#     title VARCHAR(50),
#     student_id INT
# );
#
# INSERT INTO courses VALUES (1, 'Math', 1);
# INSERT INTO courses VALUES (2, 'Physics', 2);
# INSERT INTO courses VALUES (3, 'AI', 4);
#
# -- INNER JOIN
# SELECT students.name, courses.title
# FROM students
# INNER JOIN courses ON students.id = courses.student_id;
#
# -- LEFT JOIN
# SELECT students.name, courses.title
# FROM students
# LEFT JOIN courses ON students.id = courses.student_id;
#
# -- RIGHT JOIN (اگر پشتیبانی شود)
# SELECT students.name, courses.title
# FROM students
# RIGHT JOIN courses ON students.id = courses.student_id;



# # Aggregations:
# -- میانگین سن
# SELECT AVG(age) FROM students;
#
# -- بیشترین نمره
# SELECT MAX(grade) FROM students;
#
# -- تعداد دانشجوها
# SELECT COUNT(*) FROM students;
#
# -- گروه‌بندی بر اساس سن
# SELECT age, COUNT(*) FROM students GROUP BY age;



# CREATE TABLE teachers (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(50) NOT NULL,
#     subject VARCHAR(50) DEFAULT 'Math',
#     UNIQUE(name)
# );


# # CRUD:
# -- درج رکورد با مقادیر پیش‌فرض
# INSERT INTO teachers (name) VALUES ('Ahmad');
#
# -- آپدیت چند رکورد
# UPDATE students SET grade = grade + 1 WHERE age > 20;
#
# -- حذف رکوردها با شرط
# DELETE FROM students WHERE grade < 15;


# # Joins:
# -- FULL OUTER JOIN (در PostgreSQL)
# SELECT students.name, courses.title
# FROM students
# FULL OUTER JOIN courses ON students.id = courses.student_id;
#
# -- SELF JOIN
# SELECT a.name, b.name
# FROM students a
# JOIN students b ON a.age = b.age AND a.id <> b.id;
#
#
# # Aggregations:
# -- شمارش سن‌های یکتا
# SELECT COUNT(DISTINCT age) FROM students;
#
# -- استفاده از HAVING
# SELECT age, COUNT(*)
# FROM students
# GROUP BY age
# HAVING COUNT(*) > 1;
#
# -- مجموع نمره‌ها
# SELECT SUM(grade) FROM students;
