# # ساخت فایل setup.sql
# echo "CREATE TABLE test (id INT, name TEXT);" > setup.sql
# echo "INSERT INTO test VALUES (1, 'Ali');" >> setup.sql
#
# # اجرای فایل SQL روی دیتابیس SQLite
# sqlite3 test.db < setup.sql
#
# # بررسی خروجی
# sqlite3 test.db "SELECT * FROM test;" > output.txt
#
# # تحلیل خروجی با لینوکس
# cat output.txt
# grep "Ali" output.txt
# wc -l output.txt




# # ساخت اسکریپت bash
# echo '#!/bin/bash
# sqlite3 test.db <<EOF
# CREATE TABLE people (id INT, name TEXT);
# INSERT INTO people VALUES (1, "Ali");
# INSERT INTO people VALUES (2, "Sara");
# EOF
# ' > setup.sh
#
# chmod +x setup.sh
# ./setup.sh
#
# # اجرای کوئری و ذخیره خروجی
# sqlite3 test.db "SELECT * FROM people;" > result.txt
#
# # تحلیل خروجی
# grep "Sara" result.txt
# wc -l result.txt
