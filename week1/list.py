list = [2, 5, 3]
list.append(7)
print(max(list))
print(list)


d = {"nahal":24, "ali":30}
print(d["ali"])

numbers = [4, 8, 12, 16, 20]
result = []
for num in numbers:
    if num > 5:
        result.append(num)
print(result)


numbers = [4, 8, 12, 16, 20]
print([i for i in numbers if i > 5])


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



