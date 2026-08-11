# Work with directories (pathlib/os)
import os
from pathlib import Path

def create_backup_folder(folder_name="backup_1405"):
    try:
        Path(folder_name).mkdir(exist_ok=True)
        print(f"Folder '{folder_name}' is ready (created or already exists).")
    except PermissionError:
        print(f"Error: Permission denied to create folder '{folder_name}'.")
    except Exception as e:
        print(f"Unexpected error while creating folder: {e}")


# Test it
if __name__ == "__main__":
    create_backup_folder()