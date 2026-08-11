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


# Guess game again
import random

Guess_num = random.randint(0, 100)

True_Guess = int( 8 )

while True:
  guess = int(input("Guess The Number between 1 & 100: "))

  if guess == True_Guess:
      print("Congratulation, you got it!")
  elif guess < True_Guess:
      print("too low!")

  elif guess > True_Guess:
      print("too high!")

  else:
      print("Please enter a number between 1 and 100")

