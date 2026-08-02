# Guess Number

import random
print("Guess the Number Game")
secret_num = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_num:
    print("Correct!🎉")
elif guess > secret_num:
    print("Too high!")
elif guess < secret_num:
    print("Too low!")

print(f"The secret number was {secret_num}.")