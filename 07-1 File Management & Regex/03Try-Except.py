# Manage Errors with try/except
try:
    with open('data.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("File doesn't exist")
except PermissionError:
    print("Permission denied")
else:
    print("File reads successfully")
finally:
    print("End of the task")