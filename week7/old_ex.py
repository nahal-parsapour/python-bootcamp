# #
# import os, random
#
# folder = ''
# files = [ f for f in os.listdir(folder) if f.endwith('.mp3') ]
# random.shuffle(files)
# for i, f in enumerate(files):
#     old_path = os.path.join(folder, f)
#     new_name = f'{i + 1:03D}_{f}'
#     new_path = os.path.join(folder, f)
#     os.rename(old_path, new_path)

import os, random

folder = "E:\\Remix"
all_files = []

# پیمایش همه‌ی فولدرها و زیر‌فولدرها
for root, dirs, files in os.walk(folder):
    for f in files:
        if f.endswith(".mp3"):
            all_files.append(os.path.join(root, f))

# بهم ریختن ترتیب فایل‌ها
random.shuffle(all_files)

# تغییر نام به صورت رندوم
for i, file_path in enumerate(all_files):
    folder_path = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)
    new_name = f"{i+1:03d}_{file_name}"
    new_path = os.path.join(folder_path, new_name)
    os.rename(file_path, new_path)