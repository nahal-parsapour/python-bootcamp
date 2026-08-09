# create a file with 200random numbers
import random

def generate_random_numbers(filename, count=200):
    try:
        with open(filename, "w") as f:
            for _ in range(count):
                number = random.randint(1, 1000)
                f.write(str(number) + '\n')
        print(f"{filename} created with {count} random numbers.")
    except PermissionError:
        print(f"ERROR: Permission denied while creating {filename}.")
    except Exception as e:
        print(f"Unexpected error: {e}")

generate_random_numbers('data.txt')