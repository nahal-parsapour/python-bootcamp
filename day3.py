# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(50))


numbers = [2, 3, 10, 12, 15]
def sum_avg(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return (total, avg)
print(sum_avg(numbers))



