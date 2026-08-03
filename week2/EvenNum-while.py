# Enter an Even number


num = int(input("Enter a number: "))

while num % 2 != 0:
    print("Number is odd! try again.")
    num = int(input("Enter a number: "))

print(f"Correct! {num} is Even.")
