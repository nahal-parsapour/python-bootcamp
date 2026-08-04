# practice how function works in python

def add(a, b):
    return a + b

print(add(8, 25))


def average(numbers):
    return sum(numbers) / len(numbers)

print(average([1, 2, 3]))


def count_chars(text):
    return len(text)

print(count_chars("Hello world!"))


def even_numbers(nums):
    return [n for n in nums if n % 2 == 0]

print(even_numbers([1, 2, 3, 4, 5]))