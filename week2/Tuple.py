# tuple methods

t = ("Nahal", 32, "Ai", ["python", "robotics"])

print("Name: ", t[0])
print("Age: ", t[1])
print("Skills: ", t[3])

t[3].append("Ai")
print("Updated Skills: ", t[3])

print("Lists are mutable, Tuples are immutable")