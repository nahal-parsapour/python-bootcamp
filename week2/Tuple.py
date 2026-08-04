# tuple methods

user = ("Nahal", 32, "Ai", ["python", "robotics"])

print("Name: ", user[0])
print("Age: ", user[1])
print("Skills: ", user[3])

user[3].append("Ai")
print("Updated Skills: ", user[3])

new_user = (user[0], user[1] + 1, user[2], user[3])
print("New User: ", new_user)

has_AI = "Ai" in user[3]
print("Has AI skill?: ", has_AI)

print("=== Lists are mutable, Tuples are immutable ===")