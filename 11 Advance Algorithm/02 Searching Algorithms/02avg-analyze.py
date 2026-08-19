import random

def linear_search_count(arr, target):
    count = 0
    for val in arr:
        count += 1
        if val == target:
            break
    return count

def experiment():
    counts = []
    for _ in range(10):
        arr = [random.randint(1, 500) for _ in range(100)]
        target = random.choice(arr)
        c = linear_search_count(arr, target)
        counts.append(c)
    print("Analyze count: ", counts)
    print("Average:", sum(counts) / len(counts))

experiment()
