# calculator (input/print)

print("Simple Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Choose operation: (+ or - ): ")
if operation == "+":
    print("Result: ", num1 + num2)
elif operation == "-":
    print("Result: ", num1 - num2)
else:
    print("Invalid operation")