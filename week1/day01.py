# input

print("Name: Nahal")
print("Field: Artificial Intelligence")

interests = ["Robotics", "Machine Learning", "Data Science", "Music"]
for item in interests:
    print("Interests: ", item)



name = input("What is your name? ")
age = input("How old are you? ")

print(f"Hello {name}, you are {age} years old!")



def greeting():
    name = input("What is your name? ")
    age = input("How old are you? ")
    return f"Hello, {name}! You are {age} years old."
print(greeting())
