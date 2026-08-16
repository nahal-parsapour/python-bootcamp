# # تغییر سطح دسترسی
# chmod 644 week9/a.txt
#
# # ساخت اسکریپت و قابل اجرا کردن
# echo 'echo "Run script!"' > run.sh
# chmod +x run.sh
# ./run.sh
#
# # تغییر دسترسی فولدر
# mkdir private
# chmod 700 private
#
# # تغییر مالک و گروه (نیاز به sudo)
# sudo chown $USER week9/b.txt
# sudo chgrp $USER week9/c.txt


# id
#
# ➜  09 Linux & SQL git:(main) ✗ id
# uid=501(nahal) gid=20(staff) groups=20(staff),12(everyone),
# 61(localaccounts),79(_appserverusr),80(admin),81(_appserveradm),
# 98(_lpadmin),701(com.apple.sharepoint.group.1),(333(piavpn),33(_appstore),
# 100(_lpoperator),204(_developer),250(_analyticsusers),395(com.apple.access_ftp),
# 398(com.apple.access_screensharing),399(com.apple.access_ssh),
# 400(com.apple.access_remote_ae))
#
# sudo chgrp staff week9/c.txt
#
#
# or:
# sudo groupadd nahal
# sudo chgrp nahal week9/c.txt

# # بررسی سطح دسترسی
# ls -l week9
#
# # تغییر مالک فایل
# sudo chown $USER week9/a.txt
#
# # تغییر گروه فایل
# sudo chgrp $USER week9/b.txt
# sudo chgrp staff week9/b.txt       # in mac
#
# # تست دسترسی با کاربر دیگر (اگر داری)
# su otheruser
# cat week9/a.txt
