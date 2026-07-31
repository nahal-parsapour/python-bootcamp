list = [2, 5, 3]
list.append(7)
print(max(list))
print(list)


d = {"neda":24, "ali":30}
print(d["ali"])

numbers = [4, 8, 12, 16, 20]
result = []
for num in numbers:
    if num > 5:
        result.append(num)
print(result)


numbers = [4, 8, 12, 16, 20]
print([i for i in numbers if i > 5])