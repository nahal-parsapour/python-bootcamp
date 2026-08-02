# odd/even

def num_types(num):
    if num % 2 == 0:
        return "Even"
    elif num % 2 == 1:
        return "Odd"
print(num_types(10))


def num_types():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        return "Even"
    elif num % 2 == 1:
        return "Odd"
print(num_types())
