# Built-in Functions

nums = [10, 15, 8, 2, 7]

print("len: ", len(nums))
print("max: ", max(nums))
print("min: ", min(nums))
print("sum: ", sum(nums))
print("sorted: ", sorted(nums))

# map
squared = list(map(lambda x: x**2, nums))
print("squared: ", squared)

# filter
filtered = list(filter(lambda x: x > 7, nums))
print("filtered: ", filtered)

# zip
names = ["nahal", "ali", "sara"]
ages = [32, 34, 22]
print(list(zip(names, ages)))

# enumerate
for index, item in enumerate(names):
    print(index, item)

# Example
scores = [18, 20, 19, 12]
print("Average:", sum(scores) / len(scores))