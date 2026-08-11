# factorial with Recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


# sum of nested-list
def deep_sum(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += deep_sum(item)
        else:
            total += item
    return total

print(deep_sum([1,[2, 3], [4, [5]]]))


# finding max number in list
def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    sub_max = find_max(lst[1:])
    return lst[0] if lst[0] > sub_max else sub_max

print("Max of list:", find_max([3, 8, 12, 9, 20, 7]))