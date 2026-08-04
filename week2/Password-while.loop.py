# Safe Password

password = input("Choose a strong password: ")

special_chars = "!@#$%^&*()_+-=<>?,./?;:"

while True:
    if len(password) < 8:
        print("Password must be at least 8 characters long")
    elif not any(ch.isupper() for ch in password):
        print("Password must contain at least one uppercase letter.")
    elif not any(ch.isdigit() for ch in password):
        print("Password must contain at least one digits.")
    elif not any(ch in special_chars for ch in password):
        print("Password must contain at least one special character.")
    else:
        print("Password Accepted")
        break

    password = input("Try again: ")