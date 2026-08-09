# Copy files with shutil.copy2
import os
import shutil
from pathlib import Path

def copy_txt_files_to_backup(backup_folder="backup_1405", root_dir="."):
    Path(backup_folder).mkdir(exist_ok=True)

    try:
        copied_count = 0
        for dirpath, dirnames, filenames in os.walk(root_dir):
            if backup_folder in dirpath:
                continue
            for file in filenames:
                if file.endswith(".txt"):
                    src_path = os.path.join(dirpath, file)
                    base, ext = os.path.splitext(file)
                    new_name = f"{base}_copy{ext}"
                    dst_path = os.path.join(backup_folder, new_name)

                    try:
                        shutil.copy2(src_path, dst_path)
                        print(f"Copied {src_path} -> {dst_path}")
                        copied_count += 1
                    except (PermissionError, OSError) as e:
                        print(f"Error copying {src_path}: {e}")
        print(f"Total '.txt' files copied: {copied_count}")
    except PermissionError:
        print("Error: Permission denied while accessing directories.")
    except Exception as e:
        print(f"Unexpected error: {e}")


# test
if __name__ == "__main__":
    copy_txt_files_to_backup()