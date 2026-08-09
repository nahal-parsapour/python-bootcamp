# Find ".txt" files with os.walk & print size
import os

def find_txt_files_and_size(root_dir="."):
    try:
        txt_files = []
        for dirpath, dirnames, filenames in os.walk(root_dir):
            for file in filenames:
                if file.endswith(".txt"):
                    full_path = os.path.join(dirpath, file)
                    try:
                        size = os.path.getsize(full_path)
                        txt_files.append((full_path, size))
                        print(f"File: {full_path}, Size: {size} bytes")
                    except OSError as e:
                        print(f"Could't get size for {full_path}: {e}")
        if not txt_files:
            print("no '.txt' files found.")
        return txt_files
    except PermissionError:
        print("Error: Permission denied while walking through directories.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Test
if __name__ == "__main__":
    find_txt_files_and_size()