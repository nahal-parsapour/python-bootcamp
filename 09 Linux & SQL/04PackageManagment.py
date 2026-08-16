# # نصب پکیج (مثلاً htop)
# sudo apt install htop   # روی Ubuntu/Debian
# brew install htop       # روی macOS
#
# # بررسی نسخه
# htop --version
#
# # حذف پکیج
# sudo apt remove htop
# brew uninstall htop
#
# # لیست پکیج‌ها
# apt list --installed | head -n 10
# brew list # for mac


# # جستجوی پکیج
# apt search curl
# brew search curl
#
# # نصب نسخه خاص
# sudo apt install curl=7.68.0-1ubuntu2.6
#
# # به‌روزرسانی همه پکیج‌ها
# sudo apt upgrade
# brew upgrade
#
# # بررسی وابستگی‌ها
# apt show curl
# brew info curl
